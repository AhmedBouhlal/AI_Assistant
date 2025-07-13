import customtkinter as ctk
from tkinter import filedialog, messagebox
from threading import Thread
import ast
from assistant_core import load_skills, is_allowed, log_action
from ai_interface import call_ollama

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AssistantGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ultimate AI Assistant")
        self.geometry("900x720")
        self.resizable(True, True)
        self.skills = load_skills()
        self._build_ui()
        self.append_chat("[System] Assistant ready. Type a request or use Skills menu.")

    def _build_ui(self):
        # Chat area (read-only)
        self.chat_area = ctk.CTkTextbox(self, wrap="word", width=760, height=400, font=("Segoe UI", 13))
        self.chat_area.configure(state="disabled")
        self.chat_area.grid(row=0, column=0, columnspan=3, padx=20, pady=(18, 4), sticky="nsew")

        # User input field
        self.entry_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, width=590, font=("Segoe UI", 15), height=38, corner_radius=12)
        self.entry.grid(row=1, column=0, padx=(20, 4), pady=4, sticky="ew")
        self.entry.bind('<Return>', self.send_message)

        # Send button
        self.button = ctk.CTkButton(self, text="Send", width=110, height=38, command=self.send_message, font=("Segoe UI", 13, "bold"))
        self.button.grid(row=1, column=1, padx=4, pady=4, sticky="ew")

        # Skills ComboBox with search/filter
        self.skill_names = [skill["description"] for skill in self.skills.values()]
        self.skill_picker = ctk.CTkComboBox(
            self,
            values=self.skill_names,
            width=340,
            font=("Segoe UI", 12)
        )
        self.skill_picker.set("Type or select a Skill...")
        self.skill_picker.grid(row=1, column=2, padx=(4, 20), pady=4, sticky="ew")
        self.skill_picker.bind("<<ComboboxSelected>>", self._on_skill_combo_selected)

        # File menu bar
        self.menubar = ctk.CTkFrame(self, fg_color="transparent", height=35)
        self.menubar.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(2, 8))
        self.open_file_btn = ctk.CTkButton(self.menubar, text="Open File...", command=self.open_file, width=120, height=30, font=("Segoe UI", 12))
        self.open_file_btn.pack(side="left", padx=(4,4))

        # Status bar
        self.status_var = ctk.StringVar(value="Ready.")
        self.status = ctk.CTkLabel(self, textvariable=self.status_var, font=("Segoe UI", 11, "italic"), text_color="#95cfff")
        self.status.grid(row=3, column=0, columnspan=3, sticky="ew", padx=20, pady=(0,6))

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)

    def send_message(self, event=None):
        user_input = self.entry_var.get()
        if not user_input: return
        self.append_chat(f"You: {user_input}")
        self.entry_var.set("")
        self.status_var.set("Thinking...")
        Thread(target=self.handle_ai_response, args=(user_input,)).start()

    def handle_ai_response(self, user_input):
        try:
            # --- Normal agent/skills logic ---
            skills = self.skills
            skill_prompt = "You are an AI assistant. Here are available skills:\n"
            for s in skills.values():
                params = s["function"].__code__.co_varnames
                param_str = ", ".join(params)
                skill_prompt += f"- {s['name']}({param_str}): {s['description']}\n"
            skill_prompt += (
                "\nIf the user's request matches a skill, reply ONLY with the function call in Python"
                "If not, reply with: None\n"
                f"\nUser request: {user_input}\n"
            )
            ai_skill_call = call_ollama(skill_prompt).split("\n")[0].strip()

            if ai_skill_call and ai_skill_call != "None" and "(" in ai_skill_call:
                node = ast.parse(ai_skill_call, mode='eval').body
                skill_name = node.func.id
                params = {}
                for kw in getattr(node, 'keywords', []):
                    params[kw.arg] = ast.literal_eval(kw.value)
                if skill_name in skills:
                    result = skills[skill_name]["function"](**params)
                    log_action(skill_name, params)
                    self.append_chat(f"[Skill] {ai_skill_call}\n[Result] {result}")
                else:
                    ai_response = call_ollama(user_input)
                    self.append_chat(f"AI: {ai_response}")
            else:
                ai_response = call_ollama(user_input)
                self.append_chat(f"AI: {ai_response}")
        except Exception as e:
            self.append_chat(f"[Error] {e}")
        self.status_var.set("Ready.")

    def append_chat(self, text):
        self.chat_area.configure(state='normal')
        self.chat_area.insert("end", text + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.see("end")

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.append_chat(f"[Opened file: {filepath}]")
            if is_allowed(filepath):
                Thread(target=self.run_skill, args=('summarize', {'path': filepath})).start()
            else:
                self.append_chat("[Security] File access denied by policy.")

    def _on_skill_combo_selected(self, event=None):
        value = self.skill_picker.get()
        if value and value in self.skill_names:
            self.run_skill_gui(value)
            self.skill_picker.set("Type or select a Skill...")

    def run_skill_gui(self, skill_desc):
        skill = None
        skill_name = None
        for k, v in self.skills.items():
            if v["description"] == skill_desc:
                skill = v
                skill_name = k
                break
        if not skill:
            messagebox.showwarning("Skill not found", "No matching skill found.")
            return
        params = {}
        if 'path' in skill["function"].__code__.co_varnames:
            filepath = filedialog.askopenfilename()
            if not filepath:
                return
            if not is_allowed(filepath):
                messagebox.showwarning("Security", "Not allowed by policy.")
                return
            params['path'] = filepath
        Thread(target=self.run_skill, args=(skill_name, params)).start()

    def run_skill(self, skill_name, params):
        skill = self.skills[skill_name]
        self.status_var.set(f"Running: {skill['description']}")
        self.append_chat(f"[Skill] Running: {skill_name}({params})")
        try:
            result = skill["function"](**params)
            log_action(skill_name, params)
            self.append_chat(f"[Result] {result}")
        except Exception as e:
            self.append_chat(f"[Error] {e}")
        self.status_var.set("Ready.")

if __name__ == "__main__":
    import os
    if not os.path.exists("skills"):
        os.makedirs("skills")
    app = AssistantGUI()
    app.mainloop()

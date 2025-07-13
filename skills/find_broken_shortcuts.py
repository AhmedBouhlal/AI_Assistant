import os

def find_broken_shortcuts_simple(folder=None):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder to scan for broken shortcuts")
        if not folder:
            return "No folder selected."
    broken = []
    for dirpath, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".lnk"):
                shortcut_path = os.path.join(dirpath, file)
                # Just check if target file exists in same folder (basic check)
                target_guess = os.path.join(dirpath, os.path.splitext(file)[0])
                if not any(os.path.exists(target_guess + ext) for ext in (".exe", ".bat", ".lnk", ".py", ".docx", ".xlsx", "")):
                    broken.append(shortcut_path)
    return broken or "No broken shortcuts found (simple check)."

def register():
    return {
        "name": "find_broken_shortcuts_simple",
        "function": find_broken_shortcuts_simple,
        "description": "Find broken .lnk shortcuts in a folder (simple mode)",
        "security": "read"
    }

## 🧠 Modular AI Assistant

A smart, modular, GUI-based Python assistant built for automation, file management, and local AI interactions. Fully customizable and extensible via plug-and-play skills.

---

## ✨ Features

- 🧩 Modular skills system — drop-in Python files to add new abilities
- 📁 File system tools (search, disk usage, cleanup)
- 📊 System monitoring utilities
- 📦 Simple, pop-up GUI interface (no browser needed)
- 📜 Easy skill logging and auditing
- 🛠️ Works offline — no ChatGPT, DeepSeek, or external APIs required

---

## 🗂️ Folder Structure

.
├── assistant_main.py # Entry point for the GUI assistant

├── assistant_core.py # Loads and executes skills

├── ai_interface.py # Connects to local models like LLaMA (via Ollama)

├── assistant_config.py # Stores model/host configurations

├── skills/
│ ├── init.py
│ ├── file_search.py
│ ├── disk_usage.py
│ ├── your_custom_skills.py
│ └── ...

## 🛠️ How It Works

1. **Each skill** is a Python file in the `skills/` folder.
2. Each file must include a `register()` function returning:
   - Skill name
   - Function to call
   - Description
   - (Optional) Access level

```python
def register():
    return {
        "name": "file_search",
        "function": search_files,
        "description": "Searches for files on your system.",
        "security": "open"
    }
3. Skills are auto-loaded and callable from the GUI or CLI.

##🚀 Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt

2. Run the assistant:

```bash
python main_gui.py

##🧠 How to Add a New Skill

1. Create a new Python file inside skills/, e.g. hello.py
2. Write your function and register it:

```python
def hello_world():
    return "Hello, user!"

def register():
    return {
        "name": "hello",
        "function": hello_world,
        "description": "Says hello.",
        "security": "open"
    }
3. It will automatically load on next run.

.

##🛡️ Security

You can tag any skill as "open" or "restricted" to control access.

##🤖 Model Integration

Uses a local Ollama instance running a model like LLaMA 3. You can configure it via:

assistant_config.py
```python
OLLAMA_MODEL = "llama3"
OLLAMA_HOST = "http://localhost:11434/api/generate"

##📁 Logs

All skill calls are logged via log_action(skill_name, data) in assistant_core.py.

##📌 Notes

The assistant runs fully offline.
You are free to add or remove any skills in skills/

##🧠 License

MIT — free to use, modify, and redistribute.

##🙌 Credits

Built by [Ahmed BOUHLAL] for productivity, automation, and AI experimentation.

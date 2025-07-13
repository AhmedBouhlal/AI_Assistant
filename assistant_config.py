# assistant_config.py

ALLOWED_FOLDERS = [
    r"C:\Users",           # All users (edit to restrict)
    r"D:\Work"
]
FORBIDDEN_FOLDERS = [
    r"C:\Windows",
    r"C:\Program Files"
]
CONFIRM_ACTIONS = ["delete", "move", "run_script"]
LOG_FILE = "assistant.log"
OLLAMA_MODEL = "llama3"
OLLAMA_HOST = "http://localhost:11434/api/generate"

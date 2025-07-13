import subprocess
from tkinter.filedialog import askopenfilename

def open_with_notepad(path=None):
    if not path:
        path = askopenfilename(title="Pick file to open in Notepad")
        if not path:
            return "No file chosen."
    subprocess.Popen(['notepad.exe', path])
    return f"Opened {path} in Notepad."

def register():
    return {
        "name": "open_with_notepad",
        "function": open_with_notepad,
        "description": "Open any file in Notepad",
        "security": "read"
    }

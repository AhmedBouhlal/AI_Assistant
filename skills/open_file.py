import os
import subprocess
import sys

def open_file(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Choose a file to open")
        if not path:
            return "No file selected."
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform.startswith("darwin"):
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
    return f"Opened {path} with the default app."

def register():
    return {
        "name": "open_file",
        "function": open_file,
        "description": "Open any file with its default application",
        "security": "read"
    }

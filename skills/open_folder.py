import os
import subprocess
import sys

def open_folder(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askdirectory(title="Choose a folder to open in Explorer")
        if not path:
            return "No folder selected."
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform.startswith("darwin"):
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
    return f"Opened {path} in Explorer/Finder."

def register():
    return {
        "name": "open_folder",
        "function": open_folder,
        "description": "Open any folder instantly in Explorer/Finder",
        "security": "read"
    }

import os
import subprocess
import sys

def open_terminal_here(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askdirectory(title="Select folder for terminal")
        if not path:
            return "No folder selected."
    if sys.platform.startswith("win"):
        subprocess.Popen(['start', 'cmd', '/K', f'cd /d "{path}"'], shell=True)
    elif sys.platform.startswith("darwin"):
        subprocess.Popen(['open', '-a', 'Terminal', path])
    else:
        subprocess.Popen(['x-terminal-emulator', '--working-directory', path])
    return f"Opened terminal at {path}"

def register():
    return {
        "name": "open_terminal_here",
        "function": open_terminal_here,
        "description": "Open a terminal at any folder",
        "security": "read"
    }

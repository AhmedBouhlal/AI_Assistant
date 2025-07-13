import os

def copy_path(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Select file or folder to copy path")
        if not path:
            return "No file/folder selected."
    try:
        import pyperclip
        pyperclip.copy(path)
        return f"Copied path to clipboard: {path}"
    except Exception as e:
        return f"Install 'pyperclip': pip install pyperclip"

def register():
    return {
        "name": "copy_path",
        "function": copy_path,
        "description": "Copy file/folder path to clipboard",
        "security": "read"
    }

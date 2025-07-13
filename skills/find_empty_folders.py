import os

def find_empty_folders(folder=None):
    if folder is None:
        from tkinter import filedialog
        folder = filedialog.askdirectory(title="Select folder to scan")
        if not folder:
            return "No folder selected."
    empty = []
    for dirpath, dirnames, filenames in os.walk(folder):
        if not dirnames and not filenames:
            empty.append(dirpath)
    return empty or f"No empty folders found in {folder}"

def register():
    return {
        "name": "find_empty_folders",
        "function": find_empty_folders,
        "description": "Find empty folders in a directory (folder=...)",
        "security": "read"
    }

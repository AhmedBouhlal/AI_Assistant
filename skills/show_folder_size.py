import os

def show_folder_size(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askdirectory(title="Select folder to get total size")
        if not path:
            return "No folder selected."
    total = 0
    for dirpath, dirnames, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(dirpath, f))
            except:
                continue
    return f"Total size of {path}: {total//(1024*1024)} MB"

def register():
    return {
        "name": "show_folder_size",
        "function": show_folder_size,
        "description": "Show total size of any folder",
        "security": "read"
    }

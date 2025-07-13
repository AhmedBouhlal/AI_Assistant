import os

def count_files_by_type(folder=None):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder to count files")
        if not folder:
            return "No folder selected."
    types = {}
    for dirpath, _, files in os.walk(folder):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            types[ext] = types.get(ext, 0) + 1
    return "\n".join([f"{ext if ext else 'no ext'}: {count}" for ext, count in sorted(types.items(), key=lambda x: -x[1])])

def register():
    return {
        "name": "count_files_by_type",
        "function": count_files_by_type,
        "description": "Count number of files by type in a folder",
        "security": "read"
    }

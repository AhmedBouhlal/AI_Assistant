import os

def super_search_file(folder=None, name=""):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Choose folder to search")
        if not folder:
            return "No folder selected."
    if not name:
        from tkinter.simpledialog import askstring
        name = askstring("Filename", "Enter (part of) the filename to search for:")
        if not name:
            return "No name entered."
    matches = []
    for dirpath, _, files in os.walk(folder):
        for f in files:
            if name.lower() in f.lower():
                matches.append(os.path.join(dirpath, f))
    return matches or f"No files named '{name}' found in {folder}"

def register():
    return {
        "name": "super_search_file",
        "function": super_search_file,
        "description": "Find files by (partial) name in any folder (folder=..., name=...)",
        "security": "read"
    }

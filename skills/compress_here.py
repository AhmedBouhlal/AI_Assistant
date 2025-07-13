import os
import shutil

def compress_here(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Select file or folder to compress")
        if not path:
            return "No file/folder selected."
    base = os.path.splitext(path)[0]
    archive = base + ".zip"
    if os.path.isdir(path):
        shutil.make_archive(base, 'zip', path)
    else:
        shutil.make_archive(base, 'zip', os.path.dirname(path), os.path.basename(path))
    return f"Compressed to {archive}"

def register():
    return {
        "name": "compress_here",
        "function": compress_here,
        "description": "Compress file/folder to ZIP in-place",
        "security": "write"
    }

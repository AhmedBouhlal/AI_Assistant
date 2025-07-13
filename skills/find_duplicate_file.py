import os
import hashlib

def file_hash(path, blocksize=65536):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(blocksize), b''):
            h.update(block)
    return h.hexdigest()

def find_duplicate_files(folder=None):
    if folder is None:
        from tkinter import filedialog
        folder = filedialog.askdirectory(title="Select folder to search")
        if not folder:
            return "No folder selected."
    hashes = {}
    dups = []
    for dirpath, _, files in os.walk(folder):
        for file in files:
            try:
                full_path = os.path.join(dirpath, file)
                h = file_hash(full_path)
                if h in hashes:
                    dups.append((full_path, hashes[h]))
                else:
                    hashes[h] = full_path
            except Exception:
                continue
    if not dups:
        return "No duplicate files found."
    return "\n".join([f"{a} <==> {b}" for a,b in dups])

def register():
    return {
        "name": "find_duplicate_files",
        "function": find_duplicate_files,
        "description": "Find duplicate files by content in a folder",
        "security": "read"
    }

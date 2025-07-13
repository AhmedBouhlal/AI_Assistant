import os

def find_large_files(folder=None, size_mb=100):
    if folder is None:
        from tkinter import filedialog
        folder = filedialog.askdirectory(title="Select folder to search")
        if not folder:
            return "No folder selected."
    results = []
    for dirpath, _, files in os.walk(folder):
        for file in files:
            try:
                full_path = os.path.join(dirpath, file)
                if os.path.getsize(full_path) >= size_mb * 1024 * 1024:
                    results.append(f"{full_path} ({os.path.getsize(full_path)//(1024*1024)} MB)")
            except Exception:
                continue
    return results or f"No files > {size_mb}MB found in {folder}"

def register():
    return {
        "name": "find_large_files",
        "function": find_large_files,
        "description": "Find files larger than N MB in a folder (folder=..., size_mb=...)",
        "security": "read"
    }

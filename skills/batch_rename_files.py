import os

def batch_rename_files(folder=None, pattern="file_{num}"):
    if folder is None:
        from tkinter import filedialog
        folder = filedialog.askdirectory(title="Select folder to rename files")
        if not folder:
            return "No folder selected."
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    renamed = 0
    for i, filename in enumerate(files, 1):
        ext = os.path.splitext(filename)[1]
        new_name = pattern.format(num=i) + ext
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        try:
            os.rename(old_path, new_path)
            renamed += 1
        except Exception:
            continue
    return f"Renamed {renamed} files in {folder}."

def register():
    return {
        "name": "batch_rename_files",
        "function": batch_rename_files,
        "description": "Batch rename files in a folder (folder=..., pattern=...)",
        "security": "write"
    }

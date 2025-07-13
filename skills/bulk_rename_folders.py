import os

def bulk_rename_folders(folder=None, pattern="Folder_{num}"):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select parent folder to bulk-rename its folders")
        if not folder:
            return "No folder selected."
    subfolders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    renamed = 0
    for i, name in enumerate(subfolders, 1):
        new_name = pattern.format(num=i)
        src = os.path.join(folder, name)
        dst = os.path.join(folder, new_name)
        try:
            os.rename(src, dst)
            renamed += 1
        except Exception:
            continue
    return f"Renamed {renamed} folders in {folder}."

def register():
    return {
        "name": "bulk_rename_folders",
        "function": bulk_rename_folders,
        "description": "Bulk rename all folders in a directory (folder=..., pattern=...)",
        "security": "write"
    }

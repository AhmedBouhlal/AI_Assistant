import os
import shutil

def auto_sort_downloads(folder=None):
    from tkinter import filedialog
    if folder is None:
        folder = os.path.expanduser("~/Downloads")
    if not os.path.exists(folder):
        return "Downloads folder does not exist."
    moved = 0
    for f in os.listdir(folder):
        full = os.path.join(folder, f)
        if os.path.isfile(full):
            ext = os.path.splitext(f)[1].lower().replace(".", "")
            if not ext:
                ext = "other"
            target = os.path.join(folder, ext)
            os.makedirs(target, exist_ok=True)
            try:
                shutil.move(full, os.path.join(target, f))
                moved += 1
            except Exception:
                continue
    return f"Auto-sorted {moved} files in {folder} by extension."

def register():
    return {
        "name": "auto_sort_downloads",
        "function": auto_sort_downloads,
        "description": "Auto-sort files in Downloads by type",
        "security": "write"
    }

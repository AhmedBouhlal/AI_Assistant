import os
import time

def show_recent_files(folder=None, days=3):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Choose a folder to check for recent files")
        if not folder:
            return "No folder selected."
    now = time.time()
    cutoff = now - days*24*3600
    recents = []
    for dirpath, _, files in os.walk(folder):
        for f in files:
            full = os.path.join(dirpath, f)
            try:
                if os.path.getmtime(full) >= cutoff:
                    recents.append(f"{full} (modified {time.ctime(os.path.getmtime(full))})")
            except Exception:
                continue
    return recents or f"No files modified in the last {days} days."

def register():
    return {
        "name": "show_recent_files",
        "function": show_recent_files,
        "description": "Show files modified in the last N days (folder=..., days=...)",
        "security": "read"
    }

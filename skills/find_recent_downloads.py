import os
import time

def find_recent_downloads(folder=None, days=5):
    from tkinter import filedialog
    if folder is None:
        # Set your Downloads path here if not using askdirectory
        folder = os.path.expanduser("~/Downloads")
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
    return recents or f"No downloads in last {days} days."

def register():
    return {
        "name": "find_recent_downloads",
        "function": find_recent_downloads,
        "description": "Find recent downloads (last N days)",
        "security": "read"
    }

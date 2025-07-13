import os
import shutil

def fast_move_file(src=None, dst=None):
    from tkinter import filedialog
    if src is None:
        src = filedialog.askopenfilename(title="Select file to move")
        if not src:
            return "No source file selected."
    if dst is None:
        dst = filedialog.askdirectory(title="Select destination folder")
        if not dst:
            return "No destination folder."
    new_path = os.path.join(dst, os.path.basename(src))
    shutil.move(src, new_path)
    return f"Moved {src} to {new_path}"

def register():
    return {
        "name": "fast_move_file",
        "function": fast_move_file,
        "description": "Quickly move a file to a folder (src, dst)",
        "security": "write"
    }

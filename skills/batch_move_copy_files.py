import os
import shutil

def batch_move_copy_files(src_folder=None, dst_folder=None, file_ext=".txt", action="move"):
    from tkinter import filedialog
    if src_folder is None:
        src_folder = filedialog.askdirectory(title="Source folder")
        if not src_folder:
            return "No source folder."
    if dst_folder is None:
        dst_folder = filedialog.askdirectory(title="Destination folder")
        if not dst_folder:
            return "No destination folder."
    files = [f for f in os.listdir(src_folder) if f.endswith(file_ext)]
    count = 0
    for f in files:
        src = os.path.join(src_folder, f)
        dst = os.path.join(dst_folder, f)
        try:
            if action == "move":
                shutil.move(src, dst)
            else:
                shutil.copy2(src, dst)
            count += 1
        except Exception:
            continue
    return f"{action.capitalize()}d {count} {file_ext} files from {src_folder} to {dst_folder}"

def register():
    return {
        "name": "batch_move_copy_files",
        "function": batch_move_copy_files,
        "description": "Batch move/copy files by type (src_folder=..., dst_folder=..., file_ext=..., action=move/copy)",
        "security": "write"
    }

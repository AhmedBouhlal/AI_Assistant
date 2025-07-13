import os
import shutil
import tempfile

def delete_temp_files():
    temp_dirs = [tempfile.gettempdir()]
    deleted = 0
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            for item in os.listdir(temp_dir):
                path = os.path.join(temp_dir, item)
                try:
                    if os.path.isfile(path) or os.path.islink(path):
                        os.unlink(path)
                        deleted += 1
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                        deleted += 1
                except Exception:
                    continue
    return f"Deleted {deleted} temp files/folders from {tempfile.gettempdir()}"

def register():
    return {
        "name": "delete_temp_files",
        "function": delete_temp_files,
        "description": "Delete all files in the system temp folder",
        "security": "delete"
    }

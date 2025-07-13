import os
import time

def show_file_properties(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Select file to show properties")
        if not path:
            return "No file selected."
    stat = os.stat(path)
    info = f"""Path: {path}
Size: {stat.st_size // 1024} KB
Created: {time.ctime(stat.st_ctime)}
Modified: {time.ctime(stat.st_mtime)}"""
    return info

def register():
    return {
        "name": "show_file_properties",
        "function": show_file_properties,
        "description": "Show file properties (size, date, etc.)",
        "security": "read"
    }

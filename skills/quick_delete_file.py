import os

def quick_delete_file(path=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Select file to delete")
        if not path:
            return "No file selected."
    confirm = input(f"Are you sure you want to delete {path}? [y/N]: ").strip().lower()
    if confirm == "y":
        try:
            os.remove(path)
            return f"Deleted {path}."
        except Exception as e:
            return f"Error deleting file: {e}"
    else:
        return "Delete cancelled."

def register():
    return {
        "name": "quick_delete_file",
        "function": quick_delete_file,
        "description": "Delete a file instantly (with confirmation)",
        "security": "delete"
    }

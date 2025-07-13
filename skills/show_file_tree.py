import os

def show_file_tree(folder=None, max_depth=3, prefix=""):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder to display tree")
        if not folder:
            return "No folder selected."
    result = []
    def tree(path, depth):
        if depth > max_depth:
            return
        files = []
        try:
            files = os.listdir(path)
        except Exception:
            return
        for f in files:
            full = os.path.join(path, f)
            result.append(prefix + "  " * depth + ("📁 " if os.path.isdir(full) else "📄 ") + f)
            if os.path.isdir(full):
                tree(full, depth+1)
    tree(folder, 0)
    return "\n".join(result)

def register():
    return {
        "name": "show_file_tree",
        "function": show_file_tree,
        "description": "Show file/folder tree (folder=..., max_depth=...)",
        "security": "read"
    }

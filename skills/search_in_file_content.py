import os

def search_in_file_content(folder=None, text=""):
    from tkinter import filedialog, simpledialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder to search file content")
        if not folder:
            return "No folder selected."
    if not text:
        text = simpledialog.askstring("Content Search", "Enter the word or phrase to find in files:")
        if not text:
            return "No search text entered."
    matches = []
    for dirpath, _, files in os.walk(folder):
        for f in files:
            try:
                full = os.path.join(dirpath, f)
                with open(full, "r", encoding="utf-8", errors="ignore") as file:
                    if text.lower() in file.read().lower():
                        matches.append(full)
            except Exception:
                continue
    return matches or f"No files containing '{text}' found in {folder}"

def register():
    return {
        "name": "search_in_file_content",
        "function": search_in_file_content,
        "description": "Search for text in all files (folder=..., text=...)",
        "security": "read"
    }

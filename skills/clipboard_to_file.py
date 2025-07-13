import pyperclip
from tkinter.filedialog import asksaveasfilename

def clipboard_to_file():
    text = pyperclip.paste()
    if not text:
        return "Clipboard is empty!"
    file = asksaveasfilename(title="Save clipboard content to file", defaultextension=".txt")
    if not file:
        return "No file chosen."
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)
    return f"Saved clipboard contents to {file}"

def register():
    return {
        "name": "clipboard_to_file",
        "function": clipboard_to_file,
        "description": "Save clipboard text to a file",
        "security": "write"
    }

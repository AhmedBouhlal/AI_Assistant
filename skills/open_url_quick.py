import webbrowser
from tkinter.simpledialog import askstring

def open_url_quick(url=None):
    if not url:
        url = askstring("Open URL", "Enter a web URL:")
        if not url:
            return "No URL entered."
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opened {url} in browser."

def register():
    return {
        "name": "open_url_quick",
        "function": open_url_quick,
        "description": "Open any web link instantly in your browser",
        "security": "read"
    }

import webbrowser

def open_url_in_browser(url=None):
    from tkinter.simpledialog import askstring
    if not url:
        url = askstring("Open URL", "Enter the URL to open:")
        if not url:
            return "No URL entered."
    if not url.startswith("http"):
        url = "http://" + url
    webbrowser.open(url)
    return f"Opened {url} in browser."

def register():
    return {
        "name": "open_url_in_browser",
        "function": open_url_in_browser,
        "description": "Open a website in your browser (url=...)",
        "security": "read"
    }

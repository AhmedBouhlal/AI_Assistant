import webbrowser
import pyperclip

def search_clipboard_in_google():
    text = pyperclip.paste()
    if not text:
        return "Clipboard is empty!"
    url = "https://www.google.com/search?q=" + text.replace(" ", "+")
    webbrowser.open(url)
    return f"Searched clipboard content in Google: {text}"

def register():
    return {
        "name": "search_clipboard_in_google",
        "function": search_clipboard_in_google,
        "description": "Google search whatever's in your clipboard",
        "security": "read"
    }

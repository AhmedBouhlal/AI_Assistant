import webbrowser
from tkinter.simpledialog import askstring

def send_email_quick():
    to = askstring("Send Email", "To (email address):")
    subject = askstring("Send Email", "Subject:")
    body = askstring("Send Email", "Body:")
    if not to:
        return "No recipient entered."
    url = f"mailto:{to}?subject={subject or ''}&body={body or ''}"
    webbrowser.open(url)
    return f"Opened mailto link for {to}"

def register():
    return {
        "name": "send_email_quick",
        "function": send_email_quick,
        "description": "Open a new email in your default mail app",
        "security": "execute"
    }

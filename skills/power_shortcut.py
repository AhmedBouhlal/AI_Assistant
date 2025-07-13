import os
from tkinter.simpledialog import askstring

def power_shortcut():
    action = askstring("Power Shortcut", "Action (shutdown, restart, sleep, lock):")
    if not action:
        return "No action entered."
    action = action.lower()
    if action == "shutdown":
        os.system("shutdown /s /t 0")
        return "Shutting down..."
    elif action == "restart":
        os.system("shutdown /r /t 0")
        return "Restarting..."
    elif action == "sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "Sleeping..."
    elif action == "lock":
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locked."
    else:
        return "Unknown action."

def register():
    return {
        "name": "power_shortcut",
        "function": power_shortcut,
        "description": "Instant shutdown, restart, sleep, or lock",
        "security": "execute"
    }

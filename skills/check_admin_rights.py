import os
import ctypes

def check_admin_rights():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return "Running as Administrator!" if is_admin else "Not running as Administrator."

def register():
    return {
        "name": "check_admin_rights",
        "function": check_admin_rights,
        "description": "Check if running with admin rights",
        "security": "read"
    }

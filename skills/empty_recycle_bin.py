import os
def empty_recycle_bin():
    try:
        import winshell
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        return "Recycle Bin emptied."
    except Exception:
        return "Install 'winshell' (`pip install winshell`) and run as admin."

def register():
    return {
        "name": "empty_recycle_bin",
        "function": empty_recycle_bin,
        "description": "Empty the Windows Recycle Bin",
        "security": "delete"
    }

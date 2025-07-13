import os
import subprocess
import sys
import webbrowser

# Basic download links for popular apps (expand as needed)
DOWNLOAD_LINKS = {
    "chrome": "https://www.google.com/chrome/",
    "firefox": "https://www.mozilla.org/firefox/",
    "vscode": "https://code.visualstudio.com/",
    "notepad++": "https://notepad-plus-plus.org/downloads/",
    "discord": "https://discord.com/download",
    "word": "https://www.office.com/",
    "excel": "https://www.office.com/",
}

def search_and_run_app(app_name=None):
    from tkinter.simpledialog import askstring
    import shutil

    if not app_name:
        app_name = askstring("Run App", "App name (e.g., chrome, vscode, word, discord):")
        if not app_name:
            return "No app name entered."

    app_name_lower = app_name.lower()
    # Try Windows search paths (Start Menu, Program Files, Path)
    possible_names = [
        app_name_lower,
        app_name_lower + ".exe",
        app_name_lower.replace(" ", "") + ".exe",
        app_name_lower.replace(" ", ""),
    ]

    # 1. Try in PATH (fastest)
    exe_path = shutil.which(app_name_lower)
    if exe_path:
        subprocess.Popen([exe_path])
        return f"Launched {app_name} ({exe_path})"

    # 2. Try Start Menu shortcuts (.lnk)
    start_menu_dirs = [
        os.path.expandvars(r"%AppData%\Microsoft\Windows\Start Menu\Programs"),
        os.path.expandvars(r"%ProgramData%\Microsoft\Windows\Start Menu\Programs"),
    ]
    for menu_dir in start_menu_dirs:
        for root, _, files in os.walk(menu_dir):
            for file in files:
                if file.lower().startswith(app_name_lower) and file.lower().endswith(".lnk"):
                    shortcut_path = os.path.join(root, file)
                    os.startfile(shortcut_path)
                    return f"Launched shortcut: {shortcut_path}"

    # 3. Try common Program Files folders
    prog_dirs = [
        os.environ.get("ProgramFiles", r"C:\Program Files"),
        os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
        os.environ.get("LocalAppData", r"C:\Users\%USERNAME%\AppData\Local"),
    ]
    for prog_dir in prog_dirs:
        if not prog_dir: continue
        for root, dirs, files in os.walk(prog_dir):
            for file in files:
                if file.lower() in possible_names:
                    exe = os.path.join(root, file)
                    try:
                        subprocess.Popen([exe])
                        return f"Launched {exe}"
                    except Exception as e:
                        continue

    # 4. If not found, offer download link if known
    for name, url in DOWNLOAD_LINKS.items():
        if name in app_name_lower:
            webbrowser.open(url)
            return f"{app_name.title()} is not installed. Download page opened: {url}"

    return f"{app_name.title()} not found and no download link available. Try installing manually."

def register():
    return {
        "name": "universal_app_launcher",
        "function": search_and_run_app,
        "description": "Find and launch any installed app by name, or offer download if missing",
        "security": "execute"
    }
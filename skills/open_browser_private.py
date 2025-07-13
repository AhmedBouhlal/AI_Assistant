import subprocess
import shutil

def open_browser_private(browser="chrome"):
    if browser.lower() == "chrome":
        exe = shutil.which("chrome")
        if exe:
            subprocess.Popen([exe, "--incognito"])
            return "Opened Chrome in Incognito mode."
    elif browser.lower() == "firefox":
        exe = shutil.which("firefox")
        if exe:
            subprocess.Popen([exe, "-private-window"])
            return "Opened Firefox in Private mode."
    # Add more browsers if needed
    return "Browser not found. Please install Chrome or Firefox and add it to PATH."

def register():
    return {
        "name": "open_browser_private",
        "function": open_browser_private,
        "description": "Open Chrome or Firefox in private mode",
        "security": "execute"
    }

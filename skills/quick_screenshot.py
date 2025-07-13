import pyautogui
from tkinter.filedialog import asksaveasfilename

def quick_screenshot():
    img = pyautogui.screenshot()
    file = asksaveasfilename(title="Save screenshot", defaultextension=".png")
    if not file:
        return "No file chosen."
    img.save(file)
    return f"Screenshot saved to {file}"

def register():
    return {
        "name": "quick_screenshot",
        "function": quick_screenshot,
        "description": "Take a screenshot and save instantly",
        "security": "write"
    }

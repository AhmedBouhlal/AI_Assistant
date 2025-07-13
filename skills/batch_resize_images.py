from PIL import Image
import os

def batch_resize_images(folder=None, max_size=800):
    from tkinter import filedialog, simpledialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder with images to resize")
        if not folder:
            return "No folder selected."
    if not max_size:
        max_size = simpledialog.askinteger("Resize", "Max size (width or height)?", initialvalue=800)
        if not max_size:
            return "No size entered."
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    count = 0
    for f in images:
        path = os.path.join(folder, f)
        try:
            img = Image.open(path)
            img.thumbnail((max_size, max_size))
            img.save(path)
            count += 1
        except Exception:
            continue
    return f"Resized {count} images in {folder} to max {max_size}px."

def register():
    return {
        "name": "batch_resize_images",
        "function": batch_resize_images,
        "description": "Batch resize all images in a folder (folder=..., max_size=...)",
        "security": "write"
    }

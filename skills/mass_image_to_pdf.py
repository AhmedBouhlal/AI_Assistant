from PIL import Image
import os

def mass_image_to_pdf(folder=None, output="images.pdf"):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder with images")
        if not folder:
            return "No folder selected."
    images = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith((".jpg",".jpeg",".png"))]
    if not images:
        return "No images found."
    pil_images = [Image.open(f).convert("RGB") for f in images]
    pil_images[0].save(output, save_all=True, append_images=pil_images[1:])
    return f"Saved {output}"

def register():
    return {
        "name": "mass_image_to_pdf",
        "function": mass_image_to_pdf,
        "description": "Convert all images in a folder to a single PDF (folder=..., output=...)",
        "security": "write"
    }

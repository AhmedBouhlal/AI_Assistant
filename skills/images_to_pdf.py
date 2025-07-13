def images_to_pdf(folder=None, output="output.pdf"):
    from tkinter import filedialog
    from PIL import Image
    import os
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder with images")
        if not folder:
            return "No folder selected."
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not files:
        return "No images found."
    images = [Image.open(f).convert("RGB") for f in files]
    images[0].save(output, save_all=True, append_images=images[1:])
    return f"Saved {output}"

def register():
    return {
        "name": "images_to_pdf",
        "function": images_to_pdf,
        "description": "Convert images in a folder to a single PDF (folder=..., output=...)",
        "security": "write"
    }

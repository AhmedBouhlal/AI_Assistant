from tkinter import filedialog, Toplevel, Label
from PIL import Image, ImageTk

def preview_image(path=None):
    if path is None:
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if not path:
            return "No image selected."
    top = Toplevel()
    top.title(f"Preview: {path}")
    img = Image.open(path)
    img.thumbnail((600, 600))
    tk_img = ImageTk.PhotoImage(img)
    lbl = Label(top, image=tk_img)
    lbl.image = tk_img  # Keep reference!
    lbl.pack()
    return f"Previewing {path}"

def register():
    return {
        "name": "preview_image",
        "function": preview_image,
        "description": "Preview an image file in a popup",
        "security": "read"
    }

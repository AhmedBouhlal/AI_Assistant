import shutil
import os

def compress_folder(folder=None, output="archive.zip"):
    from tkinter import filedialog
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder to compress")
        if not folder:
            return "No folder selected."
    shutil.make_archive(output.replace(".zip", ""), 'zip', folder)
    return f"Compressed {folder} to {output}"

def uncompress_zip(path=None, out_folder=None):
    from tkinter import filedialog
    if path is None:
        path = filedialog.askopenfilename(title="Select ZIP file", filetypes=[("ZIP files", "*.zip")])
        if not path:
            return "No zip file selected."
    if out_folder is None:
        out_folder = filedialog.askdirectory(title="Select output folder")
        if not out_folder:
            return "No output folder."
    shutil.unpack_archive(path, out_folder)
    return f"Extracted {path} to {out_folder}"

def register():
    return {
        "name": "compress_folder",
        "function": compress_folder,
        "description": "Compress a folder to a ZIP file (folder=..., output=...)",
        "security": "write"
    }
# Add second skill in the same file:
def register_uncompress():
    return {
        "name": "uncompress_zip",
        "function": uncompress_zip,
        "description": "Uncompress a ZIP file to a folder (path=..., out_folder=...)",
        "security": "write"
    }

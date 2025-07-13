def merge_pdfs(folder=None, output="merged.pdf"):
    from tkinter import filedialog
    import os
    if folder is None:
        folder = filedialog.askdirectory(title="Select folder with PDFs to merge")
        if not folder:
            return "No folder selected."
    pdfs = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".pdf")]
    if not pdfs:
        return "No PDFs found in folder."
    try:
        from PyPDF2 import PdfMerger
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(output)
        merger.close()
        return f"Merged PDFs into {output}"
    except Exception as e:
        return f"Error: {e}\nInstall with 'pip install PyPDF2'"

def register():
    return {
        "name": "merge_pdfs",
        "function": merge_pdfs,
        "description": "Merge all PDFs in a folder (folder=..., output=...)",
        "security": "write"
    }

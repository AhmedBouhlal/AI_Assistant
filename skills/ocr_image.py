def ocr_image(path):
    try:
        import pytesseract
        from PIL import Image
        text = pytesseract.image_to_string(Image.open(path))
        return text or "No text found."
    except Exception as e:
        return f"OCR failed: {e}\nInstall with 'pip install pytesseract pillow' and install Tesseract OCR program."

def register():
    return {
        "name": "ocr_image",
        "function": ocr_image,
        "description": "Extract text from an image file using OCR (path=...)",
        "security": "read"
    }

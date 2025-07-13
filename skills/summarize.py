from ai_interface import call_ollama

def summarize(path):
    if path.lower().endswith(".pdf"):
        try:
            import PyPDF2
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        except Exception as e:
            return f"PDF read error: {e}"
    else:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read(3000)
    prompt = f"Summarize this file:\n{text[:1500]}"
    return call_ollama(prompt)

def register():
    return {
        "name": "summarize",
        "function": summarize,
        "description": "Summarize a text or PDF file (path=...)",
        "security": "read"
    }

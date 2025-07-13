def convert_csv_to_excel(path=None, output=None):
    from tkinter import filedialog
    import os
    if path is None:
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path:
            return "No file selected."
    if output is None:
        output = os.path.splitext(path)[0] + ".xlsx"
    try:
        import pandas as pd
        df = pd.read_csv(path)
        df.to_excel(output, index=False)
        return f"Converted {path} to {output}"
    except Exception as e:
        return f"Error: {e}\nInstall with 'pip install pandas openpyxl'"

def register():
    return {
        "name": "convert_csv_to_excel",
        "function": convert_csv_to_excel,
        "description": "Convert a CSV file to Excel format (path=..., output=...)",
        "security": "write"
    }

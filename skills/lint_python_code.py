def lint_python_code(path):
    try:
        import pyflakes.api
        import pyflakes.reporter
        import io
        buf = io.StringIO()
        reporter = pyflakes.reporter.Reporter(buf, buf)
        pyflakes.api.checkPath(path, reporter=reporter)
        result = buf.getvalue() or "No issues found."
        buf.close()
        return result
    except Exception as e:
        return f"Error: {e}\nInstall with 'pip install pyflakes'"

def register():
    return {
        "name": "lint_python_code",
        "function": lint_python_code,
        "description": "Lint/check a Python file for errors (path=...)",
        "security": "read"
    }

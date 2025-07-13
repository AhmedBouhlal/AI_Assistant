# assistant_core.py

import os, glob, importlib.util
from assistant_config import ALLOWED_FOLDERS, FORBIDDEN_FOLDERS, CONFIRM_ACTIONS, LOG_FILE
from rich.console import Console

console = Console()

def load_skills():
    skills = {}
    for file in glob.glob("skills/*.py"):
        name = os.path.splitext(os.path.basename(file))[0]
        spec = importlib.util.spec_from_file_location(name, file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "register"):
            skill = mod.register()
            skills[skill["name"]] = skill
    return skills

def is_allowed(path):
    abs_path = os.path.abspath(path)
    if any(abs_path.lower().startswith(f.lower()) for f in FORBIDDEN_FOLDERS):
        return False
    return any(abs_path.lower().startswith(f.lower()) for f in ALLOWED_FOLDERS)

def confirm(action, params):
    if action in CONFIRM_ACTIONS:
        answer = input(f"Are you sure you want to {action} {params}? [y/N]: ").strip().lower()
        return answer == "y"
    return True

def log_action(action, params):
    with open(LOG_FILE, "a") as f:
        f.write(f"{action}: {params}\n")

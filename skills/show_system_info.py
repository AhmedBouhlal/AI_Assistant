import psutil

def show_system_info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    info = f"CPU: {cpu}%\nRAM: {ram.percent}% ({ram.used//(1024**2)}MB/{ram.total//(1024**2)}MB)"
    # Optional: GPU info with GPUtil
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            info += "\n" + "\n".join([f"GPU: {gpu.name}, Load: {gpu.load*100:.1f}% Mem: {gpu.memoryUsed}/{gpu.memoryTotal}MB" for gpu in gpus])
    except Exception:
        pass
    return info

def register():
    return {
        "name": "show_system_info",
        "function": show_system_info,
        "description": "Show system CPU, RAM, and GPU usage",
        "security": "read"
    }

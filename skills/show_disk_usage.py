import psutil

def show_disk_usage():
    parts = psutil.disk_partitions()
    results = []
    for part in parts:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            results.append(f"{part.mountpoint}: {usage.percent}% used ({usage.used // (2**30)}GB/{usage.total // (2**30)}GB)")
        except PermissionError:
            continue
    return "\n".join(results)

def register():
    return {
        "name": "show_disk_usage",
        "function": show_disk_usage,
        "description": "Show usage for all disks",
        "security": "read"
    }

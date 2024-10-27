import os


def get_total_size(path: str):
    total_size = 0
    try:
        if os.path.isdir(path):
            for child in os.listdir(path):
                childpath = os.path.join(path, child)
                total_size += get_total_size(childpath)
        return total_size + os.path.getsize(path)
    except (PermissionError, FileNotFoundError, OSError):
        return total_size


if __name__ == "__main__":
    total_size = get_total_size("/home")
    print(f"Total size: {total_size/1024/1024:.2f} MB ({total_size} bytes)")

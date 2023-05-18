from pathlib import Path

path = Path(r"\Users\Admin\Desktop\my_folder\my_file.txt")
print(path.exists())
print(path.name)
print(path.parent.name)
print(path.is_file())


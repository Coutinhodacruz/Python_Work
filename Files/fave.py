from pathlib import Path

path = Path.cwd() / "new_directory" / "favour.txt"
path.touch()

hot = [
    [12, 33, 44, 55, 66, ],
    [66, 77, 99, 44, 32, ],
    [32, 11, 10, 22, 33, ]
]

with open(path, encoding="utf-8", mode="w") as file:
    for number in hot:
        file.write(f"{number[0]}")
        for num in number[1:]:
            file.write(f",{num}")
    file.write("\n")
    print(hot)

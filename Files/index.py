
from pathlib import Path

path = Path.cwd() / "new_directory" / "consensus.txt"
path.touch()

numbers = [
    [29, 39, 49, 58, 34, 56],
    [80, 34, 56, 32, 67, 89],
    [43, 65, 76, 34, 78, 54]

]
correction = []


def decode(string):
    lst = string.split(",")
    new_lst = []
    for l in lst:
        new_lst.append(int(l))
    print(new_lst)

    # correction.append([int(num) for num in lst])
    # print([int(num) for num in lst])


with open(path, encoding="utf-8", mode="r") as file:
    lines = file.readlines()
    for line in lines:
        decode(line)

print(correction == numbers)





# for number in numbers:
#     file.write(f"{number[0]}")
#     for num in number[1:]:
#         file.write(f",{num}")
#     file.write("\n")
#     print(file.readlines())


# path.touch()
#
# destination = Path.cwd() / "new_directory2" / "ridwan.txt"
# path.replace(destination)
#
# new_path = Path.cwd() / "new_directory2"
# shutil.rmtree(new_path)
#
#
# source = Path.cwd() / "new_directory" / "dir_2" / "unknown.txt"
# print(source.exists())
#
# destination = Path.cwd() / "new_directory1" / "unknown.txt"
# source.replace(destination)



# dir = [
#     Path.cwd() / "new_directory1",
#     Path.cwd() / "new_directory2",
#     Path.cwd() / "new_directory3",
#     Path.cwd() / "new_directory4",
# ]
#
#
# for path in dir:
#     path.mkdir(exist_ok=True)
#
# for dir in cwd.rglob("new_directory[1234]"):
#     print(dir)
#


# print(Path.cwd() / "new_directory1")


# path = Path.cwd() / "see_fifteen" / "elite.txt"
# # if not path.exists():
# #     path.mkdir(exist_ok=True)
# path1 = Path.cwd() / "new_directory" / "dir_1"
# path2 = path.cwd() / "new_directory" / "dir_2" / "unknown.txt"
# path1.mkdir(exist_ok=True, parents=True)
# path2.parent.mkdir()
# path2.touch()

# path.touch()
# print(path.is_dir())


# path = Path(r"C:\Users\Admin\Desktop\PROGAMMING")
# print(path.exists())
#
# path2 = Path.home()
# print(path.anchor)
# print(path.name)
# print(path.suffix)
# print(path.stem)
# print(path.parent.parent)
#
# print(list(path.parents))
# path3 = Path.cwd()
#
# print(path3.exists())

import os

f = open("demoFile2.txt", "a")
f.write("Now the file has more content! ")
f.close()

# open and read the file after the appending:
f = open("demoFile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())



if os.path.exists("demoFile2.txt"):
    os.remove("demoFile2.txt")
else:
    print("The file does not exist")
#
# dir = [
#     Path.cwd() / "new_directory1",
#     Path.cwd() / "new_directory2",
#     Path.cwd() / "new_directory3",
#     Path.cwd() / "new_directory4",
# ]
# print(dir)

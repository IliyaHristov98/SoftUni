import os

path = os.path.join("resources", "my_first_file.txt")

file = open(path, "w")

file.write("I just created my first file!")

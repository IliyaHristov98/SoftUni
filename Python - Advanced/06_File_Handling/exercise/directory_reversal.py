import os


def save_extensions(directory_name, first_level=False):
    for filename in os.listdir(directory_name):
        file_path = os.path.join(directory_name, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1]
            extensions[file_extension] = extensions.get(file_extension, []) + [filename]
        elif os.path.isdir(file_path) and not first_level:
            save_extensions(file_path, first_level=True)


user_directory = input("Enter a directory: ")
extensions = {}
result = []

try:
    save_extensions(user_directory)
except FileNotFoundError:
    print("Directory not found!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("exercise\\report.txt", "w") as report_file:
    report_file.write('\n'.join(result))

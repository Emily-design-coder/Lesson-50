import os

filename = "file.txt"

if not os.path.exists(filename):
    print("File exists. \n")

with open(filename, "w") as f:
    f.write("Hello! This is an introduction to file handling.\n")

with open(filename, "r") as f:
    content = f.read()
    words = content.split()

    print("\nWords in the file:")
    for word in words:
        print(word)

sample_file = "sample_doc"
if os.path.exists(sample_file):
    os.remove(sample_file)
    print(f"\n{sample_file} deleted.")
else:
    print(f"\n{sample_file} does not exist.")
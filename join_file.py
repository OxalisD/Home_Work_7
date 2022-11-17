files = dict.fromkeys(["1.txt", "2.txt", "3.txt"], [])
for file in files.keys():
    with open(f"files/{file}", encoding="utf-8") as read_file:
        text = read_file.readlines()
        files[file] = text

with open("files/join_files.txt", "w", encoding="utf-8") as write_file:
    for name, text in sorted(files.items(), key= lambda x: len(x[1])):
        write_file.write(f"{name}\n{len(text)}\n{''.join(text)}\n")





with open("syntax.md", "r") as file:
    contents = file.read()
    print(contents)

with open("syntax.md", "a") as coc:
    coc.write(contents)
    print("Done")
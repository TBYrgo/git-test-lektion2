from random import seed, randrange

seed(None)

files: list[str] = ['dog.txt', 'science.txt']

all_lines: list[str] = []
for filename in files:
    with open(filename, "r") as file:
        for line in file:
            all_lines.append(line)

selected: int = randrange(0, len(all_lines))
print(all_lines[selected])

with open("demo.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
import string
def count_punctuation(line):
    punctuation = set(string.punctuation)
    return sum(1 for char in line if char in punctuation)
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()
with open("output.txt", "w", encoding="utf-8") as outfile:
    for line in lines:
        punctuation_count = count_punctuation(line)
        outfile.write(f"{punctuation_count}\n")
print("Результат подсчета знаков препинания записан в файл output.txt")

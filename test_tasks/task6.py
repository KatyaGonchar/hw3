import os


def read_file(filename):
    if not os.path.exists(filename):
        print("Error: File not found.")
        return None

    with open(filename, "r") as file:
        return file.readlines()

def calculate_statistics(lines):
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)

    return total_lines, total_words, total_chars

def write_statistics(filename, total_lines, total_words, total_chars):
    with open(filename, "a") as file:
        file.write(f"\nTotal lines: {total_lines}\n")
        file.write(f"Total words: {total_words}\n")
        file.write(f"Total characters: {total_chars}\n")


filename = "task6.txt"
lines = read_file(filename)

if lines is not None:
    total_lines, total_words, total_chars = calculate_statistics(lines)

    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")

    write_statistics(filename, total_lines, total_words, total_chars)

import random

# returns a list of strings containing the lines of the file
def get_file_lines(filename):
    lines = open(filename, "r")
    lines_list = lines.readlines()
    return lines_list

# prints the lines of the poem in reverse.
def lines_printed_backwards(lines_list):
    number_list = range(len(lines_list))
    number_list = list(number_list)
    for num in reversed(number_list):
        print(f"{number_list[num]} {lines_list[num]}")

# prints the lines of the poem randomly
def lines_list_printed_random(lines_list):
    number_list = range(len(lines_list))
    number_list = list(number_list)
    for i in number_list:
        num = random.randrange(3)
        print(lines_list[num])

 # prints the lines of the poem by even lines first and then odd lines
def lines_list_printed_custom(lines_list):
    for i in range(len(lines_list)):
        if i % 2 == 0:
            print(i, lines_list[i])

    for i in range(len(lines_list)):
        if i % 2 == 1:
            print(i, lines_list[i])

yeezy_list = get_file_lines("poem.txt")
print("Backwards Ye")
print("-" * 30)
lines_printed_backwards(yeezy_list)
print("Random Ye")
print("-" * 30)
lines_list_printed_random(yeezy_list)
print("Custom Ye")
print("-" * 30)
lines_list_printed_custom(yeezy_list)

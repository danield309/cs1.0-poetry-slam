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

def lines_list_printed_random(lines_list):
    number_list = range(len(lines_list))
    number_list = list(number_list)
    for i in number_list:
        num = random.randrange(3)
        print(lines_list[num])
# Testing working functions
#yeezy_list = get_file_lines("poem.txt")
#lines_printed_backwards(yeezy_list)
#lines_list_printed_random(yeezy_list)

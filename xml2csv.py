import pandas
import sys


def find_start_quo_mark(string):
    return string.index('"')


def find_end_quo_mark(string):
    return string.rindex('"')


def find_start_angle_bracket(string):
    return string.index(">")


def find_end_angle_bracket(string):
    return string.rindex("<")


result = ""
with open("strings.xml") as f:
    lines = f.readlines()
    if lines is None:
        print("Wrong File!")
    else:
        for line in lines:
            key_start = find_start_quo_mark(line)
            key_end = find_end_quo_mark(line)
            value_start = find_start_angle_bracket(line)
            value_end = find_end_angle_bracket(line)
            # print(line[key_start + 1:key_end])
            # print(line[value_start + 1:value_end])
            result = result + '"' + line[key_start + 1:key_end] + '",' + '"' + line[value_start + 1:value_end] + '"' + '\n'
    print(result)
f.close()
with open("strings.csv", "w", encoding="utf-8") as f:
    f.write(result)
f.close()



#!usr/env/python

import sys


def camel2underline(name):
    name_arr = list(name)
    new_name_arr = []
    for name_ele in name_arr:
        if name_ele.isupper():
            new_name_arr.append("_")
            new_name_arr.append(name_ele.lower())
        else:
            new_name_arr.append(name_ele)
    new_name = ''.join(name_arr)
    return new_name


def underline2camel(name):
    name_arr = name.split('_')
    new_name_arr = []
    for name_ele in name_arr:
        name_sec = name_ele.capitalize()
        new_name_arr.append(name_sec)
    new_name = ''.join(new_name_arr)
    return new_name


def main():
    if len(sys.argv) < 2:
        print("Usage: %s variable_name")

    vari_name = sys.argv[1]
    if vari_name.islower():
        convert_name = underline2camel(vari_name)
    else:
        convert_name = camel2underline(vari_name)
    print(convert_name)


if __name__ == "main":
    main()

#!/usr/bin/env python


def array_evo(this_array, this_set, pos):
    x = this_array[pos] * 2 + 1
    y = this_array[pos] * 3 + 1
    this_set.add(x)
    this_set.add(y)
    fresh_arr = []
    for ele in this_set:
        fresh_arr.append(ele)
    return fresh_arr


def main():
    my_array = [1]
    my_set = {1}
    n = 5
    for i in range(0, n):
        my_array = array_evo(my_array, my_set, i)
    print(my_array[n-1])
    print(my_array)
    print(my_set)


if __name__ == '__main__':
    main()

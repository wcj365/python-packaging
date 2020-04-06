import math
from . import centrality


def minimum(a_list):
    mini = a_list[0]  # start with the first element

    for num in a_list:
        if num < mini:
            mini = num

    return mini


def maximum(a_list):
    maxi = a_list[0]  # start with the first element

    for num in a_list:
        if num > maxi:
            maxi = num

    return maxi


def variance(a_list):
    the_mean = centrality.mean(a_list)  # we call the mean function defined earlier - code reuse

    squared_diff = [(x - the_mean) ** 2 for x in a_list]  # This is handy one-liner list comprehension

    return centrality.mean(squared_diff)  # we call the mean function defined earlier, again - code reuse


def standard_deviation(a_list):
    the_var = variance(a_list)
    return math.sqrt(the_var)


def main():
    x = [1, 2, 3, 4]
    print(x)
    print("The minimum = ", minimum(x))
    print("The maximum = ", maximum(x))
    print("The variance = ", variance(x))
    print("The standard deviation = ", standard_deviation(x))


if __name__ == "__main__":
    main()

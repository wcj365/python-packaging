
def print_list(a_list):
    print("The List = [", end="")
    for i in a_list:
        print(i, end="")
        if i < len(a_list):
            print(", ", end="")
    print("]")


def median(a_list):
    n = len(a_list)
    a_list.sort()

    if n % 2 == 0:
        m1 = a_list[n // 2]
        m2 = a_list[n // 2 - 1]
        m = (m1 + m2) / 2
    else:
        m = a_list[n // 2]

    return m


def mean(a_list):
    total = 0

    for num in a_list:
        total += num

    return total / len(a_list)


def main():
    x = [1, 2, 3, 4]
    print_list(x)
    print("The Mean = ", mean(x))
    print("The Median = ", median(x))


if __name__ == "__main__":
    main()

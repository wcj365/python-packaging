from simple_stats import centrality
from simple_stats import dispersion

def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(x)
    print("hello world!")
    centrality.print_list(x)
    print("The mean is: ", centrality.mean(x))
    print("The minimum = ", dispersion.minimum(x))
    print("The maximum = ", dispersion.maximum(x))
    print("The variance = ", dispersion.variance(x))
    print("The standard deviation = ", dispersion.standard_deviation(x))


if __name__ == "__main__":
    main()

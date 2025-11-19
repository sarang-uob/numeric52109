###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package as sp

if __name__ == '__main__':
    # Test numbers
    a = 1
    b = 2

    # Direct sum
    c = a + b
    print(f"The sum of {a} and {b} is {c}")

    # Using package simple operations
    print(f"add: {a} + {b} = {sp.operations.add(a, b)}")
    print(f"subtract: {b} - {a} = {sp.operations.subtract(b, a)}")
    print(f"multiply: {a} * {b} = {sp.operations.multiply(a, b)}")
    print(f"divide: {b} / {a} = {sp.operations.divide(b, a)}")

    # Additional operations
    print(f"power: {a} ** {b} = {sp.operations.power(a, b)}")
    print(f"square_root of 16 = {sp.operations.square_root(16)}")
    print(f"factorial of 5 = {sp.operations.factorial(5)}")
    print(f"logarithm base 10 of 1000 = {sp.operations.logarithm(1000, 10)}")
    print(f"sine(pi/2) = {sp.operations.sine(sp.operations.power(3.141592653589793, 1)/2)}")
    print(f"cosine(0) = {sp.operations.cosine(0)}")
    print(f"tangent(pi/4) = {sp.operations.tangent(3.141592653589793/4)}")

    # Note: sp.operations.interface() is interactive and is not called here.

    # Test statistics functions
    data = [1,2,3,4,5,6,7,8,9,10]
    print('\nStatistics computed from data:', data)
    print(f"mean: {sp.statistics.mean(data)}")
    print(f"median: {sp.statistics.median(data)}")
    print(f"std_dev: {sp.statistics.std_dev(data)}")
    sp.statistics.pretty_print_stats(data)

    # Test plotting functions (only if matplotlib is available)
    # Use the package graphics module and the statistics plotting function
    if getattr(sp.statistics, 'plt', None):
        print('\nPlotting histogram via sp.graphics.plot_histogram (will show a window)')
        sp.graphics.plot_histogram(data)
        print('Plotting via sp.statistics.plot_histogram')
        sp.statistics.plot_histogram(data)
    else:
        print('\nMatplotlib not available — skipping plot tests.')
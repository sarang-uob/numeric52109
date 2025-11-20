###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import math
import simple_package as sp


def section(title):
    print('\n' + '=' * 10 + f' {title} ' + '=' * 10)


if __name__ == '__main__':
    # Basic numbers
    a = 1
    b = 2

    section('Basic Python')
    c = a + b
    print(f"Direct sum: {a} + {b} = {c}")

    section('Operations from simple_package.operations')
    print(f"add: {a} + {b} = {sp.operations.add(a, b)}")
    print(f"subtract: {b} - {a} = {sp.operations.subtract(b, a)}")
    print(f"multiply: {a} * {b} = {sp.operations.multiply(a, b)}")
    print(f"divide: {b} / {a} = {sp.operations.divide(b, a)}")

    # demonstrate exception handling (divide by zero)
    try:
        print('divide by zero test:', sp.operations.divide(1, 0))
    except Exception as e:
        print('Expected error dividing by zero:', type(e).__name__, e)

    print(f"power: {a} ** {b} = {sp.operations.power(a, b)}")
    print(f"square_root of 16 = {sp.operations.square_root(16)}")
    print(f"factorial of 5 = {sp.operations.factorial(5)}")

    # Factorial error demo
    try:
        print('factorial of -1:', sp.operations.factorial(-1))
    except Exception as e:
        print('Expected error for factorial(-1):', type(e).__name__, e)

    print(f"logarithm base 10 of 1000 = {sp.operations.logarithm(1000, 10)}")
    print(f"sine(pi/2) = {sp.operations.sine(math.pi/2)}")
    print(f"cosine(0) = {sp.operations.cosine(0)}")
    print(f"tangent(pi/4) = {sp.operations.tangent(math.pi/4)}")

    # Note: sp.operations.interface() is interactive and is not executed here.
    print('\nTo run the interactive calculator use: sp.operations.interface()')

    section('Statistics from simple_package.statistics')
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('mean:', sp.statistics.mean(data))
    print('median:', sp.statistics.median(data))
    print('std_dev:', sp.statistics.std_dev(data))
    sp.statistics.pretty_print_stats(data)

    section('Plotting (graphics & statistics)')
    # plotting requires matplotlib; only call if it's available
    if getattr(sp.statistics, 'plt', None):
        print('Showing histogram via sp.graphics.plot_histogram (window will appear)')
        sp.graphics.plot_histogram(data)

        print('Showing histogram via sp.statistics.plot_histogram')
        sp.statistics.plot_histogram(data)
    else:
        print('Matplotlib not available — skipping plots.')


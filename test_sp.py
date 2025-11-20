"""
Demonstration script for the `simple_package` package.

This script is intended to look like a user of the package would write
code: import the package, call the submodules and functions, and
display small, self-contained examples along with clear explanations.

How to run:
    python3 test_sp.py

Notes and dependencies:
 - `simple_package.statistics` uses NumPy; it will raise an ImportError
   at import-time if NumPy is not installed.
 - Plotting requires Matplotlib. The script checks for plotting
   availability and only attempts to show plots when Matplotlib is
   present.
 - `simple_package.operations.interface()` is an interactive REPL-style
   calculator; this demo does not run it, but explains how to use it.
"""

import math

#Import the package as sp
import simple_package as sp


if __name__ == '__main__':
    # Part 1: show standard Python vs using the package
    a = 1
    b = 2


    # 1) Addition — use the operations module's `add` function.
    #    This is equivalent to `a + b` but demonstrates using the package API.
    result = sp.operations.add(a, b)
    print('\n# sp.operations.add(a, b)')
    print(f'{a} + {b} =', result)

    # 2) Subtraction — show how order matters: subtract(b, a) returns b - a.
    result = sp.operations.subtract(b, a)
    print('\n# sp.operations.subtract(b, a)')
    print(f'{b} - {a} =', result)

    # 3) Multiplication
    result = sp.operations.multiply(a, b)
    print('\n# sp.operations.multiply(a, b)')
    print(f'{a} * {b} =', result)

    # 4) Division
    result = sp.operations.divide(b, a)
    print('\n# sp.operations.divide(b, a)')
    print(f'{b} / {a} =', result)

    # 5) Demonstrate an expected error: dividing by zero.
    #    We catch and print the exception to show how the API behaves.

    division = sp.operations.divide(1, 0)


    # 6) Power, square root and factorial — other utilities provided.
    print('\n# sp.operations.power(a, b)')
    print('power:', sp.operations.power(a, b))

    print('\n# sp.operations.square_root(16)')
    print('square_root(16) =', sp.operations.square_root(16))

    print('\n# sp.operations.factorial(5)')
    print('factorial(5) =', sp.operations.factorial(5))

    # 7) Factorial of a negative number should raise — demonstrate input validation.
    print('\n# Factorial of a negative number (expected error)')
    try:
        _ = sp.operations.factorial(-1)
    except Exception as e:
        print('Raised ->', type(e).__name__, e)

    # 8) Logarithm and trigonometry helpers
    print('\n# sp.operations.logarithm(1000, 10)')
    print('log10(1000) =', sp.operations.logarithm(1000, 10))

    print('\n# Trigonometric functions')
    print('sine(pi/2) =', sp.operations.sine(math.pi / 2))
    print('cosine(0) =', sp.operations.cosine(0))
    print('tangent(pi/4) =', sp.operations.tangent(math.pi / 4))

    #additionally invoke the interface function
    sp.operations.interface()
    print('\nNote: `sp.operations.interface()` is an interactive calculator loop')
    print('It is not executed in automated demos. Run it manually to try the REPL.')


    data_list = [1, 2, 2, 3, 4, 10]
    print('Statistics functions accept lists or NumPy arrays. Here we use a small list:')
    print('  data =', data_list)

    # Compute mean, median, and standard deviation directly and print results.
    # The statistics functions accept lists or NumPy arrays.
    print('\n# sp.statistics.mean(data)')
    print('mean =', sp.statistics.mean(data_list))

    print('\n# sp.statistics.median(data)')
    print('median =', sp.statistics.median(data_list))

    print('\n# sp.statistics.std_dev(data)')
    print('std_dev =', sp.statistics.std_dev(data_list))

    print('\nPretty-print: `sp.statistics.pretty_print_stats(data)` prints a user-friendly summary:')
    sp.statistics.pretty_print_stats(data_list)


    print('Two plotting helpers are available: `sp.graphics.plot_histogram` and')
    print('`sp.statistics.plot_histogram`. Both show a histogram and mark mean/median.')

    #visialisation using graphics module
    sp.graphics.plot_histogram(data_list)


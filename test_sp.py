###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    #Creating a separete variable for the sum
    c = a + b
    print(f"The sum of {a} and {b} is {c}")

    ## Now do the same for the function in sp

    #fix- changed the product to sum in the string. and change sp.add to sp.operations.add while also adding an import in __init__.py of the package
    print(f"The sum of {a} and {b} is {sp.operations.add(a,b)}")


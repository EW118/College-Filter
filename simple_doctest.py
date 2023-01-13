"""

Common doctest stuff for a fresh cs105 project.

Typically this file would be renamed via "git mv" to be the main test of the project.

>>> 6*7
42

>>> times(6, 7)
42

"""

# Logic tries to get the standard Haverford "logic" module, provides some parts if it fails
from Logic import *


def times(x: float, y: float) -> float:
    precondition(x == 6)
    assertion(isInteger(6) and not isInteger(12.3))
    assertion(isNumber(6) and isNumber(6.6) and not isNumber("6.66"))
    assertion(isString("6") and not isString(6.66))
    assertion(isBoolean(True) and not isBoolean(0))
    result = x * y
    loopInvariant(True)  # just be sure the function is available
    postcondition(result == x * y)
    return result


#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In most Haverford CS course, you won't need to modify the stuff below.                    #
#############################################################################################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all " + str(result[1]) + " tests"))
    else:
        print("Rats!")

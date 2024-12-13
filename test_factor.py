from combinatorices import Combinatorics
import doctest

# FILE: test_combinatorices.py


def test_factorial():
    """
    Test the factorial function from the Combinatorics class.

    >>> Combinatorics.factorial(0)
    1
    >>> Combinatorics.factorial(1)
    1
    >>> Combinatorics.factorial(5)
    120
    >>> Combinatorics.factorial(10)
    3628800
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
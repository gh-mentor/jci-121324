class Combinatorics:
    _factorial_cache = {}

    @staticmethod
    def factorial(n):
        """
        Calculate the factorial of a given number using memoization.

        Args:
            n (int): The number to calculate the factorial for.

        Returns:
            int: The factorial of the given number.

        Notes:
            This function uses a cache to store previously calculated factorials
            to improve performance for repeated calculations.
        """
        if n in Combinatorics._factorial_cache:
            return Combinatorics._factorial_cache[n]
        if n == 0 or n == 1:
            result = 1
        else:
            result = n * Combinatorics.factorial(n - 1)
        Combinatorics._factorial_cache[n] = result
        return result

    @staticmethod
    def permutations(n, k):
        return Combinatorics.factorial(n) // Combinatorics.factorial(n - k)

    @staticmethod
    def combinations(n, k):
        return Combinatorics.permutations(n, k) // Combinatorics.factorial(k)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def permutations(n, k):
    return factorial(n) // factorial(n - k)

def combinations(n, k):
    return permutations(n, k) // factorial(k)
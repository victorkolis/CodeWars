def divisible_count(x, y, k):
    X = (x - 1) // k
    Y = y // k

    return Y - X


print(divisible_count(0, 20, 1))

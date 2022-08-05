# https://www.codewars.com/kata/526233aefd4764272800036f/train/python

def matrix_addition(matrix_a, matrix_b):
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    b = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]
    result = [map(sum, zip(*t)) for t in zip(a, b)]
    return result


print(matrix_addition(1, 2))

# TODO: Finish kata

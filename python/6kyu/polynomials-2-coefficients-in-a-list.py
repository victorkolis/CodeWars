# Link: https://www.codewars.com/kata/5694b4f9a01ae685c400002f
# Description:
#
# You will be given a list with the coefficients of a polynomial. Look the following order in both:
#
# P(x) =       6x³ + 3x² + 5x -4
# coefficients =  [ 6,   3,    5, -4]

# TODO:
def calc_poly(poly_list, x):
    sentence_tail = f'with x = {x} the value is'
    add_up = 0
    exponents = []
    poly_list_len = len(poly_list)
    for index in range(poly_list_len):
        add_up = poly_list[~index] * pow(x, index)
        exponents += [index]
    return add_up


print(calc_poly([6, 3, 5, -4], 4))

# Link: https://www.codewars.com/kata/57f6ad55cca6e045d2000627

def square_or_square_root(arr):
    new_arr = []
    for number in arr:
        rooted_number = number ** .5
        if len(str(rooted_number).split(".")[1]) > 1:
            new_arr += [int(number ** 2)]
        else:
            new_arr += [int(rooted_number)]
    return new_arr


print(square_or_square_root([4, 2, 9, 81]))

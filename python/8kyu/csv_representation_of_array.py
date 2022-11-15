# Link: https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
# Description:
#
# Create a function that returns the CSV representation of a two-dimensional numeric array.
#
# Example:
#
# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]]
#
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'


def to_csv_text(array):
    new_array = '\n'.join([','.join([str(x) for x in sub_array]) for sub_array in array])
    return new_array


print(to_csv_text([[0, 1, 2, 3, 4], [10, 11, 12, 13, 14]]))

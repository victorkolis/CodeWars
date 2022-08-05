# Link: https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e

def sum_of_differences(arr: list) -> int:
    final_sum = 0

    if len(arr) <= 1:
        return final_sum

    arr.sort(reverse=True)

    try:
        for index, number in enumerate(arr):
            final_sum += arr[index] - arr[index + 1]
    except IndexError:
        return final_sum


print(sum_of_differences([1, 2, 10]))

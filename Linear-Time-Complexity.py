def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

numbers = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = linear_search(numbers, target)
print(result)

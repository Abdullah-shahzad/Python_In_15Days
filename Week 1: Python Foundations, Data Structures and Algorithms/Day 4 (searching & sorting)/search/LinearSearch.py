def linearSearch(array, n, key):
    for i in range(0, n):
        if array[i] == key:
            return i
    return -1


arr = [2, 4, 0, 1, 9]
key_value = 1
counter = len(arr)
result = linearSearch(arr, counter, key_value)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)

def binarySearch(array1, key, low, high):
    while low <= high:

        mid = (low + high)//2

        if array1[mid] == key:
            return mid

        elif array1[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [1, 3, 5, 7, 9, 10]
key_value = 7
lower = 0
higher = len(array)-1
result = binarySearch(array, key_value, lower, higher)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

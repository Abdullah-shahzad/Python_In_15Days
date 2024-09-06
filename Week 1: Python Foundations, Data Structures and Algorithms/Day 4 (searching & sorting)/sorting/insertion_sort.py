def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1


mylist1 = [1, 23, 3, 4, 5, 19, 6]
insertion_sort(mylist1)
print(mylist1)





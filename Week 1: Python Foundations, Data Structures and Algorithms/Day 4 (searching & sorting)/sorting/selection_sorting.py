def selection_sort(mylist, size):
    for i in range(size):
        min_value = i
        for j in range(i+1, size):
            if mylist[j] < mylist[min_value]:
                min_value = j

        mylist[min_value], mylist[i] = mylist[i], mylist[min_value]


mylist1 = [9, 23, 3, 4, 4, 4, 4, 4, 5, 19, 18, 1, 3, 6]
size1 = len(mylist1)
selection_sort(mylist1, size1)
print(mylist1)


def BubbleSort(mylist):
    for i in range(len(mylist)):

        swapped = False

        for j in range(len(mylist)-i-1):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp

                swapped = True

        if not swapped:
            break


mylist1 = [1, 23, 3, 4, 5, 19, 6]
BubbleSort(mylist1)
print(mylist1)


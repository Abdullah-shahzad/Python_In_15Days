def selection_sort(mylist, size_u):
    for i in range(size_u):
        min_value = i
        for j in range(i+1, size_u):
            if mylist[j] < mylist[min_value]:
                min_value = j
        mylist[min_value], mylist[i] = mylist[i], mylist[min_value]


def duplicate_remove(merged_list1, unique_list1):
    for i in merged_list1:
        if i not in unique_list1:
            unique_list1.append(i)


list1 = [1, 2, 3, 11, 12, 5]
list2 = [12, 11, 1, 3, 13, 7]
unique_list = []
merged_list = list1 + list2

print("Merged list :", merged_list)
size = len(merged_list)

duplicate_remove(merged_list, unique_list)
print("List after removing the duplicates :", unique_list)

size1 = len(unique_list)
selection_sort(unique_list, size1)
print("Sorted list: ",unique_list)

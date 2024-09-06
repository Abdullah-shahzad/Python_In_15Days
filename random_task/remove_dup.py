
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 11, 2, 1, 6]
c = a + b
print(c)
d = []
for i in c:
    if i not in d:
        d.append(i)

print(d)


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 11, 2, 1, 6]
c = a + b
d = list(set(c))
print(d)


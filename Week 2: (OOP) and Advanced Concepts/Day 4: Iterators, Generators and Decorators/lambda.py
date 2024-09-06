List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)
#################################################
l = [2, 4, 7, 3, 14, 19]

for i in l:
#result = (lambda x: print("true") if x % 2 != 0 else print("false"))(i)
    result = (lambda x: "true" if x%2 !=0 else "false")(i)
    print(result)



def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

chopList = chop(list1)
print(list1)
print(chopList)

mid = middle(list2)
print(list2)
print(mid)
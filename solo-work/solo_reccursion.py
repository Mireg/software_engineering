# sum of the list

# create a function that will recursively add values of elements in the list

# funkcja sum_list
#    is list len > 0?

def sumList(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sumList(list[1:])

list0 = []
list1 = [1, 1, 1, 1]

print(sumList(list0))
print(sumList(list1))
# list = [1,1,1]
# sum = 0
# sum += list[0]
# print(sum)
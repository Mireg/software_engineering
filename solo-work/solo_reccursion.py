# sum of the list

# create a function that will recursively add values of elements in the list

# funkcja sum_list(list)
#    is empty?
#       return 0
#    else
#       return list[0] + rest

# def sumList(list):
#     if len(list) == 0:
#         return 0
#     else:
#         return list[0] + sumList(list[1:])

list0 = []
list1 = [1, 1, 1, 1]

# print(sumList(list0))
# print(sumList(list1))

#create a function that will recursively find maximum value in a list

#funkcja find_max(list)
#   is empty?
#       return 0
#   else: 
#      if list[0] < list[1]
#         return find_max(list[1:])
#      else:
#          return find_max(list.pop(1)) 

def find_max(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    elif len(list) > 1:
        if list[0] <= list[1]:
            return find_max(list[1:])
        else:
            list.pop(1)
            return find_max(list)

list2 = [1, 2, 2, 5, 4, 3]
print(find_max(list2))
print(find_max(list0))
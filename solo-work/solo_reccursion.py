# sum of the list

# create a function that will recursively add values of elements in the list

# funkcja sum_list(list)
#    is empty?
#       return 0
#    else
#       return list[0] + rest

def sumList(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sumList(list[1:])

list0 = []
list1 = [1, 1, 1, 2]

print(sumList(list0))
print(sumList(list1))

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
print(find_max(list1))


#Factorial

#funkcja factorial(n)
#   if n == 0
#       return 1
#   else
#       f = n * factorial(n-1)
#       return f

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))


#Fibbonaci

#zwraca n-tą liczbę ciągu fibbonaciego (1, 1, 2, 3, 5, 8...)
#funkcja fibbonaci(n)
#   if n == 0
#       return 0
#   else if n == 1
#       return 1
#   else:
#       return fibbonaci(n-1) + fibbonaci(n-2)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)


print(f"{F(0)}, {F(1)}, {F(2)}, {F(3)}, {F(4)}, {F(5)}, ... , {F(12)}")

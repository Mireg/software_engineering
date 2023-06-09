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

#Sudoku 4x4

#separate function?
#check for empty cell = 0
#check every number 1-4 if can be placed
    #check if can be placed in row
    #check if can be placed in column
    #check if can be placed in 2x2 square

#iterate over every row, 
    #iterate over every column
        #check if empty
            #if empty check every number 1-4
                #put the first one that works
                    #solve new sudoku with inputed number
                    #if cannot be solved change it back to 0
                    #and check other numbers left in range

import numpy as np

sudoku = [[1,0,0,0],
          [0,0,0,4],
          [0,0,2,0],
          [0,3,0,0]]

def is_possible (matrix, row, col, n):
    #check row
    for i in range(0,4):
        if matrix[row][i] == n:
            return False
    
    #check column
    for i in range(0,4):
        if matrix[i][col] == n:
            return False

    #check 2x2 square
    row0 = (row // 2) * 2
    col0 = (col // 2) * 2
    for i in range(2):
        for j in range(2):
            if matrix[row0 + i][col0 + j] == n:
                return False
    
    return True

print(is_possible(sudoku, 0, 2, 3))

def solve_sudoku(matrix):
    #iterate rows
    for i in range(4):
        #iterate columns
        for j in range(4):
            #check empty
            if matrix[i][j] == 0:
                #input all values from range
                for n in range(1, 5):
                    #check if it works
                    if is_possible(matrix, i, j, n):
                        #input number
                        matrix[i][j] = n
                        #solve filled sudoku
                        solve_sudoku(matrix)
                        #backtrack if cannot be solved
                        matrix[i][j] = 0
                return None
    print(np.matrix(matrix))

solve_sudoku(sudoku)
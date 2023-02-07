"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

# Вариант №1, или ТЗ надо читать Внимательно!!!
"""
import random

def createListByHands(size, numberList):
    list = []
    for i in range(0, size):
        list.append(int(input(f"Введите элемент № {i} в список № {numberList}: ")))
    return list

def quickSort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q] 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quickSort(l_nums) + e_nums + quickSort(b_nums)

list1 = []
list2 = []
endList = []

sizeList1 = int(input("Введите количество элементов в списке № 1: "))
sizeList2 = int(input("Введите количество элементов в списке № 2: "))

list1 = createListByHands(sizeList1, 1)
list2 = createListByHands(sizeList2, 2)
endList = list1

for i in range(0, sizeList2):
    endList.append(list2[i]) 

endList = set(quickSort(endList))

print(*endList)

"""

# Вариант №2, или надо исправляться

import random

def createListByHands(size, numberList):
    list = []
    for i in range(0, size):
        list.append(int(input(f"Введите элемент № {i} в список № {numberList}: ")))
    return list

def quickSort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q] 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quickSort(l_nums) + e_nums + quickSort(b_nums)

list1 = []
list2 = []
endList = []

sizeList1 = int(input("Введите количество элементов в списке № 1: "))
sizeList2 = int(input("Введите количество элементов в списке № 2: "))

list1 = createListByHands(sizeList1, 1)
list2 = createListByHands(sizeList2, 2)

for i in range(0, sizeList1):
    for j in range(0, sizeList2):
        if list1[i] == list2[j]:
            endList.append(list2[j])

endList = set(quickSort(endList))

print(*endList)
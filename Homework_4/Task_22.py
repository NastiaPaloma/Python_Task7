# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int (input('Введите количество элментов первого множества: '))
list1 = list(map(int, input().split()))
list1.sort()
m = int (input('Введите количество элментов второго множества: '))
list2 = list(map(int, input().split()))
list2.sort()
unic = []
for i in range (n):
    for j in range (m):
        if list1[i] == list2[j] and list1[i] not in unic:
            unic.append(list1[i])
            print(list1[i], end=' ')
            

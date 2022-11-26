#** 5. Реализуйте алгоритм перемешивания списка.
#Без функции shuffle из модуля random.
#10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
N = int(input('Введите количество элементов в списке N = '))
list = []
for i in range(N):
    list.append(i)
print(list)
for i in range(N):
    import random
    a = random.randint(0, N/2)
    t = list[a]
    list[a] = list[-a]
    list[-a] = t
print(list)
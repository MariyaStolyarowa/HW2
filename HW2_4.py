#4. Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
#Enter the value of N: 5
#Position one: 1
#Position two: 2
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 20

#Enter the value of N: 4
#Position one: 20
#Position two: 22
#-> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
#-> There are no values for these indexes!
N = int(input('Введите значение N = '))
pos1 = int(input('Введите номер позиции 1-го элемента:'))
pos2 = int(input('Введите номер позиции 2-го элемента:'))
list = []
for i in range(2*N+1):
    if i < N:
        list.append(-N+i)
    elif i > N:
        list.append(i-N)
    else:
        list.append(0) 
print(list)
if ((pos1 or pos2) > 2*N+1) or (pos1 or pos2) <=0:
    print('Одyj или оба значения позиции элемента находятся вне диапазона!')
else:
    print(f"Произведение элементов в указанных позициях = {list[pos1-1]*list[pos2-1]}" )
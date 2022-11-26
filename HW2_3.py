#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#in
#6
#out
#[2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
#14.071
n = int(input('Введите длину списка n = '))
a = 1
list = []
sum = 0
for i in range(1, n+1):
    a = round(((1 + 1/i)**i), 3)
    list.append(a)
    sum = sum + list[i-1]
print(list)
print(sum)


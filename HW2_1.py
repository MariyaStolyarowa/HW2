#1. Напишите программу, которая принимает на вход
#вещественное число и показывает сумму его цифр.
#Без работы с методами строк.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27
a = float(input("Ввеите число: "))
b = a - round(a)
while b !=0:
    a *= 10
    b = a - round(a)
a = int(abs(a))
print(a)
c = 0
while a > 0:
    c = c + a % 10
    a = a//10
print(c)
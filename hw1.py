# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите число "))
sum = 0
while num != 0:
    x = num % 10
    sum += x
    num = num //10
print(sum)    
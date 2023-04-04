
# 01. Написать цикл для выведения на экран каждой буквы своего ФИО.

name = input("Введите ФИО: ")

for word in name.split():
    for letter in word:
        print(letter)



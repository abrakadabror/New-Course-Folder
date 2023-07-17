numbers = [0, 1, 2, 3, 4]
# doubled_numbers = []

# for number in numbers:
#     doubled_numbers.append(number * 2)
# print(doubled_numbers)


# chce dodac w mojej nowej liscie number razy 2 gdzie number jest gdzie liczba jest listą wszystkich liczb
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

doubled_numbers = [number * 3 for number in range(5)]
print(doubled_numbers)


friends_ages = [22, 31, 35, 37]
# chcemy stworzyc tego stringa dla kazedgo elementu z listy powyzej
age_string = [f'My friend is {age} years old.' for age in friends_ages]
print(age_string)


names = ['Rolf', 'Bob', 'Jen']
lower = [name.lower()for name in names]  # zamieniamy duze litery na male
print(lower)

names = ['Rolf', 'Bob', 'Jen']
upper = [name.upper()for name in names]  # tworzy duze litery z kazdego znaku
print(upper)

names = ['rolf', 'bob', 'jen']
# tworzy capital letter z pierwszej litery
title = [name.title() for name in names]
print(title)


friend = input('Enter your friend name: ')
friends = ['Rolf', 'Bob', ' Jen', 'Charlie', 'Anne']
friends_01 = [name.lower() for name in friends]

if friend.lower() in friends_01:  # iterujemy jesli friend jest w zbiorze friends to
    print(f"{friend.title()} is one of your friends")  # drukujemy jego imie
else:
    # drukujemy imie jesli nie pochodzi z listy friends
    print(f"{friend.upper()} I don't have such a friend")

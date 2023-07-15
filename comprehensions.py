# numbers = [0, 1, 2, 3, 4]
# doubled_numbers = []

# # for number in numbers:  # tworzymy nowa liste z liczbami pomnozonywmi przez 2
# #     doubled_numbers.append(number * 2)

# # mozna zastosowac zamias numbers range(5)
# doubled_numbers = [number * 2 for number in numbers]

# print(doubled_numbers)


friends_ages = [22, 31, 35, 37]
age_string = [f'My friend is {age} years old.' for age in friends_ages]
print(age_string)


names = ['Rolf', ' Bob', 'Jen']
# wypisujemy imioona w malych literach
lower = {name.lower() for name in names}
print(lower)

friend = input('Enter your friend name: ')
friends = ['Rolf', 'Bob', 'Jen', 'Anne']
friends_lower = [name.lower() for name in friends]
if friend.lower() in friends_lower:
    # titlle pozowala na to zeby wydrukowac zmienna z upper-case and the rest w ith lower-case
    print(f'{friend.title()} is one of your friends.')

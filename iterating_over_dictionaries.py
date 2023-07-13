friends_ages = {'Rolf': 25, 'Anne': 34, 'Kamil': 35} 

# print(friends_ages['Rolf']) #ze slownika wybiermay Rolfa i jego wiek

for name, age in friends_ages.items():
    print(f'{name} is {age} years old')
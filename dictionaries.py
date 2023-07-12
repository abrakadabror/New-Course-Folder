# friend_ages = {'Rolf': 24, 'Adam': 25, 'Anne': 29} #slownik 3 elementowy
# print(friend_ages,['Rolf'])

# friend_ages['Bob'] = 20 #mozna zawsze dodac elementy do slownika 
# friend_ages['Rolf'] = 29 #edytujemy wiek Rolfa

# print(friend_ages)

#tworzymy tuple ze slowinikiem dictionary w wewnatrz
# friends = ( 
#     {'name': 'Rolf Smith', 'age': 24},
#     {'name': 'Adam  Wool', 'age': 28},
#     {'name': 'Anne Pun', 'age': 25}
# )

# print(friends[0]['name']) #friends[0] - pobieramy pierwszy element slownika a pozniej name = Rolf Smith
# print(friends[1]['age']) #pobieramy drugi element ze slownika a pozniej wiek
# print(friends[2]['name']) #pobieramy drugi element ze slownika  a pozniej name


# friends = [('Rolf', 24), ('Adam', 25), ('Anne', 29)] #lista tuples 

# friend_ages = dict(friends) #zamieniamy tuple na slownik
# print(friend_ages)

players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])
print(players[0]['numbers'][0])
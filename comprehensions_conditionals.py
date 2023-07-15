# ages = [22, 35, 27, 21, 20]
# # wartosc age zostaje podana w nowej liscie odds jesli wyrazenie z if jest True
# odds = [age for age in ages if age % 2 == 1]
# print(odds)


friends = ['Rolf', 'rutch', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_lower = [f.lower() for f in friends]
# friends_lower = set([f.lower() for f in friends]) #sety ktorych nie uzyjemy do stworzenia listy kot oprzyszeld na party
# guests_lower = set([g.lower() for g in guests])
# print(friends_lower.intersection(guests_lower))
present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
]
print(present_friends)

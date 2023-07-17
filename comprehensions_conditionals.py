ages = [22, 35, 27, 21, 20]
# # tworzymy wartosc age ktora zostanei umieszczona w nowej liscie odds
# # doda wartosc age do listy odds jesli warunek po if jest prawodziwy True
odds = [age for age in ages if age % 2 == 1]
print(odds)
print("*********************************************", '\n')

friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

intersection = friends_lower.intersection(guests_lower)
result = ' ,'.join(intersection)
print(result.title())


friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(len(present_friends), present_friends)  # liczymy ilosc

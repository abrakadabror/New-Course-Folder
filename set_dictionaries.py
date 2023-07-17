friends = ['Rolf', 'rutch', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_lower = set([n.lower() for n in friends])
guests_lower = set([n.lower() for n in guests])

print(guests_lower.intersection(friends_lower))
print(friends_lower.intersection(guests_lower))

# funckcja intersection sluzy do znalezienia czesci wspolnej pomiedz dwoma zbiorami. W tym przypadku setami.

friends = ['Rolf', 'rutch', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in friends}

result = "  ".join(present_friends)
print(result.upper())
print(result.lower())
print(result.title())


friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

long_timers = {
    # jesli 'i' jest 0 to pobierze 1 element z  listy friends(Rolf) i jest powiazane z time_since_seen, ktorym jest "3"
    friends[i]: time_since_seen[i]

    # oznacza, ze tworzymy nowa zmienna [i] i jej watrosc bedzie  w zakresie od zera do dlugosci losty friends, która wynosi 4
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)


# zip function

friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]
long_timers = {
    # jesli 'i' jest 0 to pobierze 1 element z  listy friends(Rolf) i jest powiazane z time_since_seen, ktorym jest "3"
    friends[i]: time_since_seen[i]

    # oznacza, ze tworzymy nowa zmienna [i] i jej watrosc bedzie  w zakresie od zera do dlugosci losty friends, która wynosi 4
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)

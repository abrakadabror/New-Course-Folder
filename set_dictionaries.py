# friends = ['Rolf', 'rutch', 'charlie', 'Jen']
# guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

# friends_lower = {n.lower() for n in friends}
# guest_lower = {n.lower() for n in guests}

# present_friends = friends_lower.intersection(guest_lower)
# present_friends = {name.title() for name in present_friends}

# print(present_friends)


friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

dict(zip(friends, time_since_seen))
long_timers = {
    # jesli i jest rowne 0 wybiera z listy Rolfa dla friends
    friends[i]: time_since_seen[i]
    # jesli u dla time_Since_seen jest 0 rowniez wybiera pierwsza pozycje czyli 3 z drugiej listy
    # # petla for jest po to aby przeszlo nam przez wszystkie pozycje zgodnie z iloscia wartosci
    for i in range(len(friends))
    # otrzymamy tylko trzy wartosci wieksze od 5 Bob, Jen and Anne
    # if time_since_seen[i] > 5
    # w liscie friends
}
print(long_timers)


# to samo co wyzej tylko krocej z pomoca dict i zip
friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]
long_timers = dict(zip(friends, time_since_seen))
print(long_timers)

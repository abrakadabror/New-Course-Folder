# art_friends = {'Rolf', 'Kamil', 'Jen'}
# science_firends = {'Jen','Charlie'}

# art_but_not_scienc = art_friends.difference(science_firends) #ten wiersz przekaze nam info o tym kto nie jest zarowno art i science_friendsem
# science_firends_but_not_art = science_firends.difference(art_friends)

# print(art_but_not_scienc)
# print('\n')
# print(science_firends_but_not_art)

# print('\n')

# not_in_both = art_friends.symmetric_difference(science_firends) #nie sa w oby setach
# print(not_in_both)

# art_and_science = art_friends.intersection(science_firends) #jesli chcemy uzyskac czlonkow obu setow
# print(art_and_science)

# all_friends = art_friends.union(science_firends) #wszystkie elementy bez powatrzajacych sie z obu setow
# print(all_friends)



# set_one = {1, 2, 3, 4, 5}
# set_two = {1, 3, 5, 7, 9, 11}
# set_three = set_one.intersection(set_two)
# print(set_three)

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

name = input("please give us a name: ")
user_friends.add(name)
user_friends_01 = user_friends.intersection(nearby_people)
print(user_friends_01)
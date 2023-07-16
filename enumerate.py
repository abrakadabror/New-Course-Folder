friends = ['Rolf', 'John', 'Anna']

# index = 0

# for friend in friends:
#     print(friend)
#     print(friend)
#     index = index + 1

for index, friend in enumerate(friends):
    print(index)
    print(friend)

print(list(enumerate(friends)))  # tworzy liste tupli/krotek

print(list(zip([0, 1, 2], friends)))

friends = ['Rolf', 'John', 'Anna']

index = 0

for friend in friends:
    print(index)
    print(friend)
    index = index + 1

for index, friend in enumerate(friends, start=1):  # statrujemy od 1
    print(index)
    print(friend)

print(list(enumerate(friends)))  # tworzy liste tupli

print(list(zip([0, 1, 2], friends)))
print(dict(enumerate(friends)))  # zamienia tupe w klucze i wartosci slownikowe

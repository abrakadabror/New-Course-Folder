friends = ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen']
print(friends[2:4])  # zaczyna wymieniac od "Anna" i konczy na "Bob"
print(friends[1:])  # wydrukuje wszystkich bez pierwszej pozycji
print(friends[:4])  # wydrukuje wszystko bez ostatniej pozycji "Jen"
print(friends[0:0])  # nie wydrukuje niczego
# wydrukujemy wszystkie pozycje z listy friends jako nowa liste...
print(friends[:])
print(friends)

print(friends[-3:])  # zaczynamy liczyc od konca czyli do "Anna"

print(friends[-3:-1])  # wypisze element "Anna" do elementu "Bob"


# najwazniejsza informacja to ta, ze pierwszy number to starting point a drugi to numer koncowy

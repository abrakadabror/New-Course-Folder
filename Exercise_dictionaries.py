#You must define a list of two players, each with a name and another set of numbers.
#Then for each player, print out a nice string that contains their name and how many numbers they got right (as we've done before, you can intersect their numbers with the lottery_numbers  variable provided). You'll then need to calculate the length of the resulting set to get how many numbers they got right.
#This string doesn't have to have a particular format, it just must include both the name and how many numbers they got right.


lottery_numbers = {13, 21, 22, 5, 8} #numery loterii
players = [{
    'name': 'Kamil', #gracz numer 1
    'numbers': {1, 2, 3, 4, 5} #wybrane numery w slowniku nawiasy klamrowe{} nie w tupli()
        
    },
    {
    'name': 'Pamela', #gracz numer 2
    'numbers': {13, 24, 5, 9, 11} #wybrane numery w slowniku nawiasy klamrowe{} nie w tupli()
}]

name = players[0]['name'] #deklarujemy zawodnika numer 1(Kamil)i wybieramy jego imie
numbers = players[0]['numbers'].intersection(lottery_numbers)  #intersection wykorzystujemy do znalezienia wspolnych elementow pomiedzy dwoma zbiorami
print(f"Player {name} got {len(numbers)} numbers right") #drukujemy imie zawodnika, ilosc zgadnietych(guessed) numerow


name = players[1]['name'] #deklarujemy zawodnika numer 2(Pamela)i wybieramy jego imie
numbers = players[1]['numbers'].intersection(lottery_numbers)  #intersection wykorzystujemy do znalezienia wspolnych elementow pomiedzy dwoma zbiorami
print(f"Player {name} got {len(numbers)} numbers right")  #drukujemy imie zawodnika, ilosc zgadnietych(guessed) numerow




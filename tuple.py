# short_tuple = 'Rolf', 'Bob' #krotka krotka xD
# a_bit_clearer = ('Rolf', 'Bob')# krotka do latwiejszego oganiecia z nawiasami

# tuple_in_list = [('Rolf', 'Bob')] 

# not_a_tuple = 'rolf' #to nie krotka bo brakuje comma na koncu
# not_a_tuple = 'rolf', #dodanie przecinka na koncu zamienia stringa w tuple(krotke)

friends = ('Rolf', 'Bob', 'Anne') #nie mozna dodac appendem kolejnego elementu do krtoki(tupli)
friends = friends + ('Kamil',) #ale mozna dodac do siebie dwie tuple

print(friends)

#w listach mozna usuwac i dodawac elementy w tupli nie.
#tupla jest uzytwczna gdy chcesz zachowac vaules niezmienione 
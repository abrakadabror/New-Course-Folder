for list_of_numbers in range(1,101): #liczymy petla for od 1 do 100 
    if list_of_numbers % 3 == 0 and list_of_numbers % 5== 0: #dla kazdegko numeru sprawdzamy czy jest podzielne przez 3 i 5 jesli tak to drukuje FIZZBUZZ
        print('FizzBuzz')
    elif list_of_numbers % 3 == 0: #jesli jest podzielne jedynie przez 3 durkuje Fizz
        print('Fizz')
    elif list_of_numbers  % 5 == 0: #jesli jest podzielne jedynie przez 5 drukuje Buzz
        print('Buzz')
    else:
        print(list_of_numbers) #jesli nie spelnia powyzszych warunkow drukuje jedynie numer
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz"
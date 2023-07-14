for list_of_numbers in range(1,101):
    if list_of_numbers % 3 == 0 and list_of_numbers % 5== 0:
        print('FizzBuzz')
    elif list_of_numbers % 3 == 0:
        print('Fizz')
    elif list_of_numbers  % 5 == 0:
        print('Buzz')
    else:
        print(list_of_numbers)
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz"
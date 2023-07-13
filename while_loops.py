is_learning = True

while is_learning: #colon start of the "body"
    print("you're learning")
    user_input = input('Are you still learning ?')
    is_learning = user_input == 'yes' #porownujemy wynik do stringa 'yes', jesli sa takie same to True a jak nie to False

#petle while uzywamy wtedy gdy chcemy powtorzyc cos nieokresolna liczbe razy az uzytkownik powie STOP
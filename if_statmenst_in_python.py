# pozwala na podjemowanie decyzji w zaleznosci od spelnienia warunku logicznego prawda/falsz

# friend = 'Rolf'
# user_name = input('What is your name: ')

# if user_name == friend: #dwukropek jest wymagany w if. Zadziala tylko wtedy gdy warunek jest True
#     print("hello, friend!")
# else:
#     print('Hello, stranger!')

# name = input('enter your name now!')
# print(bool(name))

# if name:
#     print('Runs.')

friends = ['Rolf','Bob', "Anne"]
family = ['Jen','Charlie']

user_name = input('enter your name: ')

if user_name in friends: #in sprawdza czy wartosc zawarrta w username znajduje sie w zbiorze friends
    print('Hello, friend!')
elif user_name in family: #in sprawdza czy wartosc zawarta w user_name znajduje sie w zbiorze liscie(friends)
    print('Hello, family!')
else:
    print('i dont know you')
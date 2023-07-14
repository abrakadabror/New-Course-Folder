for n in range(2, 10): 
    for x in range(2, n): #jesli numer jest "prime" to ta petla for nigdy sie nie przerwie
        if n % x == 0:
            print(f'equals{x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number.')
for n in range(2, 10):
    for x in range(2, n):  # jesli numer liczba pierwsza ta petla nigdy sie nie zatrzyma
        if n % x == 0:
            print(f"{n} equals {x} + {n//x}")
            break
    else:
        print(f"{n} is a prime number.")

def is_pair(number):
    if(number % 2 == 0):
        print("Ce nombre est pair")
    elif(number % 3 == 0):
        print("Ce nombre est impair, mais est multiple de 3")
    else:
        print("Ce nombre n’est ni pair ni multiple de 3")

is_pair(9)
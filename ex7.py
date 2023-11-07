a = float(input("Donner a: "))
op = input("Saisir l'operation (+,-,*,/): ")
b = float(input("Donner b: "))
result = 0
if(op == '+'):
    result = a+b
elif(op == '-'):
    result = a-b
elif(op == '*'):
    result = a*b
elif(op == '/'):
    result = a/b

print(f"{a} {op} {b} = {result}")
r1 = float(input("Digite o primeiro lado: "))
r2 = float(input("Digite o segundo lado: "))
r3 = float(input("Digite o terceiro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo!")
zaklad = float(input("Zadaj zaklad: "))
mocnina = float(input("Zadaj cislo, ktore mam priratat k x v exponente: "))
absolute = bool(int(input("Absolutna hodnota na exponente? 0 / 1: ")))
nasobok = float(input("Zadaj cislo, ktorym mam vynasobit zaklad umocneny na exponent: "))
bonus = float(input("zadaj cislo, ktore mam pripocitat k vysledku: "))

if absolute:
    for i in range(-5, 6):
        print(nasobok, "*", zaklad, "^", "|", i, "+", mocnina, "|", "+", bonus, "=",
              ((zaklad ** abs(i + mocnina)) * nasobok)
              + bonus)
else:
    for i in range(-5, 6):
        print(nasobok, "*", zaklad, "^", "(", i, "+", mocnina, ")", "+", bonus, "=",
              ((zaklad ** (i + mocnina)) * nasobok)
              + bonus)

def pad(d):
    if 10 > d > -1:
        return '0' + str(d)
    elif d > -1:
        return "+"+str(d)
    else:
        return str(d)


x, y = 59, 19

for i in range(int(y/2), 0-int(y/2), -1):
    for k in range(0-int(x/2/3), int(x/2/3)):
        if k is 0:
            print(pad(i), end=" ")
        elif i is 0:
            print(pad(k), end=" ")
        else:
            if absolute:
                if i - 1 <= int(((zaklad ** abs(k + mocnina)) * nasobok) + bonus) < i + 1:
                    if int(((zaklad ** abs(k + mocnina)) * nasobok) + bonus) == i:
                        print(" x ", end="")
                    else:
                        print(" . ", end="")
                else:
                    print("    ", end="")
            else:
                if i - 1 <= int(((zaklad ** (k + mocnina)) * nasobok) + bonus) < i + 1:
                    if int(((zaklad ** (k + mocnina)) * nasobok) + bonus) == i:
                        print(" x ", end="")
                    else:
                        print(" . ", end="")
                else:
                    print("   ", end="")
    print()
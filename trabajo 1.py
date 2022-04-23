saldo = 10000
print("\t .:MENU:. ")
print("1.ingresar dinero en la cuenta")
print("2.retirar")
print("3 Ver Saldo")
print("4 Salir")
opcion = int(input("Digite una opción en el menu:"))

print()

if opcion==1:
    extra = float(input("cuánto dinero desea ingresar ->"))
    saldo= saldo + extra
    print(f"Dinero en la cuenta:{saldo}")
elif opcion==2:
    retirar = float(input("cuanto dinero desea retirar -> "))
    if retirar>saldo:
        print("no tienes esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta:{saldo} ")
elif opcion==3:
     print(f"Dinero en la cuenta:{ saldo }")
elif opcion==4:
    print(" Gracias por utilizar su cajero automático ")
else:
    print(" Error, se equivoco de opción de menú")




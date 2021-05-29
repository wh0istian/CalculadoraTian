n1 = float(input("Pon tú primer número pa: ") )
n2 = float(input("Pon el segundo número pa: ") )

opcion = 0
while True:
    print("""
      ¿Qué quieres hacer mi bro? 😼
    Calculadora la presión por tian 🚬

    1) Sumar los dos números ➕
    2) Restar los dos números ➖
    3) Multiplicar los dos números ✖️
    4) Cambiar los números elegidos 🔁
    5) Mandar a mimir la calculadora 💤
    """)
    opcion = int(input("Elige vro 😵💨: ") )

    if opcion == 1:
        print(" ")
        print("TU RESPUESTA PA: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("TU RESPUESTA PA: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("TU RESPUESTA PA: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        n1 = float(input("Pon tú primer número pa 😸: ") )
        n2 = float(input("Pon el segundo número rey 😸: ") )
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta deah 🙁")
        

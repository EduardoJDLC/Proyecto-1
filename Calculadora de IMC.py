#Calculadora de IMC
#Se le pregunta al usuario cuantas personas van a dar sus datos en la calculadora de IMC.
Nopersonas = int(input("Número de personas: "))
#Se verifica que el número de personas sea mayor a 0, de lo contrario no se pedira nada.
while Nopersonas > 0:
    #Se le pide el Nombre con un input y se guarda.
    Nombre = (input("Introduzca su nombre por favor: "))
    #Se le pide el Apellido Paterno con un input y se guarda.
    ApellPa = (input("Introduzca su apellido paterno por favor: "))
    #Se le pide el Apellido Materno con un input y se guarda.
    ApellMa = (input("Introduzca su apellido materno por favor: "))
    #Se le pide la edad en entero y se ocupa la variable int().
    edad = int(input("Introduzca su edad en años por favor: "))
    #Se le pide el peso en float() o de variable de punto flotante.
    peso = float(input("Introduzca su peso en kg por favor: "))
    #De la misma forma se le pone la altura en punto flotante para poder ingresar correctamente el dato de la altura.
    alt = float(input("Introduzca su altura en metros porfavor: "))
    #Ocupe un renombre de variable pero resulta ser lo mismo de altura.
    al = alt
    #Se procede al calculo de el IMC de la persona en turno.
    IMC = peso / al**2
    #Lo que se hace aqui es que si la edad es mayor o menor da diferente impresión.
    if(edad < 18):
            print("Usted es menor de edad")
    else:
            print("Usted es mayor de edad")
            #Aqui se hace la impresión del resultado del IMC en formato str().
            print("IMC: " + str(IMC))
    #Dependiendo del resultado del IMC va a dar diferentes impresiones junto con el Nombre, Apellido Paterno, Apellido Materno y la edad.        
    if IMC >= 0 and IMC <= 18.50:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tienes un peso bajo. ")
    elif IMC >= 18.51 and IMC <= 24.99:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tiene un peso normal. ")
    elif IMC >= 25.00 and IMC <= 29.99:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tiene sobrepeso.")
    elif IMC >= 30.00 and IMC <= 34.99:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tiene obesidad leve.")
    elif IMC >= 35.00 and IMC <= 39.99:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tiene obesidad media. ")
    elif IMC >= 40.00:
        print("Usted " + str(Nombre) + " " + str(ApellPa) + " " + str(ApellMa) + " a tu edad de " + str(edad) + " años tiene obesidad mórbida.")

#Ocupamos esta funcíón debido a que cada vez que se termine de capturar los datos se van a tener que pedir nuevamente si ese es el caso.
#Lo ocupe para que el ciclo no fuera infinito.
    Nopersonas = Nopersonas - 1
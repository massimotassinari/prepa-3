

print('BIENVENIDO')
print('este programa te proveera un sistema de area de ciertas figuras geometricas:\n\n')
print('ingrese la opcion de la figura que esta intentando calcular el area:\n')
opcion = input('1.triangulo.\n2.cuadrado.\n3.circulo\n==>')

if opcion.isnumeric() and (int(opcion) < 4  and int(opcion) > 0):
    opcion = int(opcion)
    if opcion == 1:
        print('has decidido calcular el area de un triangulo')
        base = float(input('ingrese la base del triangulo'))
        altura = float(input('ingrese la altura del triangulo'))

        print('el area del triangulo es:\n')
        area = (base*altura)/2
        print('el area del triangulo es:', area)   
        print(f'el area del triangulo es:{(base*altura)/2}')

    elif opcion == 2:
        print('has decidido calcular el area de un cuadrado')
        side = float(input("ingrese un lado del cuadrado:\n=>"))
        print(f'el area del cuadrado es: {side**2}')

    else:
        print('has decidido calcular el area de un circulo')
        radio = float(input('ingresa el radio del circulo:\n=>'))
        area = radio**2*3.14
        print(f'el area del circulo es: {area}')



else:
    print('error. ingresa una opcion valida')
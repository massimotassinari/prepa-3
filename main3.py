

edad = input('ingrese su edad \n==>')

if edad.isnumeric():
    edad = int(edad)
    if edad<18:
        print('no pasas')
    
    elif edad >= 17 and edad <21:
        print('paga 60 tanto')
    
    elif edad >22:
        print('paga 70 dolares')
    else:
        print('paga 50 dolares especil')

else:
    print('no ingresaste una edad')

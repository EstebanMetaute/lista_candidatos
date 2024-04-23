import os
def fnt_limpiar_pantalla():
    os.system('cls')

candidatos = []
fnt_limpiar_pantalla()

def registrar_candidato():
    nombre_completo = input('Ingrese su nombre y apellido: ')
    identificacion = input('Ingrese su identificación: ')
    correo = input('Ingrese su correo electrónico: ')
    contacto = input('Ingrese su contacto: ')
    edad = int(input('Ingrese su edad: '))
    experiencia = int(input('Ingrese sus años de experiencia: '))
    profesion = input('Ingrese su profesión: ')
    ciudad = input('Ingrese su ciudad: ')
    sexo = input("Ingrese su sexo: ")
    fnt_limpiar_pantalla

    if edad >= 25 and edad <= 35 and (profesion == 'ingeniero sistemas' or profesion == 'ingeniero informático') and experiencia >= 2 and experiencia <= 4:
        candidato = {
            'nombre_completo': nombre_completo,
            'identificacion': identificacion,
            'correo': correo,
            'contacto': contacto,
            'edad': edad,
            'experiencia': experiencia,
            'profesion': profesion,
            'ciudad': ciudad,
            'sexo': sexo
        }
        candidatos.append(candidato)
        print('El candidato ha sido registrado exitosamente.')
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()
    else:
        print('El candidato no cumple con las condiciones.')
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()

def consultar_candidatos():
    if len(candidatos) > 0:
        for candidato in candidatos:
            print("\n---------- CANDIDATO ----------")
            print("Nombre completo: ", candidato["nombre_completo"])
            print("Identificación: ", candidato["identificacion"])
            print("Correo electrónico: ", candidato["correo"])
            print("Contacto: ", candidato["contacto"])
            print("Edad: ", candidato["edad"])
            print("Años de experiencia: ", candidato["experiencia"])
            print("Profesión: ", candidato["profesion"])
            print("Ciudad: ", candidato["ciudad"])
            print("Sexo: ", candidato["sexo"])
            enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()
    else:
        print("No hay candidatos registrados.")
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()

while True:
    print('\n<<<<<< MENU >>>>>>')
    print('1. Registrar candidato')
    print('2. Consultar candidatos')
    print('3. Salir')

    opcion = int(input("Ingrese su opción: "))
    fnt_limpiar_pantalla()

    if opcion == 1:
        registrar_candidato()
    elif opcion == 2:
        consultar_candidatos()
    elif opcion == 3:
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opcion valida.")
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()
    
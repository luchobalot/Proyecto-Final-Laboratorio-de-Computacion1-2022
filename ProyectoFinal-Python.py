# Alumnos: Gabino Mangas, Luciano Balot
# Proyecto: Aereolineas Python
# Contacto: gabinomangas@gmail.com, lnbalot02@gmail.com
# Fecha de entrega: 28/06/2022
# Profesor: Javier Balmaceda

from os import system

def error():
    system('cls')
    print('-------------------------------------------------------------')
    print('Los datos ingresados no son validos, porfavor intente denuevo')
    print('-------------------------------------------------------------')
    papelera = input('Presione ENTER para volver al menu')
    system("cls")

def informacion():
    while (True):
        system('cls')
        print('-------------------------------------------------------------')
        print('      aqui encontras la informacion para tu viaje            ')
        print('-------------------------------------------------------------')
        print(' ')
        print('1.- Presiona 1 para: Detalles de equipaje de mano.')
        print('2.- Presiona 2 para: Detalles de equipaje de bodega.')
        print('3.- Presiona 3 para: Articulos que no se pueden llevar.')
        print('4.- Presiona 4 para: Numeros disponibles para reclamos.')
        print('5.- Presiona 5 para volver al menu.')
        print(' ')
        infoOpc = int(input('\nIngrese que operacion desea realizar: '))
        
        if infoOpc == 1:
            system('cls')
            print('\nEquipaje de mano:')
            print('El equipaje de mano se podra transportar a bordo, sujeto a la disponibilidad de la cabina.')
            print('En caso de no poder ser transportado en la misma por temas operativos, se enviara a bodega sin cargo.')
            print('\nPeso maximo segun vuelo:')
            print('Cabotaje: 1 pieza de 8kg')
            print('Internacionales: 1 pieza de 10kg')
            print(' ')
            basura = input('Presione ENTER para volver ')

        elif infoOpc == 2:
            system('cls')
            print('Equipaje de bodega:')
            print('El equipaje registrado en bodega debe contener SOLO elementos de uso personal.')
            print('SOLAMENTE se considera como equipaje registrado: una valija, bolso o mochila.')
            print('\nPeso maximo segun vuelo:')
            print('Cabotaje: 1 pieza de 15kg')
            print('Internacionales: 1 pieza de 23kg')
            print(' ')
            basura = input('Presione ENTER para volver ')

        elif infoOpc == 3:
            system('cls')
            print('Articulos prohibidos')
            print(' ')
            Art_Prohi = ['Baterias', 'Armas y Munciones', 'Productos inflamables', 'Garrafa', 'Objetos punzantes', 'Objetos contundentes', 'Sustancias quimicas']
            z = 0
            while z < len(Art_Prohi):
                print()
                print(Art_Prohi[z])
                z+=1
            
            print(' ')
            print(' ')
            basura = input('Presione ENTER para volver ')

        elif infoOpc == 4:
            system('cls')
            print('Nuestros contactos:')
            print('\naereolineaspython@gmail.com')
            print('\nNumeros para reclamos:')
            print('Whatsapp: 2954789876')
            print('Telefono: 2954490232')
            print('\nNumeros para consultas:')
            print('Whatsapp: 2954624452')
            print('Telefono: 2954876867')
            print(' ')
            basura = input('Presione ENTER para volver')


        elif infoOpc == 5:
            break

        else:
            error()

def viaje_brasil():
    while (True):
        print('----------------------------------------------------------------------------')
        print('                      ¡Obten tu viaje a Brasil aqui!                        ')
        print('----------------------------------------------------------------------------')
        print(' ')
        
        print('1.- Presiona 1 para: Comprar pasaje en Primera Clase.')
        print('2.- Presiona 2 para: Comprar pasaje en Segunda Clase.')
        print('3.- Presiona 3 para: Volver.')
        CompraOpc = int(input('\nIngrese en que clase desea viajar: '))
         
        for x in range (0,16):
                  Asientos_brasil.append(False)
        
        if CompraOpc == 1: # Opcion para comprar en 1er Clase.
            print('\nLos asientos disponibles para viajar en Primera Clase son los siguientes: ')

            for x in range (0,5):
                if Asientos_brasil[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 0 and Posicion < 5:
                if Asientos_brasil[Posicion] == False:
                    Asientos_brasil[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_brasil.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_brasil.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $18000')
                    print('Efectivo: $15000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $18000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $15000, gracias por su compra!')
                    
                    print('\nSu numero de asiento es:', NroAsiento)
                    
            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 2: # Opcion para comprar en 2da Clase.
            print('Los asientos disponibles para viajar en Segunda Clase son los siguientes: ')

        
            for x in range (6,16):
                if Asientos_brasil[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 6 and Posicion <= 16:
                if Asientos_brasil[Posicion] == False:
                    Asientos_brasil[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_brasil.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_brasil.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $12000')
                    print('Efectivo: $10000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $12000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $10000, gracias por su compra!')

                    print('\nSu numero de asiento es:', NroAsiento)
                    
                else:
                    print('Error. El asiento elegido ya esta ocupado! Los asientos disponibles estan mostrados en pantalla.')
            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 3:
            break

        else:
            error()

        seguir = input('\nDesea volver a realizar la operacion? (SI-NO): ').lower().strip()

        if seguir != 'no':
            system("cls")
            continue

        else:
            break

    system("cls")

def viaje_eeuu():
    while (True):
        print('----------------------------------------------------------------------------')
        print('                 ¡Obten tu viaje a Estados Unidos aqui!                     ')
        print('----------------------------------------------------------------------------')
        print(' ')
        print('1.- Presiona 1 para: Comprar pasaje en Primera Clase.')
        print('2.- Presiona 2 para: Comprar pasaje en Segunda Clase.')
        print('3.- Presiona 3 para: Volver.')
        CompraOpc = int(input('\nIngrese en que clase desea viajar: '))
         
        for x in range (0,16):
                  Asientos_eeuu.append(False)
        
        if CompraOpc == 1: # Opcion para comprar en 1er Clase.
            print('\nLos asientos disponibles para viajar en Primera Clase son los siguientes: ')

            for x in range (0,5):
                if Asientos_eeuu[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 0 and Posicion < 5:
                if Asientos_eeuu[Posicion] == False:
                    Asientos_eeuu[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_eeuu.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_eeuu.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $20000')
                    print('Efectivo: $17000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $20000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $17000, gracias por su compra!')
                    
                    print('\nSu numero de asiento es:', NroAsiento)
                    
            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 2: # Opcion para comprar en 2da Clase.
            print('Los asientos disponibles para viajar en Segunda Clase son los siguientes: ')

        
            for x in range (6,16):
                if Asientos_eeuu[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 6 and Posicion <= 16:
                if Asientos_eeuu[Posicion] == False:
                    Asientos_eeuu[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_eeuu.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_eeuu.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $14000')
                    print('Efectivo: $12000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $14000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $12000, gracias por su compra!')

                    print('\nSu numero de asiento es:', NroAsiento)
                    
                else:
                    print('Error. El asiento elegido ya esta ocupado! Los asientos disponibles estan mostrados en pantalla.')

            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 3:
            break

        else:
            error()

        seguir = input('\nDesea volver a realizar la operacion? (SI-NO): ').lower().strip()

        if seguir != 'no':
            system("cls")
            continue

        else:
            break

def viaje_españa():
    while (True):
        print('----------------------------------------------------------------------------')
        print('                      ¡Obten tu viaje a España aqui!                        ')
        print('----------------------------------------------------------------------------')
        print(' ')
        print('1.- Presiona 1 para: Comprar pasaje en Primera Clase.')
        print('2.- Presiona 2 para: Comprar pasaje en Segunda Clase.')
        print('3.- Presiona 3 para: Volver.')
        CompraOpc = int(input('\nIngrese en que clase desea viajar: '))
         
        for x in range (0,16):
                  Asientos_espania.append(False)
        
        if CompraOpc == 1: # Opcion para comprar en 1er Clase.
            print('\nLos asientos disponibles para viajar en Primera Clase son los siguientes: ')

            for x in range (0,5):
                if Asientos_espania[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 0 and Posicion < 5:
                if Asientos_espania[Posicion] == False:
                    Asientos_espania[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_espania.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_espania.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $22000')
                    print('Efectivo: $19000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $22000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $19000, gracias por su compra!')
                    
                    print('\nSu numero de asiento es:', NroAsiento)
                    
            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 2: # Opcion para comprar en 2da Clase.
            print('Los asientos disponibles para viajar en Segunda Clase son los siguientes: ')

        
            for x in range (6,16):
                if Asientos_espania[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 6 and Posicion <= 16:
                if Asientos_espania[Posicion] == False:
                    Asientos_espania[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_espania.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_espania.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $16000')
                    print('Efectivo: $14000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $16000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $14000, gracias por su compra!')

                    print('\nSu numero de asiento es:', NroAsiento)
                    
                else:
                    print('Error. El asiento elegido ya esta ocupado! Los asientos disponibles estan mostrados en pantalla.')

            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')
       
        elif CompraOpc == 3:
            break

        else:
            error()

        seguir = input('\nDesea volver a realizar la operacion? (SI-NO): ').lower().strip()

        if seguir != 'no':
            system("cls")
            continue

        else:
            break

def viaje_china():
     while (True):
        print('----------------------------------------------------------------------------')
        print('                      ¡Obten tu viaje a China aqui!                         ')
        print('----------------------------------------------------------------------------')
        print(' ')
        print('1.- Presiona 1 para: Comprar pasaje en Primera Clase.')
        print('2.- Presiona 2 para: Comprar pasaje en Segunda Clase.')
        print('3.- Presiona 3 para: Volver.')
        CompraOpc = int(input('\nIngrese en que clase desea viajar: '))
         
        for x in range (0,16):
                  Asientos_china.append(False)
        
        if CompraOpc == 1: # Opcion para comprar en 1er Clase.
            print('\nLos asientos disponibles para viajar en Primera Clase son los siguientes: ')

            for x in range (0,5):
                if Asientos_china[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 0 and Posicion < 5:
                if Asientos_china[Posicion] == False:
                    Asientos_china[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_china.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_china.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $24000')
                    print('Efectivo: $21000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $24000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $21000, gracias por su compra!')
                    
                    print('\nSu numero de asiento es:', NroAsiento)
                    
            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')

        elif CompraOpc == 2: # Opcion para comprar en 2da Clase.
            print('Los asientos disponibles para viajar en Segunda Clase son los siguientes: ')

        
            for x in range (6,16):
                if Asientos_china[x] == False:
                    print(x+1)
            NroAsiento = int(input('Ingrese el asiento que desee comprar: '))
            Posicion = NroAsiento - 1

            if Posicion >= 6 and Posicion <= 16:
                if Asientos_china[Posicion] == False:
                    Asientos_china[Posicion] = True
                    system('cls')
                    print('Para finalizar la compra es necesario que ingrese los siguientes datos: ')
                    print()
                    NombrePasajero_china.append(input('Ingrese el Nombre y Apellido completo: '))
                    Documento_china.append(int(input('Ingrese el documento: ')))
                    print('\nQue forma de pago desea usar?')
                    print('Tarjeta: $18000')
                    print('Efectivo: $16000')
                    modo_pago = int(input('Ingrese 1 para pagar con tarjeta y 2 para pagar con efectivo: '))
                    system('cls')
                    if modo_pago == 1:
                        print('\nMonto pagado $18000, gracias por su compra!')
                    
                    else:
                        print('\nMonto pagado $16000, gracias por su compra!')

                    print('\nSu numero de asiento es:', NroAsiento)
                    
                else:
                    print('Error. El asiento elegido ya esta ocupado! Los asientos disponibles estan mostrados en pantalla.')

            else:
                print('\nEl asiento elegido no esta disponible')
                print(' ')
        
        elif CompraOpc == 3:
            break

        else:
            error()

        seguir = input('\nDesea volver a realizar la operacion? (SI-NO): ').lower().strip()

        if seguir != 'no':
            system("cls")
            continue

        else:
            break

def comprar_pasaje():
    while (True):
        system('cls')
        print('--------------------------------------------------------------------------------')
        print('    Bienvenido a la compra de pasajes de la aereolinia, seleccione una opcion   ')
        print('--------------------------------------------------------------------------------')
        print(' ')
        print('-Opcion 1 para el destino de Brasil')
        print('-Opcion 2 para el destino de Estados Unidos')
        print('-Opcion 3 para el destino de España')
        print('-Opcion 4 para el destino de China')
        print('-Opcion 5 para volver al menu')
        print(' ')
        opcion_pasaje = int(input('Ingrese su opcion: '))
        system("cls")
        
        if (opcion_pasaje == 1):
            viaje_brasil()
    
        elif (opcion_pasaje == 2):
            viaje_eeuu()
    
        elif (opcion_pasaje == 3):
            viaje_españa()
    
        elif (opcion_pasaje == 4):
            viaje_china()
    
        elif (opcion_pasaje == 5):
            break
        
        else:
            error()

def reservas():
    while (True):
        print('-------------------------------------------')
        print('|              MIS RESERVAS               |')
        print('-------------------------------------------')
        print('-Opcion 1 para ver mis reservas a Brasil')
        print('-Opcion 2 para ver mis reservas a Estados Unidos')
        print('-Opcion 3 para ver mis reservas a España')
        print('-Opcion 4 para ver mis reservas a China')
        print('-Opcion 5 para volver al menu')
        opcion_reserva = int(input('Ingrese su opcion: '))
    
        if (opcion_reserva == 1):
            print(' ')
            for m in range(len(NombrePasajero_brasil)):
                print('Nombre y apellido:', NombrePasajero_brasil[m], ', Documento:',Documento_brasil[m],)
                print(' ')
            salir = input('\nPresione ENTER para continuar ')
            system('cls')
            continue

        elif (opcion_reserva == 2):
            print(' ')
            for m in range(len(NombrePasajero_eeuu)):
                print('Nombre y apellido:', NombrePasajero_eeuu[m], ', Documento:',Documento_eeuu[m],)
                print(' ')       
            salir = input('\nPresione ENTER para continuar ')
            system('cls')
            continue
    
        elif (opcion_reserva == 3):
            print(' ')
            for m in range(len(NombrePasajero_espania)):
                print('Nombre y apellido:', NombrePasajero_espania[m], ', Documento:',Documento_espania[m],)
                print(' ')
            salir = input('\nPresione ENTER para continuar ')
            system('cls')
            continue
    
        elif (opcion_reserva == 4):
            print(' ')
            for m in range(len(NombrePasajero_china)):
                print('Nombre y apellido:', NombrePasajero_china[m], ', Documento:',Documento_china[m],)
                print(' ')
            salir = input('\nPresione ENTER para continuar ')
            system('cls')
            continue
    
        elif (opcion_reserva == 5):
            break
        
        else:
            error()

def cancelar_vuelo():
    while (True):
        print('-------------------------------------------')
        print('|           CANCELAR MI RESERVA           |')
        print('-------------------------------------------')
        print('-Opcion 1 para cancelar vuelo a Brasil')
        print('-Opcion 2 para cancelar vuelo a Estados Unidos')
        print('-Opcion 3 para cancelar vuelo a España')
        print('-Opcion 4 para cancelar vuelo a China')
        print('-Opcion 5 para volver al menu')
        cancelar = int(input('Opcion: '))

        if cancelar == 1:
            pasajero = input('\nIngrese el nombre y apellido del pasajero que desea cancelar la reserva: ').lower()
            for p in range(len(NombrePasajero_brasil)-1, -1, -1):
                if NombrePasajero_brasil[p] == pasajero:
                    NombrePasajero_brasil.pop(p)
                    Documento_brasil.pop(p)
                    print('\nReserva cancelada con exito!')

                else:
                    print('\nPasajero no encontrado')
                    papelera = input('Presiona ENTER para continuar')    
                    print(' ')

        elif cancelar == 2:
            pasajero = input('\nIngrese el nombre y apellido del pasajero que desea cancelar la reserva: ').lower()
            for p in range(len(NombrePasajero_eeuu)-1, -1, -1):
                if NombrePasajero_eeuu[p] == pasajero:
                    NombrePasajero_eeuu.pop(p)
                    Documento_eeuu.pop(p)
                    print('\nReserva cancelada con exito!')

                else:
                    print('\nPasajero no encontrado')
                    papelera = input('Presiona ENTER para continuar')    
                    print(' ')        

        elif cancelar == 3:
            pasajero = input('\nIngrese el nombre y apellido del pasajero que desea cancelar la reserva: ').lower()
            for p in range(len(NombrePasajero_espania)-1, -1, -1):
                if NombrePasajero_espania[p] == pasajero:
                    NombrePasajero_espania.pop(p)
                    Documento_espania.pop(p)
                    print('\nReserva cancelada con exito!')

                else:
                    print('\nPasajero no encontrado')
                    papelera = input('Presiona ENTER para continuar')    
                    print(' ')

        
        elif cancelar == 4:
            pasajero = input('\nIngrese el nombre y apellido del pasajero que desea cancelar la reserva: ').lower()
            for p in range(len(NombrePasajero_china)-1, -1, -1):
                if NombrePasajero_china[p] == pasajero:
                    NombrePasajero_china.pop(p)
                    Documento_china.pop(p)
                    print('\nReserva cancelada con exito!')

                else:
                    print('\nPasajero no encontrado')
                    papelera = input('Presiona ENTER para continuar')    
                    print(' ')        

        elif cancelar == 5:
            break
        
        else:
            error()
            continue

        print('\nDesea cancelar otro vuelo?')
        print(' ')
        opcion_cancelar = int(input('1: cancelar otro vuelo,  2: volver '))
        if opcion_cancelar == 1:
            continue

        else:
            break      

# Reservas Brasil
Asientos_brasil = []
NombrePasajero_brasil = []
Documento_brasil = []

# Reservas España
Asientos_espania = []
NombrePasajero_espania = []
Documento_espania = []

# Reservas EEUU
Asientos_eeuu = []
NombrePasajero_eeuu = []
Documento_eeuu = []

# Reservas China
Asientos_china = []
NombrePasajero_china = []
Documento_china = []

while (True):
    system("cls")
    print('////////////////////////////////////////////////////')
    print('         -BIENVENIDOS A AEREOLINEAS PYTHON          ')
    print('           -WELCOME TO PYTHON AIRLINES              ')
    print('////////////////////////////////////////////////////')
    print(' ')
    print('-Opcion 1 para comprar su pasaje')
    print('-Opcion 2 para ver mis reservas')
    print('-Opcion 3 para cancelar vuelo')
    print('-Opcion 4 para mas informacion')
    print('-Opcion 5 para finalizar el programa')
    print(' ')
    opcion_menu = int(input('Ingrese su opcion: '))
    system("cls")

    if (opcion_menu == 1):
        comprar_pasaje()
    
    elif (opcion_menu == 2):
        reservas()

    elif (opcion_menu == 3):
        cancelar_vuelo()

    elif (opcion_menu == 4):
        informacion()
    
    elif (opcion_menu == 5):
        break
    
    else:
        error()
       

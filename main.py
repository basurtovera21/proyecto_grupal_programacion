#Carlos
import os
import time
import config

#Configuración.
filas = 10
columnas = 10
letras_fila = ['A','B','C','D','E','F','G','H','I','J']
sala = []             #Matriz.
pelicula_actual = {}  #Película seleccionada.


def inicializar_matriz(): #Crear sala referencia.
    global sala
    for fila in range(filas):
        nueva_fila = []
        for columna in range(columnas):
            nueva_fila.append('[L]')
        sala.append(nueva_fila)
        

def mostrar_sala():
    #Información de película.
    titulo = pelicula_actual.get('titulo', 'sin selección') #.get(clave, valor por defecto)
    tarifa = pelicula_actual.get('tarifa', 0.00)
    
    print("S. CINE\n")
    print(f"Función : {titulo}") 
    print(f"Tarifa  : ${tarifa}\n")
    
    print("", end = "")
    for numero in range(1, columnas + 1):
        print(f"{numero :>3}", end = "")
        
    print("")


    for i in range(filas):
        print(f"{letras_fila[i]} ", end = "")

        for asiento in sala[i]:
            print(asiento, end = "")

        print()

    print("\n[L] = Libre.   [V] = Vendido.   [R] = Reservado.\n")

def limpiar_consola():
    if os.name == 'nt': # nt = Windows.
        os.system('cls') #Comando para limpiar la consola.
    else: # Mac, Linux...
        os.system('clear') #Comando para limpiar la consola.

def configurar_inicio():
    global pelicula_actual
    funciones = config.cargar_funciones()
    if not funciones:
        print("No existen funciones.")
        return
    
    while True:
        limpiar_consola()
        print("Funciones:\n")
        #funciones.json
        for i in range(len(funciones)):
            print(f"{i + 1}. {funciones[i]['titulo']} (${funciones[i]['tarifa']}).")
            
        print()
            
        try:
            seleccion = int(input("Número de selección: ")) - 1
            if seleccion >= 0 and seleccion < len(funciones):
                pelicula_actual = funciones[seleccion]
                break
            
            else:
                print("Número no válido.")
                time.sleep(1) #Pausar programa 1 segundo (time.sleep).
                
        except ValueError:
            print("Registro no válido.")
            time.sleep(1) #Pausar programa 1 segundo (time.sleep).

def iniciar_programa():
    inicializar_matriz()  #Crear la sala vacía.
    configurar_inicio()   #Película.
    
    while True:
        limpiar_consola()
        mostrar_sala()
        
        print("1. Vender entrada (L/V).")
        print("2. Reservar asiento (L/R).")
        print("3. Cancelar/liberar (L).")
        print("4. Buscar reserva (función recursiva).")
        print("5. Cierre administrativo (csv).")
        print("6. Guardar/salir (actualizar txt)\n")
        
        seleccion = str(input("Número de selección: "))
        
        match seleccion:
            #Las funciones = archivo.función_creada...
            case "1":
                print("ventas.vender_boleto(sala, pelicula_actual['precio'])") #Emily
                input("ENTER para volver.")
                
            case "2":
                print("reservas.reservar_asiento(sala)") #Ariela
                input("ENTER para volver.")
                
            case "3":
                print("reservas.cancelar_asiento(sala)") #Ariela
                input("ENTER para volver.")
            
            case "4":
                print("config.buscar_recursivo(sala)") #Persona 5
                input("ENTER para volver.")
            
            case "5":
                print("archivos.generar_reporte()") #Persona 4
                input("ENTER para volver.")
                
            case "6":
                print("sala.txt") #Persona 4
                print("Programa cerrado (actualización no terminada).")
                break
                
            case _:
                print("No válido.")

if __name__ == "__main__": #Ejecutar programa
    iniciar_programa()
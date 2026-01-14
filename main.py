#Persona 1
import os
import time
import config

#Configuración
filas = 10
columnas = 10
letras_fila = ['A','B','C','D','E','F','G','H','I','J']

sala = []             #Matriz
pelicula_actual = {}  #Película elegida


def inicializar_matriz(): #Crear sala.
    global sala
    for fila in range(filas):
        nueva_fila = []
        for columna in range(columnas):
            nueva_fila.append('[L]')
        sala.append(nueva_fila)

def mostrar_sala():
    #Información de la película.
    titulo = pelicula_actual.get('titulo', 'Sin Selección') #.get(clave, valor por defecto)
    precio = pelicula_actual.get('precio', 0.00)
    print(f"Función: {titulo} | Precio: ${precio}.")
    
    print("    ", end = "")
    for numero in range(1, columnas + 1):
        print(f"{numero : >3}", end = " ")
    print()

    # Línea separadora
    print("    " + "-" * (columnas * 4))

    for i in range(filas):
        print(letras_fila[i], "|", end = " ")

        for asiento in sala[i]:
            print(asiento, end = " ")

        print("|", letras_fila[i])

    print("[L] = Libre.   [V] = Vendido.   [R] = Reservado.")

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
        print("Funciones: ")
        # Mostramos las opciones
        for i in range(len(funciones)):
            print(i + 1, ".", funciones[i]["titulo"], "($", funciones[i]["precio"], ")")
            
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
    inicializar_matriz()  #Crear la sala vacía
    configurar_inicio()   #Elegir película
    
    while True:
        limpiar_consola()
        mostrar_sala()
        
        print("1. Vender (en proceso de creación).")
        print("2. Salir")
        
        seleccion = input("Número de selección: ")
        
        if seleccion == '1':
            print("En proceso de creación.")
            time.sleep(1) #Pausar programa 1 segundo (time.sleep).
            
        elif seleccion == '2':
            print("Programa cerrado.")
            break

if __name__ == "__main__": #Ejecutar programa
    iniciar_programa()
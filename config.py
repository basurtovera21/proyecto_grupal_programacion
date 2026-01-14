#Persona 5
import json

def cargar_funciones(): #Leer archivo .json y devolver datos.
    try:
        with open('funciones.json', 'r', encoding = 'utf-8') as funciones: #Tipo de condicicación de texto que permite leer correctamente caracteres (tildes, ñ, caracteres especiales).
            datos = json.load(funciones) #Leer archivo completo (load) e interpretar (list).
            return datos
            
    except FileNotFoundError:
        print("No se  puede localizar el archivo solicitado.")
        #Retornar lista vacía (evita que el programa falle).
        return []
        
    except json.JSONDecodeError:
        print("Error de sintaxis y/o formato del archivo.")
        return []
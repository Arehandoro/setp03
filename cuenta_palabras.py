#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 02 - Cuenta palabras:


# Libreria para aumentar la profundidad de la recursión y evitar errores, ya que el sistema por precaución limita la recursión para proteger la memoria disponible.
import sys 
sys.setrecursionlimit(10000)


#Función que ingresa el texto del archivo al diccionario.
def ingresa_texto(cadena):
    cadena_mayus = cadena.upper()    #Convierte todas las letras minusculas del string en mayusculas y guarda el string resultante.
    lista = cadena_mayus.split()    #La función split() retorna una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por los espacios en blancos y salto de lineas.
    diccionario = dict()    #Se declara un diccionario vacio.
    for palabra in lista:    #Recorre la lista palabra por palabra.
        if (palabra.isalpha()):    #Solo ingresan las palabras con letras, incluidas las con acentos.  No ingresan palabras con otros caracteres como numeros al diccionario.
            frecuencia = lista.count(palabra)    #La función count() retorna el número de veces que se encuentra la palabra en la lista.
            diccionario[palabra] = frecuencia    #Ingresa la palabra con su frecuencia al diccionario. (llave=palabra, valor=frecuencia)
    return diccionario    #Retorna el diccionario.


#Función que cuenta las palabras del texto, mediante la suma de las frecuencias de las palabras en el diccionario.
def cuenta_palabras(diccionario):
    if (len(diccionario) == 0):    #Si el diccionario esta vacio, termina la recursividad.
        return 0
    else:
        aux = diccionario    #Se copia el diccionario en un diccionario auxiliar para no borrar el original.
        suma = aux.pop(list(aux.keys())[0])    #Se borra la primera palabra del diccionario y nos retorna su frecuencia en la variable (suma).
        return cuenta_palabras(aux) + suma    #Retorna la suma de las frecuencias de las palabras, y llama a la función con 1 elemento menos.



f = open('funes.txt', encoding='utf-8')    #Abre el archivo y lo guarda en la variable "f".
cadena = f.read()    #Guarda todo el contenido del archivo retornado en string en cadena.
f.close()    #Cierra el archivo.
diccionario = ingresa_texto(cadena)
print("\nLa cantidad de palabras que hay en el texto es:",cuenta_palabras(diccionario),"palabras.")


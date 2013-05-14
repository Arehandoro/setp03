#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 01 - Pascal:

def tri_pascal(n):    #Función que imprime y retorna cada linea hasta el grado evaluado del triangulo pascal.
    if (n == 0):    #Si (n) es igual a cero finaliza la recursividad.
        return [1]
    else:
        linea = [1]    #Agrega un 1 al principio de la lista linea.
        linea_anterior = tri_pascal(n-1)    #Se llama asi misma la función, retornando la linea anterior.
        for i in range(len(linea_anterior)-1):
            coeficiente = linea_anterior[i] + linea_anterior[i+1]    #Suma el coeficiente de la posicion (i) con su sucesor, ambos de la linea anterior para retornar el coeficiente actual.
            linea.append(coeficiente)    #Se agrega el coeficiente a la lista linea.
        linea += [1]    #Agrega un 1 al final de la lista linea.
        print(linea)    #Imprime la linea
    return linea    #Retorna la lista linea del grado evaluado del binomio.

n = int(input("Ingrese el grado del Binomio:  "))    #Lee la variable tipo entero ingresada por el usuario.
print("\nTriángulo de Pascal formado de los coeficientes hasta el grado",n,"\n\n")
if (n == 0):    #Si (n) es igual a cero imprime primera linea del triangulo pascal.
    print("[1]")
elif (n > 0):    #Si (n) es de grado 1 en adelante, imprime la primera linea y llama a la función que imprime las restantes.
    print("[1]")
    tri_pascal(n)    #Llama a la función recursiva.

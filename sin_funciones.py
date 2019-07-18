#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	La linea 1 y 2 no son comentarios, aunque aparentemente lo sean.
	
	En sistemas Unix si en el archivo los dos primeros caracteres de la
primera linea son #! se le esta indicando al Sistema Operativo UNIX que 
trate al archivo como un Script y que lo ejecute utilizando el interprete
declarado desde el tercer caracter en adelante (en este caso python)

	El script en los sistemas operativos Unix es un archivo que tiene comandos 
que pueden ser ejecutados desde una ventana de comandos (conocida tambien por: terminal,
ventana shell, entre otros)

	La linea 2 se le indica a python (hasta la version 3) que use la CODIFICACION UTF-8 
para mostrar caracteres, con lo cual si en el script que estamos escribiendo incluimos 
algunos de estos caracteres ñ á é u otros caracteres "raros" en la ventana de comando,
cuando se ejecute el script, se verán correctamente y no con "simbolos raros". A partir 
de la version 3 de python no es necesario incluir la linea 2, ya que por defecto 
interpreta al script con el UTF-8. Esto se logro luego de que muchos programadores lo pidan 
y python lo tomo en cuenta. Cualquier programador que se registre como "desarrollador" 
en la pagina de python (sea aprendiz, master o lo que sea) puede proponer mejoras 
al interprete de python (lo que se conoce con las siglas PEP. Python Enhancement Proposal).

"""

#----------------------( script sin funciones )-------------------------------

"""
	Voy a mostrarte como se podria realizar un script para que python pida que se ingrese
dos numeros enteros (para no complicarla, pero vos ya sabes como hacerlo cuando no son
enteros y estaria bueno que lo hagas) y que luego haga esto:

	(A) muestre el resultado de la suma de ambos numeros
	(B) muestre el resultado de la suma del resultado de la primera suma mas 10

"""

"""

Explicacion:
	Pedimos que se ingresen los numeros. Esos numeros deben ser almacenados en un espacio
de la memoria y para eso se debe a cada numero pasarselo a una variable (en este caso 
cada numero a una variable diferente vamos a ponerle numeroUno y numeroDos).

	Antes de seguir te explico algo de los nombres de las variables y nombre de las funciones
para que cualquier programador entienda y se le sea mas facil seguir el programa, se codifica
utilizando la norma CAMELCASE (porque se asemejan el como esta escrito a las jorobas de los
camellos). Vas a encontrar infinidades de formas de codificar, pero... si te acostumbras 
al CamelCase se te va a ser mas facil a vos y al que tenga que leer el programa. 

Ejemplos:
		numeroUno
		numero_uno
		numero_Uno
		_numeroUNO

		cualquiera de las formas anteriores podes utilizar y por convencion se trata de evitar
declarar nombres de variables con la primera letra en mayusculas:

		NumeroUno
		Numero_uno
		NumeroUNO
		NUMEROUNO

		Para CONSTANTES deberias de utilizar todo en mayusculas:
	
		GRAVEDADTIERRA = 9.8
		GRAVEDAD_TIERRA = 9.8
	
		fijate que aca se puede utilizar el _ entre las dos palabras para que sea mas facil
leer ya que no se aprecia el CamelCase. Cuanto mas te aproximes a lo que se utiliza vas a ser
mejor visto cuando otro programador vea tu script, y mas aun si pedis ayuda para cuando un script
no te funciona o no sabes como desarrollarlo.

Seguimos: se codifica las dos lineas que van a pedir el ingreso de los numeros y se lo almacena
en sus respectivas variables. Fijate que a diferencia del ejercicio 5 que hicimos ahora dice 
int(input(....)) eso se pone para que el valor que se almacene en la variable sea convertido 
a un numero entero. 

numeroUno = int(input("Ingrese primer valor:"))
numeroDos = int(input("Ingrese segundo valor:"))

	- voy a detenerme de nuevo para que te ayude a pensar: que pasa si hacemos esto?
	
	numeroUno = int(input("ingrese primer valor:"))
	numeroUno = int(input("ingrese segundo valor:"))

	- la codificacion de las dos lineas anteriores ESTA BIEN, pero no hace lo que nosotros queremos, 
	por que? porque cuando pidamos que ingrese el segundo valor se lo estamos almacenando en la misma
	variable del primer valor, por lo tanto se pierde el primer valor. (Pensalo hace la prueba de 
	escritorio - prueba de escritorio es simular lo que el script hace)
	
	paso 1: numeroUno = 5
	paso 2: numeroUno = 8
	
	¿Que numero quedo almacenado en la variable numeroUno? el 8, el numero 5 fue pisado/reemplazado por el 8.

Sigamos: ya le pedimos 2 valores al usuario, ahora lo sumamos, y el resultado de la suma lo almacenamos
en la memoria. como se almacena en memoria? por medio de una variable.

suma = numeroUno + numeroDos

Hasta aca todo lindo, pero que pasa si en el script tenemos varios lugares donde terminamos
haciendo una suma de dos numeros? no vamos a estar continuamente poniendo
s1 = n1 + n2
s2 = n2 + n2
....

te muestro un ejemplo donde en tres lugares hago una suma (para que veas nada mas)

n1 = 10
n2 = 30

s = n1 + n2

n3 = 5
n4 = 8

s1 = n3 + n4

s3 = s + s1

s, s1 y s3 almacenan la suma de dos numeros. Al ser operaciones (en este caso matematicas) 
que se repiten, "eso" que se repite se lo puede codificar como una funcion. 

def suma(valor1, valor2):
	return (valor1 + valor2)

y luego reemplazamos donde codificamos la suma quedando asi:

n1 = 10
n2 = 30

s = suma(n1, n2)

n3 = 5
n4 = 8

s1 = suma(n3, n4)
s3 = suma(s, s1)

¿Que es lo que hace? ejecuta la funcion definida como "suma" utilizando los 
dos valores que se le pasan. (analizalo y lo que no se entienda me lo preguntas)

A este tipo de funciones en donde se le transfiere valores y cuyos valores
no van a ser cambiados por la funcion, se les dice "funciones con variables por valor". 
A otras funciones se les dice "funciones con variables por referencia" que vas a verlo
mas adelante.

Te dejo el programa que empezamos completo sin utilizar funciones asi lo probas y 
modificalo para que utilice funciones.
Y como ya deberias de saber hacerlo modificalo para que no se produzca el "error
en tiempo de ejecuacion" que se produce al introducir otro tipo de datos que no 
sea un numero entero (acordate del try:)

"""

numeroUno = int(input("Ingrese primer valor:"))
numeroDos = int(input("Ingrese segundo valor:"))

suma1 = numeroUno + numeroDos

suma2 = suma1 + 452

print("Primera suma: {}". format(suma1))
print("Primera suma + el numero 452: {}". format(suma2))


#suerte pa!

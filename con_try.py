#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	
	try: intentar. es lo que le dice el script al python,
que intente ejecutar las operaciones que se tipean a partir de 
ese comando, si no puede ejecutarlo porque se produce un error
'en tiempo de ejecucion' que le informe al usuario pero que no
detenga la ejecucion del script

	Es muy importante que se respete el TAB al inicio de la linea
que lo sigue a cualquier comando de python que asi lo requiera,
jamas poner ESPACIOS, tiene que ser TAB (la diferencia visual vos
no la vez, pero un espacio para python tiene el codigo ASCII (32) y
en cambio el codigo para el TAB es ASCII(09) esto es informacion 
adicional)

	por ejemplo si vos presionas tres veces el espacio antes de una 
	linea python lo veria asi:
	323232a = input()
	
	en cambio, si tu TAB esta definido para que cuando lo presiones se
	desplace 3 lugares, el python lo veria asi:
	09a = input()

	si usas algun editor de codigo, sublimetext, atom, e incluso el mismo
	editor interno de cualquier version UNIX y tu script tiene 
	extension .py automaticamente cuando presiones ENTER y sea necesario 
	que se tabule la siguiente linea el editor automaticamente lo va a ser,
	por ejemplos en sentensias IF, ELSE, TRY, etc.

"""

#codigo para probar el try

try:
	numeroUno = int( input( "Ingrese un valor: "))

	print("el numero ingresado es: {} ".format(numeroUno))

except ValueError:

	print( "Se produjo un error al ingresar el dato")

"""
Explicacion de las lineas de arriba:

En la linea 37 el TRY que se esta definiendo va a controlar 
el ingreso del primer numero que se almacena en la variable numeroUno, 
si el ingreso fue correcto sigue con la linea 39, al no tener nada esa linea
sigue con la 40 en donde muestra por pantalla el valor que tiene almacenado
la variable "numeroUno". 

Si, se llega a ingresar un valor no valido al ejecutarse la linea 38 (como pueden ser letras), 
el TRY sigue la ejecucion del programa sin producir un "error en tiempo de ejecucion" 
y salta a la linea 42 "except ValueError:" que es la que captura el error que se produce y 
ejecuta todas las lineas que esten a partir de esa linea de definicion, en este caso
ejecuta la linea 44 y muestra en pantalla el cartel "se produjo un error al ingresar el dato".

OJO/ojito/ojato/ojeeeee:
la variable "ValueError" es una variable interna del python en donde almacena el error y 
debe ir siempre despues de "except" respetando ademas el CamelCase (mayusculas y minusculas)

"""

#Suerte pa! no estas solo
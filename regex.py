#!/usr/bin/python3

# creando un pequeño script que lee datos de un archivo txt.
# by Blackster


# importamos la libreria re.
import re
		

def buscar_nombres():
	""" funcion que abre nuestro archivo txt para leerlo y encontrar los nombres """
	with open('nombres.txt', "r") as name_list:
		for nombres in name_list:
			# buscar por el primer elemento dado.
			"""if re.findall("^HERNANDEZ", nombres):
				print(nombres)"""
			if re.findall('^{}'.format(nombre), nombres):
				print(nombres)


if __name__ == '__main__':
	nombre = str(input("[*]Introduce el apellido de la persona: "))
	buscar_nombres()
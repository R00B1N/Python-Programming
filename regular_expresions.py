#!/usr/bin/python3


# creando un pequeños script con expresiones regulares.
# by Blackster.


# importamos los modulos necesarios.
import re

def ejecutar_busqueda():
	# lista de nombres para nuestro script.
	nombres = ['Juan Caballero',
				'Pedro Perez',
				'Junior Hernandez', 
				'Sebastian Garcia',
				'Juan Valdez',
				'Oscar Sanchez']
	# usar expresiones regulares para encontrar nombres dentro de una lista.
	for busqueda in nombres:
		""" funcion que ejecuta una busqueda en nuestra lista
		 de nombres y nos arroja los resultados."""

		# ejecutamos nuestra busqueda 
		if re.findall('^Juan', busqueda): # el simbolo '^' se utiliza para jerarquizar la busqueda por Mayuscula.
			print(busqueda) # imprimir la busqueda por nombre.
		elif re.findall('Hernandez$', busqueda): # realizar una busqueda por todas las coincidencias que terminen por 'Hernandez'.
			print(busqueda)
		""" El caracter '^' se utiliza para buscar los elementos que empiezen con dichos caracteres especificos
		 y el caracter '$' se utiliza para buscar elementos que terminen con  dichos caracteres.
		"""

if __name__ == '__main__':
	ejecutar_busqueda()
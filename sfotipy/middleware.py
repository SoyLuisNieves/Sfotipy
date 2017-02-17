from random import choice
from django.shortcuts import redirect

countries = ['Colombia', 'Peru', 'Mexico']

def Im_From(request):
	return choice(countries)

class CountryMiddleware():
	def process_request(self, request):
		country = Im_From(request)
		if country == 'Mexico':
			return redirect('http://google.com')

# Middleware es una clase que tiene metodos de process_request y puede manejar errores


# Procesador de contexto sirve unicamente para agregar informacion para las plantillas
# Un Middleware puede modificar el comportamiento global de la aplicacion
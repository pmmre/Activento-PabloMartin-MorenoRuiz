from django.test import TestCase
from .models import Usuario,Categoria
from .views import registrarse,index,user,crearCategoria,listarCategorias,listarUsuario,siguiendo
from django.shortcuts import render
from django.test.client import Client
from django.core.urlresolvers import reverse

import unittest


class TestStringMethods(unittest.TestCase):

	def test_index(self):
		"""
		 	Comprobamos que la pagina index funciona mandandole
		 	una peticion get y comprobando que el codigo de 
		 	respuesta es correcto (200)
		"""
		c = Client()

		respose = c.get(reverse('inicio'))
		self.assertEqual(respose.status_code,200)

	def test_registrarse(self):
		"""
    		Con este test se va comprobar que podemos instertar un usuario
    		que si lo volvemos a intentar insertar no nos deja hacerlo sin 
    		darnos un error e intentar introducir usuario con las contrasenias 
    		mal introducidas.
    		Para todo ello usamos un cliente con el que le mandamos peticiones
    		post a registrarse y comprobamos los resultados
    	"""
		c = Client()

		response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
		self.assertEqual(response.status_code, 200)

    	
		usu = Usuario(nombre="Pablo",password="entero")
		self.assertEqual(usu.nombre, "Pablo")
		self.assertEqual(usu.password, "entero")

		response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
		self.assertEqual(response.status_code, 200)
		usu = Usuario.objects.get(nombre="Pablo")

		response = c.post(reverse('registrarse'),{'nombre':"Pablo2",'password':"ent",'password2':"ent"})
		self.assertEqual(response.status_code, 200)
    	
    	
		response = c.post(reverse('registrarse'),{'nombre':"Pablo2",'password':"entera",'password2':"entero"})
		self.assertEqual(response.status_code, 200)


	def test_iniciar_sesion(self):
		"""
    		Con este test voy a comprobar si funciona bien el inicio de
    		sesion para ello voy crear un cliente, lo registrare usando
    		parte del codigo del test para registrar y luego inicio sesion
    		dos veces una correctamente y otra erroneamente, comprobando
    		siempre que no falla el programa
    	"""

		c = Client()

		response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
		self.assertEqual(response.status_code, 200)

    	

		usu = Usuario(nombre="Pablo",password="entero")
		self.assertEqual(usu.nombre, "Pablo")
		self.assertEqual(usu.password, "entero")


		response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entero"})
		self.assertEqual(response.status_code, 200)


		response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entera"})
		self.assertEqual(response.status_code, 200)

	def test_crear_categoria(self):
		"""
			Con este test se va a comprobar que se pueden crear correctamente
			las categorias. Para ello creamos una categoria y comprobamos si 
			esta introducida en la base de datos, volvemos a intentar introducir
			la misma categoria y comprobamos si no esta duplicada.

		"""
		c = Client()

		response = c.post(reverse('crearCategoria'),{'nombre':"Ciclismo",'descripcion':"Ir con la bici"})
		self.assertEqual(response.status_code,200)

		usu = Categoria.objects.get(nombre="Ciclismo")
		self.assertEqual(usu.nombre, "Ciclismo")
		self.assertEqual(usu.descripcion, "Ir con la bici")

		response = c.post(reverse('crearCategoria'),{'nombre':"Ciclismo",'descripcion':"Ir con la bici"})
		self.assertEqual(response.status_code,200)	
		usu = Categoria.objects.get(nombre="Ciclismo")

	def test_listar_categoria(self):
		"""
			Con este test se va a comprobar que la funcion listar categorias se
			ejecuta correctamente para ello voy a crear un usuario e iniciarlo
			comprobando en cada momento que todo va funcionanado y despues
			comprobar que listar categoria funciona, lo hago asi pues use una
			variable de session.
		"""
		c = Client()


		response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
		self.assertEqual(response.status_code, 200)

		response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entero"})
		self.assertEqual(response.status_code, 200)

		response = c.get(reverse('listarCategorias'))
		self.assertEqual(response.status_code, 200)


	def test_listar_usuarios(self):
		"""
			Con este test vamos a comprobar listar usuarios que debe de mostrarnos
			los otros usuarios que existen en la aplicacion, para ello creo mi usuario
			y lo inicio. Una vez hecho esto le pido la lista de usuario que me saldran
			todos menos el mio que esta introducido en una variable de sesion
		"""
		c = Client()

		response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
		self.assertEqual(response.status_code, 200)

		response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entero"})
		self.assertEqual(response.status_code, 200)	

		response = c.get(reverse('listarUsuario'))
		self.assertEqual(response.status_code, 200)

	def test_siguiendo(self):
		"""
			Con el siguiente test voy a comproba que la siguiente pagina funciona
			aunque no tengo implementado su funcionamiento.
		"""
		c = Client()

		response = c.get(reverse("siguiendo"))
		self.assertEqual(response.status_code,200)


if __name__ == '__main__':
	unittest.main()
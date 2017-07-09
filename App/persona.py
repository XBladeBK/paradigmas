from abc import ABCMeta, abstractmethod
from persistent import Persistent
"""@abstract"""
class Persona(Persistent):
	
 	__metaclass__ = ABCMeta
	

	def __init__ (self,nombre,apellido,documento,edad):
		self.nombre=nombre
		self.apellido=apellido
		self.documento=documento
		self.fecha_nac=fecha_nac

class Contacto:
	def __init__(self,telefono='',celular='',email='',direccion=''):
		self.telefono=telefono
		self.celular=celular
		self.email = email
		self.direccion=direccion
	
	def get_telefono(self):
		return self.telefono
	
	def get_celular(self):
		return self.celular

	def get_email(self):
		return self.email
	
	def get_direccion(self):
		return self.direccion
	@abstractmethod
	def agregar(self):
		pass
	@abstractmethod
	def modificar(self):
		pass
	@abstractmethod
	def borrar(self):
		pass

	
	

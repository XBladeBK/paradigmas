
from abc import ABCMeta, abstractmethod
#TODO 
class Comprable():
	__metaclass__ = ABCMeta
	
	def __init__(self, precioMensual, precioAnual):
		
		self.precioMensual=precioMensual
		self.precioAnual=precioAnual

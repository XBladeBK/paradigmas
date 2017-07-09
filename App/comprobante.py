from abc import ABCMeta, abstractmethod

class Comprobante(object):
	
	 __metaclass__ = ABCMeta

	 @abstractmethod
	 def imprimir(self):
	 	#Metodo que debera llamar a la impresora
	 	pass
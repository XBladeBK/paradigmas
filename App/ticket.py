from lugar import Lugar
import random
from datetime import datetime
from persistent import Persistent
from comprobante import Comprobante

class Ticket(Comprobante, Persistent):
	
	def __init__(self):
		self.numero=0
		self.lugar=0
		self.montoTotal=0
		self.fechaE=None
		self.fechaS=None
		self.importeFinal=None
	def setFechaEntrada(self):
		self.fechaE = datetime.now()

	def setFechaSalida(self):
		self.fechaS = datetime.now()	

	def calcularMinutos(self):
		diferenciaFecha=self.fechaS-self.fechaE
		segundos=diferenciaFecha.total_seconds()
		return segundos/60



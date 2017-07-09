from lugar import Lugar
from persistent import Persistent
import persistent.list

class Estacionamiento (Persistent):
	def __init__(self, cantidadLugares, precioHora):
		self.clientes=[]
		self.cantidadLugares = cantidadLugares
		self.lugares=persistent.list.PersistentList()
		self.precioHora=precioHora
		
		for i in range(cantidadLugares):
			l = Lugar()
			l.id = i
			self.lugares.append(l)
	
	

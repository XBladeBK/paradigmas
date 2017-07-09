from automovil import Automovil
from persistent import Persistent
from comprable import Comprable
class Lugar(Comprable, Persistent):

	def __init__(self):
		
		#Comprable.__init__()
		self.id = None
		self.libre = True #libre
		self.clienteDocumento = None
		self.autoIndex = None

'''MOMENTANEAMENTE, TODOS LOS LUGARES DEL ESTACIONAMIENTO SON COMPRABLES
PERO SE ESTIMA PARA EL FUTURO, HABILITAR UN SEGUNDO PISO DE ESTACIONAMIENTO EN LA PLANTA ALTA
PERO DEBIDO A PROBLEMAS DE UBICACION, ESTOS NO SERAN COMPRABLES COMO LOS DE LA PLANTA BAJA.
'''

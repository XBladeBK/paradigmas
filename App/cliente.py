from persona import Persona
from automovil import Automovil
import persistent.list

class Cliente(Persona):

	def __init__ (self,nombre,apellido,documento,fecha_nac):
				
		self.automoviles=persistent.list.PersistentList()	
		self.nombre=nombre
		self.apellido=apellido
		self.documento=documento
		self.fecha_nac=fecha_nac
		


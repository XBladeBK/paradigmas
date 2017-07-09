from mizodb import MiZODB, transaction
from cliente import Cliente
from ticket import Ticket
from estacionamiento import Estacionamiento
from lugar import Lugar
from automovil import Automovil
import BTrees.OOBTree

class Model:

	def initDB(self):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		dbroot.clientes = BTrees.OOBTree.BTree() 
		dbroot.tickets = BTrees.OOBTree.BTree()
		dbroot.numeroTiketActual = 0
		transaction.commit()
		db.close()
		
	def guardarCliente (self,cliente):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		dbroot.clientes[cliente.documento]= cliente
		transaction.commit()
		db.close()
		
	def guardarTicket(self, ticket):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		ticket.numero = dbroot.numeroTiketActual
		dbroot.numeroTiketActual+=1
		dbroot.tickets[ticket.numero]= ticket
		transaction.commit()
		db.close()
		return ticket.numero

	def guardarEstacionamiento(self, estacionamiento):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		dbroot.estacionamiento = estacionamiento
		transaction.commit()
		db.close()
	
	def actualizarLugar(self, identif, libre, clienteDoc, autoIndex):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		lugarOrig = dbroot.estacionamiento.lugares[identif]
		lugarOrig.libre = libre
		lugarOrig.clienteDocumento = clienteDoc
		lugarOrig.autoIndex = autoIndex
		transaction.commit()
		db.close()

	def actualizarTicket(self, numero, fechaS, importeFinal):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		ticketOrginal = dbroot.tickets[numero]
		ticketOrginal.fechaS = fechaS
		ticketOrginal.importeFinal = importeFinal

		transaction.commit()
		db.close()

	def obtenerEstacionamiento(self):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		try:
			estacionamiento = dbroot.estacionamiento
		except:
			db.close()
			return False
		
		for l in estacionamiento.lugares:
			l.libre
		db.close()
		return estacionamiento
		
	def buscarCliente (self,documento):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		try:
			cliente = dbroot.clientes[documento]
		except:
			db.close()
			return False
		if isinstance(cliente, Cliente):		
			cliente.automoviles[0].chapa
		else:
			cliente= "cliente no encontrado"
		db.close()
		return cliente

	def buscarTicket(self, numero):
		db = MiZODB('./Data.fs')
		dbroot = db.raiz
		try:
			ticket = dbroot.tickets[numero]
			ticket.numero
		except Exception as e:
			print e
			db.close()
			return False
		if isinstance(ticket, Ticket):
			db.close()
			return ticket
		else:
			db.close()
			return False	

	

	

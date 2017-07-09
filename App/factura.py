from comprobante import Comprobante

class Ticket(Comprobante, Persistent):

	def __init__(self, ruc, descripcion, montoTotal, numeroFactura):
		self.ruc = ruc
		self.descripcion = descripcion
		self.montoTotal = montoTotal
		self.numeroFactura = numeroFactura

	def imprimir(self):
		# LLAMARA A LA IMPRESORA
		
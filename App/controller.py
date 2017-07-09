from model import Model
from estacionamiento import Estacionamiento
from lugar import Lugar
from cliente import Cliente
from ticket import Ticket
from automovil import Automovil
import os
from Tkinter import *
import tkMessageBox

class Controller():
	def __init__(self):
		self.model = Model()
		self.root=Tk()
		self.root.title('....::::SISTEMA GESTOR DE ESTACIONAMIENTO::::....')
		self.root.geometry("500x400+50+50")
		self.vp=Frame(self.root)
		self.vp.grid(column=0,row=0,padx=(150,50),pady=(20,20))
		self.vp.columnconfigure(0,weight=1)
		self.vp.rowconfigure(0,weight=1)
		e = self.model.obtenerEstacionamiento()
		if e == False :
			e = self.cargarEstacionamiento()
		else:
			self.estacionamiento = e
			self.crearMenu()
			self.root.mainloop()
		

	def cargarEstacionamiento(self):
		self.root.geometry("500x400+50+50")
		self.vp.grid(column=0,row=0,padx=(50,50),pady=(20,20))
		Label(self.vp, text='INGRESE LOS DATOS DEL ESTACIONAMIENTO').grid(row=1,column=2)
		Label(self.vp, text='Cantidad de lugares: ').grid(row=2,column=1)
		Label(self.vp, text='Precio por hora(Gs): ').grid(row=3,column=1)
		cantidadLugares = IntVar(self.root)
		precio = IntVar(self.root)
		Entry(self.vp, textvariable=cantidadLugares).grid(row=2,column=2)
		Entry(self.vp, textvariable=precio).grid(row=3,column=2)
		Button(self.vp,text='Aceptar',bd=3,command=lambda:self.guardarEstacionamiento(cantidadLugares, precio)).grid(row=4,column=1)
		self.root.mainloop()
	


	def guardarEstacionamiento(self,cantidadLugares, precio):
		try:
			cantidadLugares = int(cantidadLugares.get())
			precio = int(precio.get())
			if (cantidadLugares<=0 or precio <=0):
				Label(self.vp, text='Datos invalidos',fg="red").grid(row=4,column=2)
				return			
		except:
			Label(self.vp, text='Datos invalidos',fg="red").grid(row=4,column=2)
			return

		e = Estacionamiento(cantidadLugares, precio)
		e.cantidadLugares = cantidadLugares
		e.precio = precio
		self.model.initDB()
		self.model.guardarEstacionamiento(e)
		tkMessageBox.showinfo('INFO','Datos cargados con exito!')
		self.estacionamiento = e
		self.root.destroy()
		self.root=Tk()
		self.root.title('....::::SISTEMA GESTOR DE ESTACIONAMIENTO::::....')
		self.root.geometry("500x400+50+50")
		self.vp=Frame(self.root)
		self.vp.grid(column=0,row=0,padx=(150,50),pady=(20,20))
		self.vp.columnconfigure(0,weight=1)
		self.vp.rowconfigure(0,weight=1)
		self.crearMenu() # va al metodo para crear el menu principal




	def crearMenu(self):
		Label(self.vp, text='Precio por hora(Gs): ' + str(self.estacionamiento.precioHora)).grid(row=0,column=1)
		self.botonIngreso=Button(self.vp, text='Ingreso vehicular',command=self.registrarIngreso,fg="green",bd=3).grid(row=1,column=1)
		self.botonSalida=Button(self.vp, text='Salida vehicular',command=self.registrarSalida,fg="red",bd=3).grid(row=2,column=1)
		Label(self.vp, text='------------------------- ').grid(row=3,column=1)
		self.botonNuevoCliente=Button(self.vp, text='Nuevo cliente',command=self.nuevoCliente,bd=3).grid(row=5,column=1)
		self.botonComprarLugar=Button(self.vp, text='Comprar lugar',bd=3).grid(row=6,column=1)
		self.botonListarClientes=Button(self.vp, text='Listar clientes',bd=3).grid(row=7,column=1)
		self.botonAgregarAutomovil=Button(self.vp,text='Agregar Automovil a Cliente',command=self.agregarAutomovil,bd=3).grid(row=8,column=1)
		Label(self.vp, text='\n ------------------------- \n').grid(row=9,column=1)
		self.botonSalir=Button(self.vp, text='Salir del sistema',command=self.root.destroy,bd=3).grid(row=10,column=1)




	def obtenerDatos(self, ventanaCliente,fp):
		nombreCli=nombre.get() 
		apellidoCli=apellido.get()
		try: #CONTROLA LA ENTRADA DEL NRO DE CEDULA
			docClie=int(ci.get())
		except:
			Label(fp, text='NUMERO DE CEDULA INVALIDO',fg='red').grid(row=14,column=2)
			return
		
		fecha_nacCli=fecha_nac.get()
		while True:
			try:
				cliente = Cliente(str(nombreCli), str(apellidoCli), int(docClie), str(fecha_nacCli))
				auto = Automovil()
				auto.marca = marca.get()
				auto.chapa = chapa.get()
				auto.color = color.get()
				auto.anio = anho_fab.get()
				cliente.automoviles.append(auto)
				self.model.guardarCliente(cliente)
				tkMessageBox.showinfo('INFO','Se ha creado el nuevo cliente: '+cliente.nombre+' \nNro de cedula: '+str(docClie))
				ventanaCliente.destroy()
				break
			except:
				break
			




	def nuevoCliente(self):
	#CREACION Y CONFIG DE LA VENTANA
		ventanaCliente=Toplevel(self.root)
		ventanaCliente.geometry("500x400+250+250")
		ventanaCliente.title('.......::::NUEVO CLIENTE::::......')
		fp=Frame(ventanaCliente)
		fp.grid(column=0,row=0,padx=(50,50),pady=(20,20))
		fp.columnconfigure(0,weight=1)
		fp.rowconfigure(0,weight=1)
	#LABELS	DEL NUEVO CLIENTE
		Label(fp, text='INGRESE LOS DATOS DEL CLIENTE').grid(row=1,column=2)
		Label(fp, text='Nombre: ').grid(row=2,column=1)
		Label(fp, text='Apellido: ').grid(row=3,column=1)
		Label(fp, text='Numero de Cedula: ').grid(row=4,column=1)
		Label(fp, text='Fecha de Nacimiento: ').grid(row=5,column=1)
		Label(fp, text='Datos del automovil').grid(row=6,column=2)
		Label(fp, text='Marca: ').grid(row=7,column=1)
		Label(fp, text='Modelo: ').grid(row=8,column=1)
		Label(fp, text='Chapa: ').grid(row=9,column=1)
		Label(fp, text='Anho de fabricacion: ').grid(row=10,column=1)
		Label(fp, text='Color: ').grid(row=11,column=1)
	#VARIABLES PARA EL NUEVO CLIENTE 	
		global nombre
		global apellido
		global ci
		global fecha_nac
		global nombre
		global apellido
		global ci
		global fecha_nac
		nombre=StringVar(ventanaCliente)
		apellido=StringVar(ventanaCliente)
		ci=StringVar(ventanaCliente)
		fecha_nac=StringVar(ventanaCliente)	
	#CAMPOS DE TEXTO
		entryNombre=Entry(fp, textvariable=nombre).grid(row=2,column=2)
		entryApellido=Entry(fp, textvariable=apellido).grid(row=3,column=2)
		entryCliente=Entry(fp, textvariable=ci).grid(row=4,column=2)
		entryFecha_nac=Entry(fp,textvariable=fecha_nac).grid(row=5,column=2)
		

			#VARIABLES PARA EL NUEVO CLIENTE	
		global marca
		global modelo
		global chapa
		global anho_fab
		global color
		marca=StringVar(ventanaCliente)
		modelo=StringVar(ventanaCliente)
		chapa=StringVar(ventanaCliente)
		anho_fab=StringVar(ventanaCliente)
		color=StringVar(ventanaCliente)	
	#CAMPOS DE TEXTO
		entryMarca=Entry(fp, textvariable=marca).grid(row=7,column=2)
		entryModelo=Entry(fp, textvariable=modelo).grid(row=8,column=2)
		entryChapa=Entry(fp, textvariable=chapa).grid(row=9,column=2)
		entryAnho=Entry(fp,textvariable=anho_fab).grid(row=10,column=2)
		entryColor=Entry(fp,textvariable=color).grid(row=11,column=2)
	#BOTONES
		crear=Button(fp,text='Crear Cliente',bd=3,command=lambda:self.obtenerDatos(ventanaCliente,fp)).grid(row=12,column=1)
		salir=Button(fp,text='Salir',bd=3,command=ventanaCliente.destroy).grid(row=12,column=2)
		#agregarAuto=Button(fp,text='Agregar Automovil',bd=3,command=self.agregarAutomovil).grid(row=9,column=1)
		
		ventanaCliente.mainloop()





	def agregarAutomovil(self):
		# A IMPLEMENTAR
		pass



	def listarCliente(self):
		# A IMPLEMENTAR
		pass



	'''
	 *********** METODOS DE REGISTRAR INGRESO *********** 
	'''
	def registrarIngreso(self):
		#CONFIGURACINO DE LA VENTANA
		ventanaIngreso=Toplevel(self.root)
		ventanaIngreso.geometry("800x400+250+250")
		ventanaIngreso.title('.......::::INGRESO VEHICULAR::::......')
		#CONFIGURACION DE LA VENTANA
		fp=Frame(ventanaIngreso)
		fp.grid(column=0,row=0,padx=(50,50),pady=(20,20))
		fp.columnconfigure(0,weight=1)
		fp.rowconfigure(0,weight=1)
		ciCliente=StringVar(ventanaIngreso)
		Label(fp, text='Ingrese el numero de cedula: ').grid(row=1,column=1)
		#ENTRADA
		Entry(fp, textvariable=ciCliente).grid(row=1,column=2)
		#BOTONES
		Button(fp,text='Buscar',bd=3,command=lambda:self.buscarCliente(ciCliente,ventanaIngreso,fp)).grid(row=1,column=3)
		Button(fp,text='Cancelar',bd=3,command=ventanaIngreso.destroy).grid(row=1,column=4)




	def buscarCliente(self,ciCliente,ventanaIngreso,fp):

		try:
			cliente = self.model.buscarCliente(int(ciCliente.get()))				#CONTROLA DATOS DE INGRESO DE NRO DE CEDULA
		except:
			label = Label(fp,text='Nro de cedula invalido',fg="red").grid(row=3,column=1)
			return
		
		if cliente:
			select=IntVar(ventanaIngreso)
			selectLavado=IntVar(ventanaIngreso)
			lugarSelected=IntVar(ventanaIngreso)
			
			#LABELS

			Label(fp,text='\n\n            Cliente:           ',font=('bold')).grid(row=3,column=1)
			Label(fp,text='\n\n'+cliente.nombre+' '+cliente.apellido,font=('bold')).grid(row=3,column=2)
			Label(fp,text='     Seleccione el automovil',font=('bold')).grid(row=4,column=1)
			Label(fp,text='Desea un lavado?',font=('bold')).grid(row=5,column=2)
			Label(fp,text='Seleccione un lugar: (1 al ' + str(self.estacionamiento.cantidadLugares) +')',font=('bold')).grid(row=10,column=1)
			Entry(fp,textvariable=lugarSelected).grid(row=10,column=2)
			autoSelected = IntVar(ventanaIngreso)
		
		#LISTA LOS CLIENTES
			for index in range(len(cliente.automoviles)): 
				auto = cliente.automoviles[index]
				row = 5 + index
				Radiobutton(fp, text=auto.marca + " " + auto.chapa, variable=autoSelected, value=index).grid(row=row,column=1)
			

			rad=Radiobutton(fp,text='Si',value=5,variable=selectLavado).grid(row=6,column=2)
			rad=Radiobutton(fp,text='No',value=6,variable=selectLavado).grid(row=7,column=2)
			row = 11 + len(cliente.automoviles)
			aceptar=Button(fp,text='Aceptar', command=lambda:self.generarTicket(ventanaIngreso, fp, autoSelected, cliente, lugarSelected),bd=3).grid(row=row,column=1)
			salir=Button(fp,text='Salir',bd=3,command=ventanaIngreso.destroy).grid(row=row,column=2)
		else:
			label = Label(fp,text='Cliente no encontrado',fg="red").grid(row=3,column=1)
			



	def generarTicket(self, ventanaIngreso, fp, autoSelected, cliente, lugarSelected):
		autoIndex = int(autoSelected.get())
		try:
			lugarSelected = int(lugarSelected.get())
		except:
			Label(fp,text='Seleccione un lugar valido', fg="red").grid(row=10,column=3)
			return
		
		if lugarSelected == 0 or lugarSelected>len(self.estacionamiento.lugares):		#control de lugar existente
			Label(fp,text='Seleccione un lugar valido', fg="red").grid(row=10,column=3)
			return
		
		lug = self.estacionamiento.lugares[lugarSelected] #instancia un lugar para verificar su estado 
		if lug.libre==False:
			Label(fp,text='                                       ').grid(row=10,column=3)
			Label(fp,text='Lugar ocupado', fg="red").grid(row=10,column=3)
			return
		else:																			#si no esta ocupado, actualiza datos del lugar
			Label(fp,text='                                ').grid(row=10,column=3)
			print autoIndex
			
			self.model.actualizarLugar(lug.id, False, cliente.documento, autoIndex)
			ticket = Ticket()
			ticket.lugar = lugarSelected
			ticket.setFechaEntrada()
			ticket.numero = self.model.guardarTicket(ticket)
			ventanaIngreso.destroy()
			self.estacionamiento = self.model.obtenerEstacionamiento()
			tkMessageBox.showinfo('INFO','Ticket generado: ' + str(ticket.numero) + '\nFecha de ingreso: ' + str(ticket.fechaE.strftime ('%d/%m/%Y %H:%M')) 
				+'\nCliente: ' + cliente.nombre + ' \nNro de cedula: '+str(cliente.documento))
			



	'''
	 *********** METODOS DE REGISTRAR SALIDA *********** 
	'''
	


	def registrarSalida(self):
		#CONFIGURACION DE LA VENTANA 'SALIDA'
		
		ventanaSalida=Toplevel(self.root)
		ventanaSalida.geometry("800x400+250+250")
		ventanaSalida.title('.......::::SALIDA VEHICULAR::::......')
		fp=Frame(ventanaSalida)
		fp.grid(column=0,row=0,padx=(50,50),pady=(20,20))
		fp.columnconfigure(0,weight=1)
		fp.rowconfigure(0,weight=1)
			#BOTONES PARA ENTRADA DE DATOS 
		nroTicket=StringVar(ventanaSalida)
		Label(fp, text='Ingrese el numero de Ticket: ').grid(row=1,column=1)
		Entry(fp, textvariable=nroTicket).grid(row=1,column=2)
		Button(fp,text='Buscar',bd=3,command=lambda:self.obtenerTicket(nroTicket,ventanaSalida,fp)).grid(row=1,column=3)
		Button(fp,text='Cancelar',bd=3,command=ventanaSalida.destroy).grid(row=1,column=4)
	



	def obtenerTicket(self,nroTicket,ventanaSalida,fp):		

	#BUSCA EL TICKET  EN EL MODEL PARA REGISTRAR LA SALIDA
		try:
			ticket = self.model.buscarTicket(int(nroTicket.get()))
			if ticket.fechaS != None:
				Label(fp, text='NUMERO DE TICKET YA PROCESADO',fg='red').grid(row=2,column=1) #CONTROLA QUE EL TICKET NO SE HAYA COBRADO ANTERIORMENTE
				return
		except:
			etiq=Label(fp, text='NUMERO DE TICKET INVALIDO \nO INEXISTENTE, VUELVA A INTENTAR',fg='red').grid(row=2,column=1)	#CONTROL DE ENTRADA
			return
		if ticket==False:
			etiq=Label(fp, text='NUMERO DE TICKET INVALIDO \nO INEXISTENTE!, VUELVA A INTENTAR',fg='red').grid(row=2,column=1)
			return
		try:								
			
			ticket.setFechaSalida()
			minutos = ticket.calcularMinutos()
			total = self.estacionamiento.precio/60*minutos
			ticket.importeFinal = total
			lugar = self.estacionamiento.lugares[ticket.lugar]
			cliente = self.model.buscarCliente(lugar.clienteDocumento)
			if cliente:
				autoEstacionado = cliente.automoviles[lugar.autoIndex]
				Label(fp, text="Cliente:               "+cliente.nombre + ' ' + cliente.apellido).grid(row=2,column=1)
				Label(fp, text="Automovil estacionado: "+ autoEstacionado.marca+ ' ' + autoEstacionado.color + ', ' + autoEstacionado.chapa ).grid(row=3,column=1)
				Label(fp, text="Fecha de entrada:      "+str(ticket.fechaE.strftime ('%d/%m/%Y %H:%M'))).grid(row=5,column=1)
				Label(fp, text="Fecha de salida:       "+str(ticket.fechaS.strftime ('%d/%m/%Y %H:%M'))).grid(row=6,column=1)
				Label(fp, text='Importe Final:         ' + str(int(ticket.importeFinal)) + ' Gs.').grid(row=7,column=1)
				Button(fp,text='Confirmar',bd=3,command=lambda:self.confirmarSalida(ticket, ventanaSalida)).grid(row=8,column=1)
			else:
				Label(fp, text="Cliente no encontrado               ").grid(row=2,column=1)
		except:
			return
	
			#CONFIRMA LA SALIDA DEL VEHICULO Y ACTUALIZA EL LUGAR QUE SE DESOCUPA
	



	def confirmarSalida(self, ticket, ventanaSalida):
		self.model.actualizarLugar(ticket.lugar, True, None, None)
		self.model.actualizarTicket(ticket.numero, ticket.fechaS, ticket.importeFinal)
		self.estacionamiento = self.model.obtenerEstacionamiento()
		ventanaSalida.destroy()
		tkMessageBox.showinfo('INFO','Ticket procesado!')

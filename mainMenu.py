from tkinter import *
from tkinter.messagebox import *
import cargarClienteProcedures as cli


root = Tk()
root.title('Farmers Market SG')
cli.locate_window(600,600, root)

def hola():
    print( "Hola!")

def cargarNuevo():
    cli.cargarCliente()

menubar = Menu(root)
fontVar = "Arial 12"

# Elemento desplegable “Archivo”
menuArchivo = Menu(menubar, tearoff=0, font=fontVar)
menuArchivo.add_command(label="Abrir", command=hola, font=fontVar)
menuArchivo.add_command(label="Guardar", command=hola, font=fontVar)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=root.quit, font=fontVar)
menubar.add_cascade(label="Archivo", menu=menuArchivo, font=fontVar)

# Elemento desplegable “Editar”
menuClientes = Menu(menubar, tearoff=0)
menuClientes.add_command(label="Cargar Nuevo", command=cargarNuevo, font=fontVar)
menuClientes.add_command(label="Copiar", command=hola, font=fontVar)
menuClientes.add_command(label="Pegar", command=hola, font=fontVar)
menuClientes.add_separator()
menubar.add_cascade(label="Clientes", menu=menuClientes, font=fontVar)

submenu = Menu(menuClientes, tearoff=True, font=fontVar)
submenu.add_command(label='Rotar', command=hola, font=fontVar)
submenu.add_command(label='Deformación libre', command=hola, font=fontVar)
menuClientes.add_cascade(label='Transformación',   menu=submenu, font=fontVar)

# Elemento desplegable “Ayuda”
menuAyuda = Menu(menubar, tearoff=0, font=fontVar)
menuAyuda.add_command(label="Acerca de..", command=hola, font=fontVar)
menubar.add_cascade(label="Ayuda", menu=menuAyuda, font=fontVar)
##############################################################
# crear una caja
##############################################################
frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)

# asociar el popup a la caja
frame.bind("<Button-3>", popup)



# Mostrar menú
root.config(menu=menubar)

root.mainloop()
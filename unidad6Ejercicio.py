##############
# Bibliotecas#
##############
from tkinter import *
from tkinter.messagebox import *
import random
import mysql.connector

###########
#funciones#
###########
def callback():
    registro = (titulo.get(),ruta.get(),descripcion.get())
    if askyesno ('Confirma','¿Desea confirmar el Alta?'):
        mensaje = "Se cargó " + str(micursor.rowcount) + " registro correctamente: " + str(registro[0])
        
        try:
            micursor.execute(sql,registro)
            db.commit()
            showinfo ('Alta Confirmada', mensaje)
        except:
            showinfo ('Alta Rechazada', 'Ha ocurrido un error.')
        reset()
        
    
def reset():
    titulo.set("")
    ruta.set("")
    descripcion.set("")
    
def pickHexRand():
    return "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def newColor():
    nc=pickHexRand()
    l1.configure(bg=nc)
    l2.configure(bg=nc)
    l3.configure(bg=nc)
    master.configure(bg=nc)

def crearEntrada(valueForm,ancho,fila,columna):
    return Entry(master, width=ancho, textvariable=valueForm).grid(row=fila,column=columna)

def crearEtiqueta(texto,fuente,fila, columna):
    etiqueta = Label(master, text=texto, font=fuente)
    etiqueta.grid(row=fila, column=columna,sticky=W)
    etiqueta.configure(bg=bgcolor)
    return etiqueta

###########
#Variables#
###########
master = Tk()
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=" baseprueba1"
)
micursor = db.cursor()
sql = "INSERT INTO producto (titulo,ruta,descripcion) VALUES (%s,%s,%s)"


titulo = StringVar()
ruta = StringVar()
descripcion = StringVar()
bgcolor = pickHexRand()
master.title("Tarea POO")
master.configure(bg=bgcolor)


#Etiquetas
l0 = Label(master, text="Ingrese sus datos", font="Arial 12", width="60", height="1", background="#9932cd", foreground="white", anchor=CENTER).grid(row=0, columnspan=3, sticky=W)
l1 = crearEtiqueta("Título","Arial 12",1, 0)
l2 = crearEtiqueta("Ruta","Arial 12",2, 0)
l3 = crearEtiqueta("Descripción","Arial 12",3, 0)

#Forms
e1 = crearEntrada(titulo,30,1,1)
e2 = crearEntrada(ruta,30,2,1)
e3 = crearEntrada(descripcion,30,3,1)

sorpresa = Button(master,text="Sorpresa", font="Arial 12",command=newColor, width="15")
alta = Button(master, text="Alta", font="Arial 12",command=callback)
sorpresa.grid(row=4, column=2)
alta.grid(row=4, column=1)

mainloop()
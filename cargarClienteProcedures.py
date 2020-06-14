from tkinter import *
cargaC = Tk()
cargaC.title('Cargar Nuevo Cliente')


def cargarCliente():
    #cargaC = Tk()
    #cargaC.title('Cargar Nuevo Cliente')
    #locate_window(600,600, cargaC)
    #labels(cargaC)
    pass

def labels(cargaC):
    font = "Arial 14"
    l_titulo = Label(cargaC, text="Alta de Nuevo Cliente", font="Arial 14 bold", padx=15, pady=15, width="30", height="1",anchor=W)
    l_titulo.grid(row=0, columnspan=2, column=0,sticky=W)
    l_nombre = Label(cargaC, text="Nombre", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_nombre.grid(row=1, column=0, sticky=W)
    e_nombre = Entry(cargaC,font=font, width=15)
    e_nombre.grid(row=2, column=0,padx=15, sticky=W,rowspan=1)

    l_apellido = Label(cargaC, text="Apellido", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_apellido.grid(row=1, column=1, sticky=W,columnspan=3)  
    e_apellido = Entry(cargaC,font=font, width=20)
    e_apellido.grid(row=2, column=1, sticky=W,rowspan=1,columnspan=3)

    l_email = Label(cargaC, text="Email", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_email.grid(row=3, column=0, sticky=W)
    e_mail = Entry(cargaC,font=font, width=25)
    e_mail.grid(row=4, column=0,padx=15, sticky=W,rowspan=1)

    l_calle = Label(cargaC, text="Calle", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_calle.grid(row=5, column=0, sticky=W)
    e_calle = Entry(cargaC,font=font, width=25)
    e_calle.grid(row=6, column=0,padx=15, sticky=W,rowspan=1)
    l_altura = Label(cargaC, text="Altura", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_altura.grid(row=5, column=1, sticky=W)  
    e_altura = Entry(cargaC,font=font, width=5)
    e_altura.grid(row=6, column=1, sticky=W,rowspan=1)
    l_pisoDepto = Label(cargaC, text="Piso/Depto/Torre", font=font, padx=1, pady=7, width=15, height=1,anchor=W)
    l_pisoDepto.grid(row=5, column=2, sticky=W)  
    e_pisoDepto = Entry(cargaC,font=font, width=15)
    e_pisoDepto.grid(row=6, column=2, sticky=W,rowspan=1)

    # CP Localidad Zona
    l_localidad = Label(cargaC, text="Localidad", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_localidad.grid(row=7, column=0, sticky=W)
    e_localidad = Entry(cargaC,font=font, width=25)
    e_localidad.grid(row=8, column=0,padx=15, sticky=W,rowspan=1)
    l_cp = Label(cargaC, text="CP", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_cp.grid(row=7, column=1, sticky=W)  
    e_cp = Entry(cargaC,font=font, width=5)
    e_cp.grid(row=8, column=1, sticky=W,rowspan=1)
    l_zona = Label(cargaC, text="Zona", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_zona.grid(row=7, column=2, sticky=W)  
    e_zona = Entry(cargaC,font=font, width=5)
    e_zona.grid(row=8, column=2, sticky=W,rowspan=1)

    # Celular/fijo
    l_celular = Label(cargaC, text="Celular", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_celular.grid(row=9, column=0, sticky=W)
    e_celular = Entry(cargaC,font=font, width=25)
    e_celular.grid(row=10, column=0,padx=15, sticky=W,rowspan=1)
    l_fijo = Label(cargaC, text="Fijo", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_fijo.grid(row=9, column=1, sticky=W,columnspan=3)  
    e_fijo = Entry(cargaC,font=font, width=20)
    e_fijo.grid(row=10, column=1, sticky=W,rowspan=1,columnspan=3)
    
    # face/insta
    l_facebook = Label(cargaC, text="Facebook", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_facebook.grid(row=11, column=0, sticky=W)
    e_facebook = Entry(cargaC,font=font, width=25)
    e_facebook.grid(row=12, column=0,padx=15, sticky=W,rowspan=1)
    l_instagram = Label(cargaC, text="Instagram", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_instagram.grid(row=11, column=1, sticky=W,columnspan=3)  
    e_instagram = Entry(cargaC,font=font, width=20)
    e_instagram.grid(row=12, column=1, sticky=W,rowspan=1,columnspan=3)
def aceptarCallback():
    pass

def cancelarCallback():
    pass

def buttons(cargaC):
    line = Label(cargaC, text="-------------------------------------------------------------------------------------------------------------")
    line.grid(row=13,columnspan=3)
    aceptar = Button(cargaC, text="Aceptar", font="Arial 14",command=aceptarCallback, pady=12) 
    aceptar.grid(row=14, column=0, sticky=S,rowspan=1,columnspan=1)
    cancelar = Button(cargaC, text="Cancelar", font="Arial 14",command=cancelarCallback, pady=12) 
    cancelar.grid(row=14, column=1, sticky=S,rowspan=1,columnspan=1)   


def locate_window(width, height, widget):
    screen_width = widget.winfo_screenwidth()
    screen_height = widget.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    widget.geometry('%dx%d+%d+%d' % (width, height, x, y))




locate_window(600,600, cargaC)
labels(cargaC)
buttons(cargaC)
cargaC.mainloop()

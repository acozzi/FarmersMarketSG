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
    
    

    


def locate_window(width, height, widget):
    screen_width = widget.winfo_screenwidth()
    screen_height = widget.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    widget.geometry('%dx%d+%d+%d' % (width, height, x, y))




locate_window(600,600, cargaC)
labels(cargaC)
cargaC.mainloop()

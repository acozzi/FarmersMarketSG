from tkinter import *
from pymongo import MongoClient
import datetime

cargaC = Tk()
cargaC.title('Cargar Nuevo Cliente')


def cargarCliente():
    #cargaC = Tk()
    #cargaC.title('Cargar Nuevo Cliente')
    #locate_window(600,600, cargaC)
    #labels(cargaC)
    pass

def labels(cargaC, ):
    font = "Arial 14"
    l_titulo = Label(cargaC, text="Alta de Nuevo Cliente", font="Arial 14 bold", padx=15, pady=15, width="30", height="1",anchor=W)
    l_titulo.grid(row=0, columnspan=2, column=0,sticky=W)
    l_nombre = Label(cargaC, text="Nombre", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_nombre.grid(row=1, column=0, sticky=W)
    e_nombre = Entry(cargaC,font=font, width=15, textvariable=nombre)
    e_nombre.grid(row=2, column=0,padx=15, sticky=W,rowspan=1)

    l_apellido = Label(cargaC, text="Apellido", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_apellido.grid(row=1, column=1, sticky=W,columnspan=3)  
    e_apellido = Entry(cargaC,font=font, width=20, textvariable=apellido)
    e_apellido.grid(row=2, column=1, sticky=W,rowspan=1,columnspan=3)

    l_email = Label(cargaC, text="Email", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_email.grid(row=3, column=0, sticky=W)
    e_mail = Entry(cargaC,font=font, width=25, textvariable=email)
    e_mail.grid(row=4, column=0,padx=15, sticky=W,rowspan=1)

    l_calle = Label(cargaC, text="Calle", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_calle.grid(row=5, column=0, sticky=W)
    e_calle = Entry(cargaC,font=font, width=25, textvariable=calle)
    e_calle.grid(row=6, column=0,padx=15, sticky=W,rowspan=1)
    l_altura = Label(cargaC, text="Altura", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_altura.grid(row=5, column=1, sticky=W)  
    e_altura = Entry(cargaC,font=font, width=5, textvariable=altura)
    e_altura.grid(row=6, column=1, sticky=W,rowspan=1)
    l_pisoDepto = Label(cargaC, text="Piso/Depto/Torre", font=font, padx=1, pady=7, width=15, height=1,anchor=W)
    l_pisoDepto.grid(row=5, column=2, sticky=W)  
    e_pisoDepto = Entry(cargaC,font=font, width=15, textvariable=pisoDepto)
    e_pisoDepto.grid(row=6, column=2, sticky=W,rowspan=1)

    # CP Localidad Zona
    l_localidad = Label(cargaC, text="Localidad", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_localidad.grid(row=7, column=0, sticky=W)
    e_localidad = Entry(cargaC,font=font, width=25, textvariable=localidad)
    e_localidad.grid(row=8, column=0,padx=15, sticky=W,rowspan=1)
    l_cp = Label(cargaC, text="CP", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_cp.grid(row=7, column=1, sticky=W)  
    e_cp = Entry(cargaC,font=font, width=5, textvariable=cp)
    e_cp.grid(row=8, column=1, sticky=W,rowspan=1)
    l_zona = Label(cargaC, text="Zona", font=font, padx=1, pady=7, width=5, height=1,anchor=W)
    l_zona.grid(row=7, column=2, sticky=W)  
    e_zona = Entry(cargaC,font=font, width=5, textvariable=zona)
    e_zona.grid(row=8, column=2, sticky=W,rowspan=1)

    # Celular/fijo
    l_celular = Label(cargaC, text="Celular", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_celular.grid(row=9, column=0, sticky=W)
    e_celular = Entry(cargaC,font=font, width=25, textvariable=celular)
    e_celular.grid(row=10, column=0,padx=15, sticky=W,rowspan=1)
    l_fijo = Label(cargaC, text="Fijo", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_fijo.grid(row=9, column=1, sticky=W,columnspan=3)  
    e_fijo = Entry(cargaC,font=font, width=20, textvariable=fijo)
    e_fijo.grid(row=10, column=1, sticky=W,rowspan=1,columnspan=3)
    
    # face/insta
    l_facebook = Label(cargaC, text="Facebook", font=font, padx=15, pady=7, width=15, height=1,anchor=W)
    l_facebook.grid(row=11, column=0, sticky=W)
    e_facebook = Entry(cargaC,font=font, width=25, textvariable=facebook)
    e_facebook.grid(row=12, column=0,padx=15, sticky=W,rowspan=1)
    l_instagram = Label(cargaC, text="Instagram", font=font, padx=1, pady=7, width=8, height=1,anchor=W)
    l_instagram.grid(row=11, column=1, sticky=W,columnspan=3)  
    e_instagram = Entry(cargaC,font=font, width=20, textvariable=instagram)
    e_instagram.grid(row=12, column=1, sticky=W,rowspan=1,columnspan=3)
    line = Label(cargaC, text="-------------------------------------------------------------------------------------------------------------")
    line.grid(row=13,columnspan=3)
    aceptar = Button(cargaC, text="Aceptar", font="Arial 14",command=aceptarCallback, pady=12) 
    aceptar.grid(row=14, column=0, sticky=S,rowspan=1,columnspan=1)
    cancelar = Button(cargaC, text="Cancelar", font="Arial 14",command=cargaC.quit, pady=12) 
    cancelar.grid(row=14, column=1, sticky=S,rowspan=1,columnspan=1)  


def aceptarCallback():
    document = {
        "nombre": nombre.get(),
        "apellido": apellido.get(),
        "email": email.get(),
        "direccion" : {
            "calle": calle.get(),
            "altura": int(altura.get()),
            "pisoDepto": pisoDepto.get(),
            "localidad": localidad.get(),
            "cp": int(cp.get()),
            "zona": int(zona.get())
        },
        "telefono":{
            "celular": int(celular.get()),
            "fijo": int(fijo.get())
        },    
        "redes":{
            "facebook": facebook.get(),
            "instagram": instagram.get()
        }    
    }
    client = MongoClient('mongodb+srv://acozzi:aw96b6@farmersmarket-tu1em.gcp.mongodb.net/farmersMarket?retryWrites=true&w=majority')
    db = client['sg'] # <class 'pymongo.database.Database'>
    clientes = db.clientes # <class 'pymongo.collection.Collection'>
    post_id = clientes.insert_one(document).inserted_id
    print(post_id)

def cancelarCallback():
    pass
    #ver quits


def locate_window(width, height, widget):
    screen_width = widget.winfo_screenwidth()
    screen_height = widget.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    widget.geometry('%dx%d+%d+%d' % (width, height, x, y))



nombre = StringVar()
apellido = StringVar()
email = StringVar()
calle = StringVar()
altura = StringVar()
pisoDepto = StringVar()
localidad = StringVar()
cp = StringVar()
zona = StringVar()
celular = StringVar()
fijo = StringVar()
facebook = StringVar()
instagram = StringVar()


locate_window(600,600, cargaC)
labels(cargaC)


cargaC.mainloop()

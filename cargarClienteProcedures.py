from tkinter import *
from pymongo import MongoClient
import datetime
from tkinter import ttk
import files.tkObjects as tko
cargaC = Tk()
cargaC.title('Cargar Nuevo Cliente')


def cargarCliente():
    #cargaC = Tk()
    #cargaC.title('Cargar Nuevo Cliente')
    #locate_window(600,600, cargaC)
    #labels(cargaC)
    pass

def labels(cargaC,):
    row = 0
    font = "Arial 12"
    padx = 15
    pady = 7
    width = 15
    height = 1
    texts = ["Alta de Nuevo Cliente","Nombre", "Email", "calle", "localidad", "Facebook", "Celular","Apellido", "Altura", "Piso/Depto/Torre", "CP", "Zona", "Fijo", "Instagram"]
    
    l_titulo = Label(cargaC, text=texts[0], font="Arial 14 bold", padx=padx, pady=15, width="30", height="1",anchor=W)
    l_nombre = tko.createLabels(cargaC, texts[1], font, padx, pady, width, height)
    l_email = tko.createLabels(cargaC, texts[2], font, padx, pady, width, height)
    l_calle = tko.createLabels(cargaC, texts[3], font, padx, pady, width, height)
    l_localidad = tko.createLabels(cargaC, texts[4], font, padx, pady, width, height)
    l_facebook = tko.createLabels(cargaC, texts[5], font, padx, pady, width, height)
    l_celular = tko.createLabels(cargaC, texts[6], font, padx, pady, width, height)
    l_apellido = tko.createLabels(cargaC, texts[7], font, 1, 7, 8, 1)
    l_altura = tko.createLabels(cargaC, texts[8], font, 1, 7, 5, 1)
    l_pisoDepto = tko.createLabels(cargaC, texts[9], font, 1, 7, 15, 1)
    l_cp = tko.createLabels(cargaC, texts[10], font, 1, 7, 5, 1)
    l_zona = tko.createLabels(cargaC, texts[11], font, 1, 7, 5, 1)
    l_fijo = tko.createLabels(cargaC, texts[12], font, 1, 7, 8, 1)    
    l_instagram = tko.createLabels(cargaC, texts[13], font, 1, 7, 8, 1)
    

    e_nombre = tko.createEntrys(cargaC,font, 15, nombre)
    e_apellido = tko.createEntrys(cargaC,font, 20, apellido)    
    e_mail = tko.createEntrys(cargaC,font, 25, email)
    e_calle = tko.createEntrys(cargaC, font, 25, calle)
    e_altura = tko.createEntrys(cargaC, font, 5, altura)
    e_pisoDepto = tko.createEntrys(cargaC,font, 15, pisoDepto)
    e_localidad = tko.createEntrys(cargaC,font, 25, localidad) 
    e_cp = tko.createEntrys(cargaC,font, 5, cp) 
    e_zona = tko.createEntrys(cargaC,font, 5, zona)
    e_celular = tko.createEntrys(cargaC,font, 25, celular)
    e_fijo = tko.createEntrys(cargaC,font, 20, fijo)
    e_facebook = tko.createEntrys(cargaC,font, 25, facebook)
    e_instagram = tko.createEntrys(cargaC,font, 20, instagram)


    l_titulo.grid(row=row, columnspan=2, column=0,sticky=W)
    row += 1
    l_nombre.grid(row=row, column=0, sticky=W)
    l_apellido.grid(row=row, column=1, sticky=W, columnspan=3)
    row += 1
    e_nombre.grid(row=row, column=0, padx=15, sticky=W, rowspan=1)
    e_apellido.grid(row=row, column=1, sticky=W, rowspan=1, columnspan=3)
    
    row += 2  # salto la 3 para el view
    verDatos = ttk.Treeview(columns=2, height=1)
    verDatos["columns"] = ("nombre", "direccion")
    verDatos.column("#0", width=130, anchor=W)
    #verDatos.column("id", width=130, anchor=W)
    verDatos.column("nombre", width=250, anchor=W)
    verDatos.column("direccion", width=150, anchor=W)
    verDatos.grid(column=0, pady=10, padx=15, row=3, columnspan=4)

    
    l_email.grid(row=row, column=0, sticky=W)
    row += 1
    e_mail.grid(row=row, column=0, padx=15, sticky=W, rowspan=1)
    row += 1
    l_calle.grid(row=row, column=0, sticky=W)
    l_altura.grid(row=row, column=1, sticky=W)  
    l_pisoDepto.grid(row=row, column=2, sticky=W)    
    row += 1
    e_calle.grid(row=row, column=0, padx=15, sticky=W, rowspan=1)     
    e_altura.grid(row=row, column=1, sticky=W, rowspan=1)
    e_pisoDepto.grid(row=row, column=2, sticky=W,rowspan=1) 
    row += 1
    l_localidad.grid(row=row, column=0, sticky=W)
    l_cp.grid(row=row, column=1, sticky=W)
    l_zona.grid(row=row, column=2, sticky=W)
    row += 1
    e_localidad.grid(row=row, column=0, padx=15, sticky=W, rowspan=1)
    e_cp.grid(row=row, column=1, sticky=W,rowspan=1)
    e_zona.grid(row=row, column=2, sticky=W, rowspan=1)
    row += 1
    l_celular.grid(row=row, column=0, sticky=W)
    l_fijo.grid(row=row, column=1, sticky=W,columnspan=3)  
    row += 1
    e_celular.grid(row=row, column=0,padx=15, sticky=W,rowspan=1)
    e_fijo.grid(row=row, column=1, sticky=W, rowspan=1, columnspan=3)
    row += 1
    l_facebook.grid(row=row, column=0, sticky=W)
    l_instagram.grid(row=row, column=1, sticky=W,columnspan=3) 
    row += 1
    e_facebook.grid(row=row, column=0,padx=15, sticky=W,rowspan=1)  
    e_instagram.grid(row=row, column=1, sticky=W, rowspan=1, columnspan=3)
    row += 1
    line = Label(cargaC, text="-------------------------------------------------------------------------------------------------------------")
    line.grid(row=row, columnspan=3)
    row += 1
    aceptar = Button(cargaC, text="Aceptar", font="Arial 14",command=aceptarCallback, pady=12) 
    aceptar.grid(row=row, column=0, sticky=S, rowspan=1,columnspan=1)
    cancelar = Button(cargaC, text="Cancelar", font="Arial 14",command=cargaC.quit, pady=12) 
    cancelar.grid(row=row, column=1, sticky=S,rowspan=1,columnspan=1)  


def aceptarCallback():
    document = {
        "nombre": nombre.get(),
        "apellido": apellido.get(),
        "email": email.get(),
        "direccion" : {
            "calle": calle.get(),
            "altura": altura.get(),
            "pisoDepto": pisoDepto.get(),
            "localidad": localidad.get(),
            "cp": cp.get(),
            "zona": zona.get()
        },
        "telefono":{
            "celular": celular.get(),
            "fijo": fijo.get()
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
altura = IntVar()
pisoDepto = StringVar()
localidad = StringVar()
cp = IntVar()
zona = StringVar()
celular = IntVar()
fijo = IntVar()
facebook = StringVar()
instagram = StringVar()

nombre.set(' ')
apellido.set(' ')
email.set(' ')
calle.set(' ')
altura.set(0)
pisoDepto.set(' ')
localidad.set(' ')
cp.set(0)
zona.set(' ')
celular.set(0)
fijo.set(0)
facebook.set(' ')
instagram.set(' ')




locate_window(600,600, cargaC)
labels(cargaC)


cargaC.mainloop()

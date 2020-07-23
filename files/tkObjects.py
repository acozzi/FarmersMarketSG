from tkinter import *
from tkinter import ttk

def createLabels(widget,texto,fuente,padX,padY,width,height):
    label = Label(widget, text=texto, font=fuente, padx=padX, pady=padY, width=width, height=height, anchor=W)
    return label

def createEntrys(widget, font, width, textvariable):
    entry = Entry(widget, font=font, width=width, textvariable=textvariable)
    return entry

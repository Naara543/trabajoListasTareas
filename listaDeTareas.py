import tkinter 
from tkinter import ttk
from datetime import datetime



def agregar():
    today = datetime.today()
    fecha = f"{today.day}/{today.month}]/{today.year}"
    treeview.insert("", tkinter.END, text= texto.get(), values=(fecha, False))
    texto.delete(0, tkinter.END)


#def listar():

def borrar():
    selec = treeview.selection()
    if selec:
        for i in selec:
            treeview.delete()

            
main_window = tkinter.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("fecha", "completada"))
treeview.heading("#0", text="tarea")
treeview.heading("fecha", text="fecha")
treeview.heading("completada", text="Fecha")
treeview.pack()


  
boton_agrega = tkinter.Button(main_window, bg= "green", text="Agregar", command = agregar)
#listar_btn = tkinter.Button(main_window, bg= "green", text="Listar", command = listar)
boton_borrar = tkinter.Button(main_window, bg= "red", text="Borrar", command = borrar)
cuadrito = tkinter.Entry(main_window)


cuadrito.pack()
boton_agrega.pack()
#listar_btn.pack()
boton_borrar.pack()
main_window.mainloop()

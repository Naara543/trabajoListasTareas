import tkinter
from tkinter import ttk, messagebox
from datetime import datetime

#funcion Agregar usando metodo insert()
def agregar():
    today = datetime.today()
    fecha = f"{today.day}/{today.month}/{today.year}"
    treeview.insert("", tkinter.END, text=texto.get(), values=(fecha, False))
    texto.delete(0, tkinter.END)

def tareaCompletada():
    tareaSeleccionada = treeview.selection()
    if tareaSeleccionada:
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de completar esta tarea?")
        if confirmar:
            for i in tareaSeleccionada:
                treeview.item(i, values=(treeview.item(i)['values'][0], True))
#funcion Borrar
def borrar():
    selec = treeview.selection()
    if selec:
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de borrar esta tarea?")
        if confirmar:
            for i in selec:
                treeview.delete(i)

def salir():
    confirmar = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
    if confirmar:
        main_window.destroy()

main_window = tkinter.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("fecha", "completada"))
treeview.heading("#0", text="Tarea")
treeview.heading("fecha", text="Fecha")
treeview.heading("completada", text="Completada")
treeview.pack()

# Crear un Frame para contener los botones
botones_frame = tkinter.Frame(main_window)
botones_frame.pack()

# Colocar los botones en el Frame
boton_agrega = tkinter.Button(botones_frame, bg="green", text="Agregar", command=agregar)
boton_completar = tkinter.Button(botones_frame, bg="lightblue", text="Completar", command=tareaCompletada)
boton_borrar = tkinter.Button(botones_frame, bg="red", text="Borrar", command=borrar)
boton_salir = tkinter.Button(botones_frame, bg="yellow", text="Salir", command=salir)

# Organizar los botones en forma horizontal usando grid
boton_agrega.grid(row=0, column=0, padx=5)
boton_completar.grid(row=0, column=1, padx=5)
boton_borrar.grid(row=0, column=2, padx=5)
boton_salir.grid(row=0, column=3, padx=5)

texto = tkinter.Entry(main_window)
texto.pack()

main_window.mainloop()

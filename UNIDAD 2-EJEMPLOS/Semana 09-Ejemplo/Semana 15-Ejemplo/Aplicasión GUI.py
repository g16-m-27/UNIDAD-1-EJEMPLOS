import tkinter as tk
from tkinter import messagebox

#ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Lista interna de tareas
tareas = []

# ---------------- FUNCIONES ----------------

def añadir_tarea(event=None):
    tarea = entrada.get()
    if tarea != "":
        tareas.append({"texto": tarea, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea")

def marcar_completada():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()

def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

def doble_click(event):
    marcar_completada()

def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        if tarea["completada"]:
            lista.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista.insert(tk.END, tarea["texto"])

# ---------------- INTERFAZ ----------------

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Evento Enter
entrada.bind("<Return>", añadir_tarea)

# Botones
btn_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Evento doble clic
lista.bind("<Double-Button-1>", doble_click)

# Ejecutar app
ventana.mainloop()
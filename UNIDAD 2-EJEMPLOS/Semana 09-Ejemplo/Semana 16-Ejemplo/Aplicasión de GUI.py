import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Lista para guardar tareas
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea, completada in tareas:
        if completada:
            lista.insert(tk.END, f"✔ {tarea}")
            lista.itemconfig(tk.END, fg="green")
        else:
            lista.insert(tk.END, f"✗ {tarea}")
            lista.itemconfig(tk.END, fg="black")

# Añadir tarea
def añadir_tarea(event=None):
    texto = entrada.get()
    if texto != "":
        tareas.append((texto, False))
        entrada.delete(0, tk.END)
        actualizar_lista()

# Marcar como completada
def completar_tarea(event=None):
    try:
        index = lista.curselection()[0]
        tarea, _ = tareas[index]
        tareas[index] = (tarea, True)
        actualizar_lista()
    except:
        pass

# Eliminar tarea
def eliminar_tarea(event=None):
    try:
        index = lista.curselection()[0]
        tareas.pop(index)
        actualizar_lista()
    except:
        pass

# Interfaz gráfica
entrada = tk.Entry(root, width=40)
entrada.pack(pady=10)

lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=10)

# Botones
btn_añadir = tk.Button(root, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack()

btn_completar = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack()

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# ATAJOS DE TECLADO
root.bind("<Return>", añadir_tarea)     # Enter para añadir
root.bind("c", completar_tarea)        # tecla C para completar
root.bind("d", eliminar_tarea)         # tecla D para eliminar
root.bind("<Delete>", eliminar_tarea)  # Delete para eliminar
root.bind("<Escape>", lambda e: root.quit())  # Escape para salir

# Ejecutar aplicación
root.mainloop()
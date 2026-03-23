#Nombre:Zhune Zuleyka
#POO

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- FUNCIONES ---------------- #

def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    desc = entrada_desc.get()

    if fecha == "" or hora == "" or desc == "":
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    tabla.insert("", "end", values=(fecha, hora, desc))

    # Limpiar campos
    entrada_fecha.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)
    entrada_desc.delete(0, tk.END)


def eliminar_evento():
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar este evento?")
    if confirmar:
        tabla.delete(seleccionado)


# ---------------- VENTANA ---------------- #

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("700x450")
ventana.config(bg="#f0f0f0")

# ---------------- FRAME TABLA ---------------- #

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

tabla = ttk.Treeview(frame_tabla, columns=("Fecha", "Hora", "Descripcion"), show="headings", height=8)

tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripcion", text="Descripción")

tabla.column("Fecha", width=100)
tabla.column("Hora", width=100)
tabla.column("Descripcion", width=300)

tabla.pack()

# ---------------- FRAME ENTRADA ---------------- #

frame_entrada = tk.Frame(ventana, bg="#f0f0f0")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
entrada_fecha = tk.Entry(frame_entrada)
entrada_fecha.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Hora (hh:mm):", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=5)

tk.Label(frame_entrada, text="Descripción:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
entrada_desc = tk.Entry(frame_entrada, width=30)
entrada_desc.grid(row=2, column=1, padx=5)

# ---------------- FRAME BOTONES ---------------- #

frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=15)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="#4CAF50", fg="white")
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento, bg="#f44336", fg="white")
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=10)

# ---------------- EJECUCIÓN ---------------- #

ventana.mainloop()
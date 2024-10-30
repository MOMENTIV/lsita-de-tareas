import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser

# Funciones para manejar las tareas
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(tk.END, f"{tarea} - Completada")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcar como completada.")

def cambiar_color():
    try:
        indice = lista_tareas.curselection()[0]
        color = colorchooser.askcolor()[1]
        if color:
            lista_tareas.itemconfig(indice, {'fg': color})
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para cambiar su color.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x300")  # Dimensiones iniciales de la ventana

# colores para mantener la interfaz osucra
color_fondo = "#2b2b2b"
color_texto = "#ffffff"
color_boton = "#444444"
color_boton_texto = "#ffffff"

# Configurar fondo oscuro para la ventana
ventana.configure(bg=color_fondo)

# widgets con colores personalizados
entrada_tarea = tk.Entry(ventana, width=30, bg=color_fondo, fg=color_texto, insertbackground=color_texto)
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea, bg=color_boton, fg=color_boton_texto)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea, bg=color_boton, fg=color_boton_texto)
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada, bg=color_boton, fg=color_boton_texto)
boton_cambiar_color = tk.Button(ventana, text="Cambiar Color Tarea", command=cambiar_color, bg=color_boton, fg=color_boton_texto)
lista_tareas = tk.Listbox(ventana, width=50, height=10, bg=color_fondo, fg=color_texto, selectbackground="#666666")

# Organizar widgets
entrada_tarea.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
boton_agregar.grid(row=0, column=1, padx=10, pady=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
boton_eliminar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
boton_completar.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
boton_cambiar_color.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Configurar las columnas y filas para que se expandan
ventana.grid_columnconfigure(0, weight=1)  # La columna 0 se expande
ventana.grid_columnconfigure(1, weight=1)  # La columna 1 se expande
ventana.grid_rowconfigure(1, weight=1)     # La fila 1 (donde está la lista de tareas) se expande

# Iniciar el loop de la ventana
ventana.mainloop()

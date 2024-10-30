*Lista de Tareas
Esta es una aplicación de Lista de Tareas creada con Python y Tkinter. Permite a los usuarios agregar, eliminar, marcar como completadas y cambiar el color de las tareas para una mejor administración.

*Características
- Modo oscuro (noche) con letras blancas y botones claros.
- Posibilidad de cambiar el color de las tareas.
- Diseño adaptable a diferentes tamaños de ventana.
- Interfaz interactiva y basada en eventos.

*Instrucciones de uso
1. **Agregar Tarea**: Escribe una tarea en el campo de texto y presiona el botón "Agregar Tarea".
2. **Eliminar Tarea**: Selecciona una tarea de la lista y presiona "Eliminar Tarea".
3. **Marcar como Completada**: Selecciona una tarea y presiona "Marcar como Completada".
4. **Cambiar Color**: Selecciona una tarea y presiona "Cambiar Color" para asignar un color personalizado a cada tarea.

*Requerimientos
- Python 3.x
- Tkinter (incluido en la mayoría de las distribuciones de Python)
- PyInstaller (para generar ejecutables)

*Ejecutar la aplicación
Si deseas ejecutar la aplicación sin instalar nada adicional, simplemente abre el archivo ejecutable `Lista de Tareas.exe` en la carpeta `aplicacion`.

*Generar el ejecutable
Si prefieres generar el ejecutable por ti mismo, utiliza PyInstaller con el siguiente comando:

```bash
pyinstaller --onefile --windowed --name "Lista de Tareas" funciones.py

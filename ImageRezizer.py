from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def seleccionar_imagen():
    ruta_imagen = filedialog.askopenfilename()
    imagen_original = Image.open(ruta_imagen)
    imagen_tk = ImageTk.PhotoImage(imagen_original)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    seleccion_actual.set(ruta_imagen)
    ancho, alto = imagen_original.size
    cuadro_ancho.delete(0, END)
    cuadro_alto.delete(0, END)
    cuadro_ancho.insert(0, ancho)
    cuadro_alto.insert(0, alto)

def redimensionar_imagen():
    ancho = cuadro_ancho.get()
    alto = cuadro_alto.get()
    nueva_resolucion = ancho + 'x' + alto
    nuevo_ancho, nuevo_alto = nueva_resolucion.split('x')
    nuevo_ancho, nuevo_alto = int(nuevo_ancho), int(nuevo_alto)
    nuevo_tamaño = (nuevo_ancho, nuevo_alto)
    imagen_original = Image.open(seleccion_actual.get())
    imagen_redimensionada = imagen_original.resize(nuevo_tamaño)
    ruta_imagen = seleccion_actual.get()
    nombre_archivo, extension = ruta_imagen.split('.')
    nueva_ruta_imagen = nombre_archivo + '_redimensionada.' + extension
    imagen_redimensionada.save(nueva_ruta_imagen)
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    seleccion_actual.set(nueva_ruta_imagen)

ventana = Tk()
ventana.title('ImagenResizer By Matecitos')

seleccion_actual = StringVar()

boton_seleccionar = Button(ventana, text='Seleccionar Imagen', command=seleccionar_imagen, padx=10, pady=10)
boton_seleccionar.pack(pady=10)

etiqueta_ancho = Label(ventana, text='Ancho:')
etiqueta_ancho.pack()

cuadro_ancho = Entry(ventana, width=25)
cuadro_ancho.pack()

etiqueta_alto = Label(ventana, text='Alto:')
etiqueta_alto.pack()

cuadro_alto = Entry(ventana, width=25)
cuadro_alto.pack()

boton_redimensionar = Button(ventana, text='Redimensionar', command=redimensionar_imagen, padx=20, pady=20)
boton_redimensionar.pack(pady=10)

etiqueta_imagen = Label(ventana, pady=10)
etiqueta_imagen.pack()

ventana.geometry("300x300")
ventana.configure(padx=10, pady=10)
ventana.mainloop()
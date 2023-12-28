# Convertidor de diferentes unidades

# Version 1.0
# Autor: Zenxlk

# Definir menú

# 1. Longitud
# 2. Masa
# 3. Temperatura
# 4.Tiempo
# 5. Salir

# Importar librerias para interfaz grafica

from tkinter import *
from tkinter import messagebox


# Informacion

from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox

# Intro


def info():
    # Crear una nueva ventana para el mensaje de información
    info_ventana = Tk()
    info_ventana.title("")
    info_ventana.geometry("400x300")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 300
    pantalla_ancho = info_ventana.winfo_screenwidth()
    pantalla_alto = info_ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    info_ventana.geometry(
        f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

    # Crear un widget Label para mostrar el mensaje de información
    label = Label(
        info_ventana,
        text="Convertidor de unidades\n\n\nVersion: 1.0\n\n\nAutor: Zenxlk \n",
        fg="black",
        font=("Helvetica", 16),
        anchor="center",
        justify="center",
    )
    label.pack(expand=True)
    info_ventana.iconbitmap("img/icono.ico")

    # Programar la función menu() para que se ejecute después de 2000 milisegundos
    info_ventana.after(2000, lambda: [info_ventana.destroy(), menu()])

    # Ejecutar el bucle principal de Tkinter
    info_ventana.mainloop()


# Menu principal


def menu():
    # Ventana

    global ventana
    ventana = Tk()
    ventana.title("Convertidor de unidades")
    ventana.geometry("400x400")
    ventana.resizable(False, False)
    ventana.config(bg="black")
    ventana.iconbitmap("img/icono.ico")
    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Opciones

    opcion1 = Button(ventana, text="1. Longitud", command=convertir_longitud)
    opcion1.pack()
    opcion2 = Button(ventana, text="2. Masa", command=convertir_masa)
    opcion2.pack()
    opcion3 = Button(ventana, text="3. Temperatura",
                     command=convertir_temperatura)
    opcion3.pack()
    opcion4 = Button(ventana, text="4. Tiempo", command=convertir_tiempo)
    opcion4.pack()
    opcion5 = Button(ventana, text="5. Salir", command=ventana.quit)
    opcion5.pack()
    ventana.mainloop()


# Opciones


def convertir_longitud():
    global ventana
    ventana = Tk()
    ventana.title("1. Longitud")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Unidades de longitud
    unidades_longitud = ["Metro", "Kilómetro",
                         "Pulgada", "Pie", "Yarda", "Milla"]
    seleccion1 = StringVar(ventana)
    seleccion1.set(unidades_longitud[0])  # Posicion

    seleccion2 = StringVar(ventana)
    seleccion2.set(unidades_longitud[1])  # Posicion

    # Dropdown menus
    lista_desplegable1 = OptionMenu(ventana, seleccion1, *unidades_longitud)
    lista_desplegable1.pack()

    lista_desplegable2 = OptionMenu(ventana, seleccion2, *unidades_longitud)
    lista_desplegable2.pack()

    # Input field
    input_valor = Entry(ventana)
    input_valor.pack()

    # Conversion button
    def calcular_conversion():
        valor = float(input_valor.get())
        unidad_origen = seleccion1.get()
        unidad_destino = seleccion2.get()
        
        #Metro
        if unidad_origen == "Metro" and unidad_destino == "Metro":
            unidad_destino = valor
            unidad_destino = valor
            
            
    boton_calcular = Button(ventana, text="Calcular",
                            command=calcular_conversion)
    boton_calcular.pack()

    ventana.mainloop()


def convertir_masa():
    global ventana
    ventana = Tk()
    ventana.title("2. Masa")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Unidades de masa
    unidades_masa = ["Gramo", "Kilogramo", "Onza", "Libra", "Tonelada"]
    seleccion = StringVar(ventana)
    seleccion.set(unidades_masa[0])  # Posicion

    lista_desplegable = OptionMenu(ventana, seleccion, *unidades_masa)
    lista_desplegable.pack()

    ventana.mainloop()


def convertir_temperatura():
    global ventana
    ventana = Tk()
    ventana.title("3. Temperatura")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Unidades de temperatura

    unidades_temperatura = ["Celcius", "Farenheit"]
    seleccion = StringVar(ventana)
    seleccion.set(unidades_temperatura[0])  # Posicion

    lista_desplegable = OptionMenu(ventana, seleccion, *unidades_temperatura)
    lista_desplegable.pack()

    ventana.mainloop()


def convertir_tiempo():
    global ventana
    ventana = Tk()
    ventana.title("4. Tiempo")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Calcular la posición de la ventana para que se muestre en el centro de la pantalla
    ventana_ancho = 300
    ventana_alto = 200
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2

    # Posicionar la ventana en el centro de la pantalla
    ventana.geometry(f"{ventana_ancho}x{
                     ventana_alto}+{posicion_x}+{posicion_y}")

    # Unidades de tiempo
    unidades_tiempo = ["Años", "Meses", "Dias"]
    seleccion = StringVar(ventana)
    seleccion.set(unidades_tiempo[0])  # Posicion

    lista_desplegable = OptionMenu(ventana, seleccion, *unidades_tiempo)
    lista_desplegable.pack()

    ventana.mainloop()


# Llamar a la función menu para iniciar la interfaz gráfica
info()

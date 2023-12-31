# Autor: Zenxlk

# Definir menú

# 1. Longitud
# 2. Masa
# 3. Temperatura
# 4.Tiempo
# 5. Salir

# Importar librerias para interfaz grafica

from tkinter import *

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
    ventana_alto = 210
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

    # Seperador con label
    label = Label(
        ventana,
        text="a:",
        fg="black",
        font=("Helvetica", 10),
        anchor="center",
        justify="center",
    )
    label.pack()

    lista_desplegable2 = OptionMenu(ventana, seleccion2, *unidades_longitud)
    lista_desplegable2.pack()

    # Separador label
    label2 = Label(
        ventana,
        text=" "
    )

    label2.pack()
    label = Label(
        ventana,
        text="Ingrese cantidad a converetir:",
        fg="black",
        font=("Helvetica", 10),
        anchor="center",
        justify="center",
    )
    label.pack()

    # Input field
    input_valor = Entry(
        ventana,
        fg="black",
        borderwidth=2,
        relief="solid"
    )
    input_valor.pack()

    # Variable resultado
    resultado = 0

    # Conversion button
    def calcular_conversion():
        valor = float(input_valor.get())
        unidad_origen = seleccion1.get()
        unidad_destino = seleccion2.get()

        conversion_rates = {
            "Metro": 1,
            "Kilómetro": 1000,
            "Pulgada": 0.0254,
            "Pie": 0.3048,
            "Yarda": 0.9144,
            "Milla": 1609.34
        }

        if unidad_origen in conversion_rates and unidad_destino in conversion_rates:
            resultado = valor * \
                conversion_rates[unidad_origen] / \
                conversion_rates[unidad_destino]
            resultado_label.config(text=f"La conversión es: {
                                   resultado} {unidad_destino}s")
        else:
            resultado = 0
            print(f"Unidad de origen: {unidad_origen}, Unidad de destino: {
                  unidad_destino} el resultado es: {resultado} ")

    # Label de resultado
    resultado_label = Label(ventana, text="Ingrese datos...")
    resultado_label.pack()

    boton_calcular = Button(ventana, text="Calcular",
                            command=calcular_conversion)
    boton_calcular.pack()

    boton_calcular.config(command=calcular_conversion)

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
    seleccion1 = StringVar(ventana)
    seleccion1.set(unidades_masa[0])  # Posicion

    seleccion2 = StringVar(ventana)
    seleccion2.set(unidades_masa[0])  # Posicion

    lista_desplegable1 = OptionMenu(ventana, seleccion1, *unidades_masa)
    lista_desplegable1.pack()

    # Seperador con label
    label = Label(
        ventana,
        text="a:",
        fg="black",
        font=("Helvetica", 10),
        anchor="center",
        justify="center",
    )
    label.pack()

    lista_desplegable2 = OptionMenu(ventana, seleccion2, *unidades_masa)
    lista_desplegable2.pack()

    # Separador label
    label3 = Label(
        ventana,
        text=" "
    )
    label3.pack()

    # Separador label
    label2 = Label(
        ventana,
        text="Ingrese cantidad a convertir:"
    )
    label2.pack()

    input_valor = Entry(
        ventana,
        fg="black",
        borderwidth=2,
        relief="solid"
    )
    input_valor.pack()

    # Boton conversion
    def calcular_conversion():
        valor = float(input_valor.get())
        unidad_origen = seleccion1.get()
        unidad_destino = seleccion2.get()

        conversion_rates = {
            "Gramo": 1,
            "Kilogramo": 1000,
            "Onza": 28.3495,
            "Libra": 453.592,
            "Tonelada": 1000000
        }

        if unidad_origen in conversion_rates and unidad_destino in conversion_rates:
            resultado = valor * \
                conversion_rates[unidad_origen] / \
                conversion_rates[unidad_destino]
        else:
            resultado = 0
            print(f"Unidad de origen: {unidad_origen}, Unidad de destino: {
                  unidad_destino} el resultado es: {resultado}")

        resultado_label.config(text=f"La conversión es: {
                               resultado} {unidad_destino}s")

    # Label de resultado
    resultado_label = Label(ventana, text="Ingrese datos...")
    resultado_label.pack()

    boton_calcular = Button(ventana, text="Calcular",
                            command=calcular_conversion)
    boton_calcular.pack()

    boton_calcular.config(command=calcular_conversion)

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

    # Unidades de temperatura}
    unidades_temperatura = ["Celsius", "Fahrenheit", "Kelvin"]
    seleccion1 = StringVar(ventana)
    seleccion1.set(unidades_temperatura[0])  # Posicion

    seleccion2 = StringVar(ventana)
    seleccion2.set(unidades_temperatura[0])  # Posicion

    lista_desplegable1 = OptionMenu(ventana, seleccion, *unidades_temperatura)
    lista_desplegable1.pack()

    # Seperador con label
    label = Label(
        ventana,
        text="a:",
        fg="black",
        font=("Helvetica", 10),
        anchor="center",
        justify="center",
    )
    label.pack()

    lista_desplegable2 = OptionMenu(ventana, seleccion, *unidades_temperatura)
    lista_desplegable2.pack()

    # Separador label
    label2 = Label(
        ventana,
        text=" "
    )
    label2.pack()

    # Separador label
    label2 = Label(
        ventana,
        text="Ingrese cantidad a convertir:"
    )
    label2.pack()

    input_valor = Entry(
        ventana,
        fg="black",
        borderwidth=2,
        relief="solid"
    )
    input_valor.pack()

    # Boton conversion
    def calcular_conversion():
        valor = float(input_valor.get())
        unidad_origen = seleccion1.get()
        unidad_destino = seleccion2.get()

        conversion_rates = {
            "Celsius": 1,
            "Fahrenheit": 1.8,
            "Kelvin": 1
        }

        if unidad_origen in conversion_rates and unidad_destino in conversion_rates:
            resultado = valor * \
                conversion_rates[unidad_origen] / \
                conversion_rates[unidad_destino]
        else:
            resultado = 0
            print(f"Unidad de origen: {unidad_origen}, Unidad de destino: {
                  unidad_destino} el resultado es: {resultado}")

        resultado_label.config(text=f"La conversión es: {
                               resultado} {unidad_destino}s")

    # Label de resultado
    resultado_label = Label(ventana, text="Ingrese datos...")
    resultado_label.pack()

    boton_calcular = Button(ventana, text="Calcular",
                            command=calcular_conversion)
    boton_calcular.pack()

    boton_calcular.config(command=calcular_conversion)

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
    unidades_tiempo = ["Segundo", "Minuto",
                       "Hora", "Día", "Semana", "Mes", "Año"]
    seleccion1 = StringVar(ventana)
    seleccion1.set(unidades_tiempo[0])  # Posicion

    seleccion2 = StringVar(ventana)
    seleccion2.set(unidades_tiempo[0])  # Posicion

    lista_desplegable1 = OptionMenu(ventana, seleccion1, *unidades_tiempo)
    lista_desplegable1.pack()

    # Seperador con label
    label = Label(
        ventana,
        text="a:",
        fg="black",
        font=("Helvetica", 10),
        anchor="center",
        justify="center",
    )
    label.pack()

    lista_desplegable2 = OptionMenu(ventana, seleccion2, *unidades_tiempo)
    lista_desplegable2.pack()

    # Separador label
    label2 = Label(
        ventana,
        text=" "
    )
    label2.pack()

    # Separador label
    label2 = Label(
        ventana,
        text="Ingrese cantidad a convertir:"
    )
    label2.pack()

    input_valor = Entry(
        ventana,
        fg="black",
        borderwidth=2,
        relief="solid"
    )
    input_valor.pack()

    # Boton conversion
    def calcular_conversion():
        valor = float(input_valor.get())
        unidad_origen = seleccion1.get()
        unidad_destino = seleccion2.get()

        conversion_rates = {
            "Segundo": 1,
            "Minuto": 60,
            "Hora": 3600,
            "Día": 86400,
            "Semana": 604800,
            "Mes": 2629800,
            "Año": 31557600
        }

        if unidad_origen in conversion_rates and unidad_destino in conversion_rates:
            resultado = valor * \
                conversion_rates[unidad_origen] / \
                conversion_rates[unidad_destino]
        else:
            resultado = 0
            print(f"Unidad de origen: {unidad_origen}, Unidad de destino: {
                  unidad_destino} el resultado es: {resultado}")

        resultado_label.config(text=f"La conversión es: {
                               resultado} {unidad_destino}s")

    # Label de resultado
    resultado_label = Label(ventana, text="Ingrese datos...")
    resultado_label.pack()

    boton_calcular = Button(ventana, text="Calcular",
                            command=calcular_conversion)
    boton_calcular.pack()

    boton_calcular.config(command=calcular_conversion)

    ventana.mainloop()


# Llamar a la función menu para iniciar la interfaz gráfica
info()

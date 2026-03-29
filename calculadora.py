import tkinter as tk

# Crear la ventana principal

ventana = tk.Tk()
ventana.title("Mi Calculadora")

#Cambiar icono de la app
#ruta_icono = "C:\Users\user\Pictures"
ventana.iconbitmap("calculadora.ico")

#Una variable para almacenar la expresion matematica
expresion = ""

#Variable para almacenar el estado del visor
resultados_mostrado = False

#Funcion para actualizar la expresion en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultados_mostrado
     #Evaluar si ya se ha calculado y mostrado un resultado
    if resultados_mostrado:
        #Evaluar si se presiono un int o ".", reiniciar el visor
        if tecla.isdigit() or tecla == ".":
            expresion = str(tecla)
        else:
            expresion += str(tecla)
        resultados_mostrado = False
    else: 
        expresion += str(tecla)            
    visor_texto.set(expresion)

#Funcion para limpiar la entrada

def limpiar():
    global expresion, resultados_mostrado

    expresion = ""
    visor_texto.set(expresion)
    resultados_mostrado = False    

#Funcion para evaluar la expresion y mostrar el resultado

def evaluar():
    global expresion, resultados_mostrado

    try:
        resultado = eval(expresion)
        #Verificar si el resultado es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultados_mostrado = True
    except:
        visor_texto.set("Error")
        expresion = ""
        resultados_mostrado = False        



#Configurar el tamaño dinamico de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

"Cuadro de texto para mostrar las expresiones y resultados"
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 35, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief="sunken",
                 bg="#e8f0fe",
                 fg="#333333")
visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky="ew",
           padx=10,
           pady=10)

#Botones de calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('c', 4, 2), ('+', 4, 3),
]

# Colores almacenados en variables

color_fondo = "#0B0F1A"              # negro azulado profundo
color_fondo_secundario = "#1A1F38"  # panel elegante

color_botones_numeros = "#F9C80E"   # 🟡 amarillo vibrante (protagonista)
color_botones_operadores = "#FF006E" # 🌈 rosado neón
color_boton_igual = "#00F5D4"       # 💎 verde aqua brillante
color_boton_borrar = "#FF2E63"      # 🔴 rojo intenso moderno

color_texto_principal = "#0B0F1A"   # negro para contraste en botones claros
color_texto_secundario = "#FFFFFF"  # blanco limpio

color_hover = "#8338EC"             # 🟣 morado eléctrico (hover)
color_bordes = "#3A86FF"            # 🔵 azul eléctrico


#Crear y posicionar los botones ("Excepto "="")
for (texto, fila, columna) in botones: 
    if texto in ['/', '*', '-', '+']:
        comando = lambda x=texto: pulsar_tecla(x)
        bg_color = color_botones_operadores
        fg_color = color_texto_secundario

    elif texto == 'c':
        comando = limpiar
        bg_color = color_boton_borrar
        fg_color = color_texto_secundario

    elif texto == '=':
        comando = lambda x=texto: pulsar_tecla(x)
        bg_color = color_boton_igual
        fg_color = color_texto_principal

    else: 
        comando = lambda x=texto: pulsar_tecla(x)
        bg_color = color_botones_numeros   # 🟡 Amarillo para números
        fg_color = color_texto_principal   # Negro para que resalte

    tk.Button(
        ventana,
        text=texto,
        padx=20,
        pady=20,
        font=('Helvetica', 20, 'bold'),
        command=comando,
        bd=2,
        relief="raised",
        bg=bg_color,
        fg=fg_color,
        activebackground=color_hover,
        activeforeground="#FFFFFF"
    ).grid(
        row=fila,
        column=columna,
        sticky='nsew',
        padx=3,
        pady=3
    )
# Boton de igual "=" que ocupa toda la ultima fila
tk.Button(ventana,
              text="=",
              padx=20,
              pady=20,
              font=('Helvetica', 40, 'bold'),
              command=evaluar,
              bd=1,
              relief="raised",
              bg= color_boton_igual,
              fg=color_fondo_secundario,
              activeforeground=color_hover,
              activebackground=color_texto_principal
              ).grid(row=5,
                    column=0,
                    columnspan=4,
                    sticky='ew',
                    padx=3,
                    pady=3) 
# Ejecutar la aplicación
ventana.mainloop()

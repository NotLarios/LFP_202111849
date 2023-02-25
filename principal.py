import colorama
from colorama import Fore

import tkinter as tk
from tkinter import filedialog

import os

datos = []
diccionario = {} 
pelicula = []
file_path = ""
year = ""

def menuInicio():
    print(Fore.LIGHTBLUE_EX + """

         ____________________BIENVENIDO_____________________
        |                                                   |
        |          Lenguajes Formales de Programación       |
        |                                                   |
        |                    Sección B-                     |
        |                                                   |
        |                 Carnet 202111849                  |
        |                                                   |
        |            Sergio Andrés Larios Fajardo           |
        |___________________________________________________|

    """)

    askInputMenuInicio()

def menuPrincipal():
    print(Fore.LIGHTBLUE_EX + """

         __________________MENÚ PRINCIPAL___________________
        |                                                   |
        |   1.        Cargar Archivo de Entrada             |
        |                                                   |
        |   2.           Gestionar Películas                |
        |                                                   |
        |   3.                Filtrado                      |
        |                                                   |
        |   4.                Gráfica                       |
        |                                                   |
        |   5.                 Salir                        |
        |___________________________________________________|

    """)

    askInputMenuPrincipal()

def askInputMenuInicio():
    a = input(Fore.LIGHTCYAN_EX + "Presione Enter para ir al Menú Principal \n")
    if a == "":
        menuPrincipal()
    else:
        menuPrincipal()

def askInputMenuPrincipal():
    a = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")

    if a == "1":
        print(Fore.GREEN + "Se ha abierto una ventana para que seleccione el archivo \n")
        cargarArchivos()
    elif a == "2":
        gestionarPelículas()
    elif a == "3":
        filtrado()
    elif a == "4":
        grafica()
    elif a == "5":
        exit()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputMenuPrincipal()

def askInputGestionarPeliculas():
    a = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")
    if a == "1":
        gestionarPeliculas_mostrarPeliculas()
    elif a == "2":
        gestionarPeliculas_mostrarActores()
    elif a == "3":
        menuPrincipal()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputGestionarPeliculas

def askInputFiltrado():
    a = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")
    if a == "1":
        askInputActor()
    elif a == "2":
        askInputFiltradoAnio()
    elif a == "3":
        filtradoGenero()
    elif a == "4":
        menuPrincipal()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputFiltrado()
         
def cargarArchivos():
    
    try:
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(title="Selecciona un documento", filetypes=[("Documentos tipo LFP", ".lfp")])
        
        user = open(file_path, 'r')
        lineas = user.readlines()
        for i in user.read().split("\n"):
            for linea in lineas:
                linea = linea.strip().split(';')
                
                diccionario = {
                    linea[i]: linea[i+1] for i in range(0, len(linea), 2)
                }
                datos.append(diccionario)
        print(Fore.GREEN + "Archivo cargado exitosamente \n")
    except Exception as e:
        print(e)
        menuPrincipal()
    finally:
        user.close()

    askInputMenuInicio()

def cargarArchivosAnio():
    
    try:
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(title="Selecciona un documento", filetypes=[("Documentos tipo LFP", ".lfp")])
        
        user = open(file_path, 'r')
        lineas = user.readlines()
        for i in user.read().split("\n"):
            for linea in lineas:
                linea = linea.strip().split(';')
                
                diccionario = {
                    linea[i]: linea[i+1] for i in range(0, len(linea), 2)
                }
                datos.append(diccionario)
        print(Fore.GREEN + "Archivo cargado exitosamente \n")
    except Exception as e:
        print(e)
        menuPrincipal()
    finally:
        user.close()

def gestionarPelículas():
    print(Fore.LIGHTBLUE_EX + """
    
         _______________GESTIÓN DE PELÍCULAS________________
        |                                                   |
        |   1.            Mostrar películas                 |
        |                                                   |
        |   2.             Mostrar actores                  |
        |                                                   |
        |   3.                Regresar                      |
        |___________________________________________________|
    
    """)

    askInputGestionarPeliculas()



def gestionarPeliculas_mostrarPeliculas():
    
    try:
        print(Fore.MAGENTA + "Estas son las películas que se encontraron dentro del archivo \n")

        for diccionario in datos:
            print(Fore.BLUE + '[' + ''.join([f"'{clave}', '{valor}'," for clave, valor in diccionario.items()])[:-1] + ']')
            print()

    except Exception as e:
        print(Fore.RED + "Error" + e)

    finally:
        askInputMenuInicio()

"""
def gestionarPeliculas_mostrarActores():
    print("Mostrar actores")
"""

def gestionarPeliculas_mostrarActores():
    global datos
    # Imprime el listado de películas enumeradas
    print("Películas en el sistema:")
    for i, pelicula in enumerate(datos):
        print(f"{i+1}. {pelicula[0]}")

    # Solicita al usuario que seleccione una película
    pelicula_seleccionada = input("Seleccione una película para mostrar los actores (Ingrese el número de la película): ")
    try:
        pelicula_seleccionada = int(pelicula_seleccionada)
        if pelicula_seleccionada < 1 or pelicula_seleccionada > len(datos):
            raise ValueError
    except ValueError:
        print("ERROR: Selección inválida. Debe ingresar el número de una película en la lista.")
        gestionarPeliculas_mostrarActores()
        return

    # Muestra los actores de la película seleccionada
    pelicula_seleccionada -= 1  # Corregir el índice para acceder a la lista
    actores = datos[pelicula_seleccionada]["actores"]
    print(f"Actores de la película {datos[pelicula_seleccionada]['nombre']}:")
    for actor in actores.split(","):
        print(f"- {actor.strip()}")



def filtrado():
    print(Fore.LIGHTBLUE_EX + """
    
         _____________________FILTRADO______________________
        |                                                   |
        |   1.            Filtrar por actor                 |
        |                                                   |
        |   2.             Filtrar por año                  |
        |                                                   |
        |   3.            Filtrar por género                |
        |                                                   |
        |   4.                Regresar                      |
        |___________________________________________________|

    """)

    askInputFiltrado()

actor = "" 
def askInputActor():
    actorInput = input(Fore.RED + "Ingrese el nombre del actor \n")
    filtradoActor(actorInput)
    

def filtradoActor(actor):
    peliculas = []
    for elemento in datos:
        for key, value in elemento.items():
            if key == "actores":
                if actor in value:
                    peliculas.append(elemento[0])
                    break
    if peliculas:
        print(f"Las películas en las que participa {actor} son:")
        for i, pelicula in enumerate(peliculas):
            print(f"{i+1}. {pelicula}")
    else:
        print(f"No se encontraron resultados para {actor}")
    askInputMenuInicio()

def askInputFiltradoAnio():
    yearInput = input("Ingrese el año \n")
    filtradoAnio(yearInput)

def filtradoAnio(year):
    movies = cargarArchivosAnio()
    filtered_movies = []
    for movie in movies:
        movie_year = movie.split(";")[2]
        if movie_year == year:
            filtered_movies.append(movie)
    print(filtered_movies)

def filtradoGenero():
    askInputMenuInicio()

def grafica():

    data = '''
    digraph main {
        graph [pad="0.5", nodesep="0.5", ranksep="2"];
        node [shape=plain]
        rankdir=LR;\n
    '''
    global iteracion
    iteracion = 0
    iteracion_2 = 1

    peliculas = {
        'Avengers': 
        {
            'Actores':['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans', 'Mark Bufalo'], 
            'Anio': 2012, 
            'Genero': 'Accion'
        }, 
        'Spiderman Homecoming':
        {
            'Actores':['Robert Dw. Jr', 'Tom Holland', 'Zendaya'],
            'Anio':2016,
            'Genero':'Accion'
        }, 
        'Spiderman No Way Home':
        {
            'Actores':['Robert Dw. Jr', 'Tom Holland', 'Zendaya'],
            'Anio': 2018,
            'Genero': 'Accion'
        }, 
        'Avengers Infinity War':
        {
            'Actores':['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans'], 
            'Anio': 2018,
            'Genero': 'Accion'
        },
        'Thor Ragnarok':
        {
            'Actores':['Chris Hermswor', 'Mark Bufalo'],
            'Anio': 2017,
            'Genero': 'Accion'
        }}

    actores = ['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans', 'Mark Bufalo', 'Tom Holland', 'Zendaya']

    def crear_nodo(pelicula, anio, genero):
        global iteracion
        iteracion += 1
        return f'''\nnodo{iteracion} [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="#0091ea" port="p1" colspan="2">{pelicula}</td></tr>
        <tr><td> {anio} </td><td> {genero} </td></tr>
        </table>>];\n\n'''

    def crear_actor(actor):
        return f'\t"{actor}"\n' # Eso lo pueden omitir xd
        

    def crear_relacion(nodo,actor):
        return f'''\tnodo{nodo}:p1 -> "{actor}";\n'''

    def agregar_estilo():
        data += 'node [shape=box, style=filled, fillcolor="#00c853"]\n'

    # Aqui creamos los nodos de peliculas
    for pelicula in peliculas.keys():
        anio = peliculas[pelicula]['Anio']
        genero = peliculas[pelicula]['Genero']
        nodo =crear_nodo(pelicula, anio, genero)
        data += nodo

    # Aqui agregamos el estilo a los nodos de actores
    data += 'node [shape=box, style=filled, fillcolor="#00c853"]'
    # Aqui creamos los nodos de actores
    for actor in actores:
        nodo = crear_actor(actor)
        data += nodo

    # Aqui creamos las relaciones
    for pelicula in peliculas.keys():
        for actor in peliculas[pelicula]['Actores']:
            relacion = crear_relacion(iteracion_2,actor)
            data += relacion
        iteracion_2 += 1
        
    data += '}'

    # Aqui creamos el archivo
    with open('ejemplo_graphviz.dot', 'w') as f:
        f.write(data)

    # Aqui creamos la imagen
    os.system('dot -Tpng ejemplo_graphviz.dot -o ejemplo_graphviz.pdf')

menuInicio()
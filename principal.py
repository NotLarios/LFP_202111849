import colorama
from colorama import Fore

import tkinter as tk
from tkinter import filedialog

import os

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
    user = input(Fore.LIGHTCYAN_EX + "Presione Enter para ir al Menú Principal \n")
    if user == "":
        menuPrincipal()
    else:
        menuPrincipal()

def askInputMenuPrincipal():
    user = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")

    if user == "1":
        print(Fore.GREEN + "Se ha abierto una ventana para que seleccione el archivo \n")
        cargarArchivos()
    elif user == "2":
        gestionarPelículas()
    elif user == "3":
        filtrado()
    elif user == "4":
        filtrado()
    elif user == "5":
        exit()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputMenuPrincipal()

def askInputGestionarPeliculas():
    user = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")
    if user == "1":
        gestionarPeliculas_mostrarPeliculas()
    elif user == "2":
        gestionarPeliculas_mostrarActores()
    elif user == "3":
        menuPrincipal()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputGestionarPeliculas

def askInputFiltrado():
    user = input(Fore.CYAN + "Ingrese el número correspondiente a la opción que quiere utilizar \n")
    if user == "1":
        filtradoActor()
    elif user == "2":
        filtradoAnio()
    elif user == "3":
        filtradoGenero()
    elif user == "4":
        menuPrincipal()
    else:
        print(Fore.RED + """
        ==================================================================
                            Ingrese una opción válida
        ==================================================================
        """)
        askInputFiltrado()
        
datos = []
diccionario={}  
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
        print(str(datos[0]))
    except Exception as e:
        print(Fore.RED + "Error" + e)
    finally:
        askInputMenuInicio()


def gestionarPeliculas_mostrarActores():
    print("Mostrar actores")


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

def filtradoActor():
    print("Filtrado por actor")

def filtradoAnio():
    print("Filtrado por actor")

def filtradoGenero():
    print("Filtrado por actor")

def grafica():
    print("")

menuInicio()
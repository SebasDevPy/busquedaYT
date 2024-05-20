"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
from class_video import Video
from data import lista_videos

def menu():
    normalizados = False
    while True:
        print("\nMenú de opciones:")
        print("A. Normalizar objetos")
        print("B. Mostrar temas")
        print("C. Ordenar temas")
        print("D. Promedio de vistas")
        print("E. Máxima reproducción")
        print("F. Búsqueda por código")
        print("G. Listar por colaborador")
        print("H. Listar por mes")
        print("I. Salir")
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == 'A':
            Video.normalizar_videos(lista_videos)
            normalizados = True
            print("Videos normalizados.")
        elif opcion == 'B':
            if normalizados:
                Video.mostrar_temas(lista_videos)
            else:
                print("Debe normalizar los datos antes de usar esta opción.")
        elif opcion == 'C':
            if normalizados:
                Video.ordenar_temas(lista_videos)
            else:
                print("Debe normalizar los datos antes de usar esta opción.")
        elif opcion == 'D':
            Video.promedio_vistas(lista_videos)
        elif opcion == 'E':
            Video.maxima_reproduccion(lista_videos)
        elif opcion == 'F':
            codigo = input("Ingrese el código: ")
            Video.busqueda_por_codigo(lista_videos, codigo)
        elif opcion == 'G':
            colaborador = input("Ingrese el nombre del colaborador: ")
            Video.listar_por_colaborador(lista_videos, colaborador)
        elif opcion == 'H':
            mes = int(input("Ingrese el mes (1-12): "))
            Video.listar_por_mes(lista_videos, mes)
        elif opcion == 'I':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    menu()
from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime('%d-%m-%Y')}")
        print("*"*30)

    def dividir_titulo(self):
        partes = self.titulo.split(" | ")
        if len(partes) == 2:
            self.colaborador, sesion_str = partes
            self.sesion = int(sesion_str.replace("Sesión #", "").strip())
    
    def obtener_codigo_url(self):
        self.codigo_url = self.url_youtube.split("v=")[-1]
        
    def formatear_fecha(self):
        partes = self.fecha_lanzamiento.split("-")
        año = int(partes[0])
        mes = int(partes[1])
        dia = int(partes[2])
        self.fecha_lanzamiento = datetime(año, mes, dia)
    
    
    def normalizar_videos(lista_videos: list["Video"]):
        for video in lista_videos:
            if isinstance(video.fecha_lanzamiento, str):
                video.formatear_fecha()
            video.dividir_titulo()
            video.obtener_codigo_url()
   
    
    def mostrar_temas(lista_videos: list["Video"]):
        for video in lista_videos:
            video.mostrar_tema()

    
    def ordenar_temas(lista_videos: list["Video"]):
        tema = len(lista_videos)
        for i in range(tema-1):
            for j in range(0, tema-i-1):
                if lista_videos[j].sesion > lista_videos[j+1].sesion:
                    lista_videos[j], lista_videos[j+1] = lista_videos[j+1], lista_videos[j]
        print("Temas ordenados por sesión de menor a mayor.")

    
    def promedio_vistas(lista_videos):
        total_vistas = sum(video.vistas for video in lista_videos)
        promedio = total_vistas / len(lista_videos)
        print(f"Promedio de vistas: {promedio / 1000:.2f}k")

    
    def maxima_reproduccion(lista_videos):
        max_vistas = max(video.vistas for video in lista_videos)
        videos_max_vistas = [video for video in lista_videos if video.vistas == max_vistas]
        for video in videos_max_vistas:
            video.mostrar_tema()

    
    def busqueda_por_codigo(lista_videos, codigo):
        if codigo == "nick":
            videos_filtrados = [video for video in lista_videos if video.codigo_url[:len("nick")] == "nick"]
            for video in videos_filtrados:
                video.mostrar_tema()
        else:
            print("El código proporcionado no coincide con 'nick'.")

    
    def listar_por_colaborador(lista_videos, colaborador):
        videos_filtrados = [video for video in lista_videos if video.colaborador.lower() == colaborador.lower()]
        for video in videos_filtrados:
            video.mostrar_tema()

    
    def listar_por_mes(lista_videos, mes):
        if 1 <= mes <= 12:
            videos_filtrados = [video for video in lista_videos if video.fecha_lanzamiento.mes == mes]
            for video in videos_filtrados:
                video.mostrar_tema()
        else:
            print("Mes inválido. Debe estar entre 1 y 12.")
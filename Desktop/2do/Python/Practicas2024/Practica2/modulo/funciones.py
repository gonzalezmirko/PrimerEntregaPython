#1. Generar una estructura todas las estadísticas asociadas a cada jugador ojugadora.
def generar_estadisticas_jugadorxs(names, goals, goals_avoided, assists):

    #Genero una lista para almacenar las estadisticas de los jugadores
    estadisticas_jugadores=[]

    for nombre,goles,goles_evitados,asistencias in zip(names,goals,goals_avoided,assists):
        #Creo un diccionario con la informacion de cada jugador
        jugador={
            "nombre":nombre,
            "goles":goles,
            "goles_evitados":goles_evitados,
            "asistencias":asistencias
        }
        #Agrego el jugador(diccionario) a la lista que genere
        estadisticas_jugadores.append(jugador)

    return estadisticas_jugadores

#2. Conocer el nombre y la cantidad de goles del goleador o goleadora.
def buscar_goleadxr(estadisticas_jugadores):
    #Busco con la funcion max el jugador con mas goles con la expresion lambda 
    goleador=max(estadisticas_jugadores, key=lambda jugador: jugador['goles'])
    return goleador['nombre'], goleador['goles']

#3Conocer el nombre del jugador o jugadora más influyente.
def mas_influyente(estadisticas_jugadores):
    
    suma=max(estadisticas_jugadores,key=lambda x:x['goles']*1.5+x['goles_evitados']*1.25+x['asistencias'])
    return suma['nombre']

#4. Conocer el promedio de goles por partido del equipo en general.
def  promedio_goles_equipo(estadisticas_jugadores):
    partidos_temporada=25
    total_goles=0
    for jugador in estadisticas_jugadores:
        total_goles += jugador['goles']

    return total_goles / partidos_temporada

#5. Conocer el promedio de goles por partido del goleador o goleadora.
def promedio_goles_goleador(goles):
    partidos_temporada=25
    return goles/partidos_temporada
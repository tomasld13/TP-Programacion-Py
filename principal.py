#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        #Sonidos agregados para el juego.
        acierto=pygame.mixer.Sound("utinicortado.wav")
        error=pygame.mixer.Sound("noocortado.wav")
        laser=pygame.mixer.Sound("laser.wav")
        trompeta=pygame.mixer.Sound("trompeta.wav")
        #Preparar la ventana
        #Nombre del juego.
        pygame.display.set_caption("Guerra de las Palabras")
        #icono de la aplicación
        icono=pygame.image.load("yodababy.png")
        #Musica de fondo
        pygame.mixer.music.load("star.wav")
        pygame.mixer.music.play(3)
        pygame.display.set_icon(icono)
        screen = pygame.display.set_mode((ANCHO, ALTO))        
        #Imagen de fondo
        fondo=pygame.image.load("starfondonuevo.jpg").convert()
        screen.blit(fondo, (0,0))
        

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        tiempo= TIEMPO_MAX
        segundos = tiempo
        fps = FPS_inicial
        puntos = 200
        candidata = ""
        silabasEnPantalla = []
        posiciones = []
        listaDeSilabas=[]
        lemario=[]
        cont=0 #un contador que vale 0, se le va sumando 0.03 hasta llegar a 1 y vuelve a su valor inicial. Se usa para controlar la velocidad en que se agregan silabas en la pantalla.
        record=(recordA(puntos)) #variable que contiene el record de puntaje global
        racha=0 #racha de aciertos
        color=[] #lista que tendra el color de cada silaba en pantalla
        puntoX=0 #Un valor random entre los valores de x, que va cambiando cuando la variable cont llega a 1
        

        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)

        archivo2= open("lemario.txt","r")
        lectura(archivo2, lemario)

        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos,record,racha,color)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            if True:
            	fps = 60
            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario,dameSilabas,puntos,esValida)
                        
                        if procesar(candidata, silabasEnPantalla, posiciones, lemario,dameSilabas,puntos,esValida) > 0:  #si el valor retornado es mayor a 0 se trata de un acierto.
                            racha+=1  #se suma 1 a la racha de aciertos
                            a=record #contiene el ultimo record de puntos registrado
                            record=recordA(puntos) #devuelve el record de puntos actual
                            if a < record: #este if es para que cuando se supere al record por cada acierto suene un ruido de lasér
                                laser.play()
                            acierto.play() # se ejecuta el sonido de acierto 
                            quitar(candidata,silabasEnPantalla,posiciones,dameSilabas) #se quita la silaba que se uso para hacer la palabra
                            tiempo+=racha #le suma en segundos el valor de la racha
                        else:
                            puntos-=3
                            error.play() #se ejecuta el sonido cuando el usuario tiene una equivocación
                            racha=0 #la racha de aciertos vuelve a 0
                        candidata = ""

            segundos =tiempo - pygame.time.get_ticks()/1000
            #segundos+=tiempoExtra//2
            #Limpiar pantalla anterior
            #screen.fill(COLOR_FONDO)
            screen.blit(fondo, (0,0))

            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos,record,racha,color)

            pygame.display.flip()
            if cont > 1: #si el cont es mayor a 1 puntoX vuelve a tener un nuevo valor y el cont pasa a valer 0
                puntoX=random.randint(0,740)
                cont=0
            else: #si el cont no es mayor a 1, se va incrementando. La cantidad en que incrementa el cont depende de cuanto sea el puntaje, esto para que a mayor puntaje se vaya aumentando la velocidad en que aparecen las silabas.
                if puntos <50:
                    cont+=0.03
                elif puntos >=50 and puntos < 100:
                    cont+=0.05
                elif puntos >=100 and puntos < 150:
                    cont+=0.07
                elif puntos >=150:
                    cont+=0.09
                elif puntos >=200:
                    cont+=1.1
            actualizar(silabasEnPantalla, posiciones, listaDeSilabas, puntoX,cont,xigualy,puntos,color)
        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

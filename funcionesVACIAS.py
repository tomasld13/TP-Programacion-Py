from principal import *
from configuracion import *
from funcionesSeparador import *
import random
import math
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def lectura(archivo, lista):
    for elemento in archivo.readlines():
        lista.append(elemento[:-1])
    return lista
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def actualizar(silabasEnPantalla,posiciones,listaDeSilabas,puntoX,cont,xigualy,puntos,color):
    #este if es para agregar una primer silaba a la lista, una primera posicion y un primer color. Solo es llamada para asignar los primeros valores a las 3 listas. Es necesario ya que sino al comenzar la aplicación
    #la función dibujo llamaria a las listas pero estas al estar vacias producirian un error.
    if len(silabasEnPantalla) == 0:
        #llama a la función nuevaSilaba para obtener una silaba aleatoria de la listaDeSilabas y posteriormente la agrega a la lista SilabasEnPantalla
        agregar=nuevaSilaba(listaDeSilabas)
        silabasEnPantalla.append(agregar)
        #agrega a posiciones el valor de puntoX(que es aleatorio) y el valor y=0 para que aparezca en la parte superior de la pantalla.
        xy=(puntoX,0)
        posiciones.append(xy)
        #aquí la función obtiene tres valores al azar dentro de la paleta de colores y los agrega en la lista color. Esto le da un color distinto a cada silaba en pantalla.
        color1=random.randint(0,255)
        color2=random.randint(0,255)
        color3=random.randint(0,255)
        colores=(color1,color2,color3)
        #aquí la función obtiene tres valores al azar dentro de la paleta de colores y los agrega en la lista color. Esto le da un color distinto a cada silaba en pantalla.
        color.append(colores)
    #este elif es llamado cuando cont es mayor a uno, cont es una variable que se encuentra en principal empieza con un valor de 0 y se le va sumando 0.03 hasta que llega a 1, donde su valor vuelve a ser 0.
    #Esto permite tener un control sobre el tiempo en que aparecen las silabas en pantalla y evita que se agreguen palabras en la pantalla sin control.    
    elif cont > 1:
        #llama a la función nuevaSilaba para obtener una silaba aleatoria de la listaDeSilabas y posteriormente la agrega a la lista SilabasEnPantalla
        agregar=noEstaEnPantalla(nuevaSilaba,listaDeSilabas,silabasEnPantalla)
        silabasEnPantalla.append(agregar)
        a=puntoX
        for i in range(len(posiciones)):
            #puntoX es un valor de random.randint(0,Ancho-60) y c es el valor x de una silaba en pantalla.
            c=encontrarX(posiciones,i)
            if c==a and a+100 < ANCHO:
                a+=100
            elif c==a and a+100 > ANCHO:
                if a-100 > ANCHO:
                    a-=200
                else:
                    a-=100
        xy=(a,0)
        posiciones.append(xy)
    #esta parte de la función analiza si el valor "y" del indice "i" de la lista posiciones esta por superar el valor de la linea blanca de la pantalla, de ser asi se elimina la palabra y la posición.  
    for i in range(len(silabasEnPantalla)-1):
        x=encontrarX(posiciones,i)
        y=encontarY(posiciones,i,xigualy)
        if y < ALTO-110:
            #estos if son los que aceleran la velocidad cuando el usuario supera ciertos puntos.
            if puntos < 50:
                posiciones[i]=(x,y+0.5)
            elif puntos >=50 and puntos < 100:
                posiciones[i]=(x,y+0.8)
            elif puntos >=100 and puntos < 150:
                posiciones[i]=(x,y+1.2)
            elif puntos >= 150:
                posiciones[i]=(x,y+1.5)
            elif puntos >= 200:
                posiciones[i]=(x,y+1.8)
        else:
            for elemento in posiciones:
                if elemento == posiciones[i]:
                    posiciones.pop(i)
                    silabasEnPantalla.pop(i)
                    color.pop(i)
        #aquí la función obtiene tres valores al azar dentro de la paleta de colores y los agrega en la lista color. Esto le da un color distinto a cada silaba en pantalla.
        color1=random.randint(0,255)
        color2=random.randint(0,255)
        color3=random.randint(0,255)
        colores=(color1,color2,color3)
        color.append(colores)
    return silabasEnPantalla,posiciones,color
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función verifica que la silaba a agregar no este ya en la pantalla y ademas que tenga una longitud menor a 4, hasta que no se cumplan ambas funciones no retorna una silaba
def noEstaEnPantalla(nuevaSilaba,listaDeSilabas,silabasEnPantalla):
    cont=0
    while cont==0:
        a=nuevaSilaba(listaDeSilabas)
        if a not in silabasEnPantalla and len(a) < 4:
            cont+=1
    return a
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función retorna la poscion x del elemento (x,y) del indice de la lista posiciones
def encontrarX(lista,i):
    b=lista[i]
    a=0
    cont=0
    for elemento in b:
        while elemento != "(" and cont==0:
            a+=elemento
            cont+=1
    return a
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función retorna la poscion y del elemento (x,y) del indice de la lista posiciones
def encontarY(lista,i,xigualy):
    b=lista[i]
    a=0
    noquiero=["(",")"]
    c=encontrarX(lista,i)
    noquiero.append(c)
    #no quiero tendria los parentesis y a "x"
    for elemento in b:
        if elemento not in noquiero:
            a+=elemento
    #el problema que surge cuando la variable "a" sigue valiendo 0, ya que hay dos posibles causas. La primera es que "x" tenga el mismo valor que "y", ya que "x" esta dentro de noquiero. Y la segunda es que "y" valga 0.
    #para resolver esto tuve que recurrir a una nueva funcion que llamé "xigualy", la cual retorna True si los elementos "x-y" son iguales o False si son distintos, por lo cual confirmamos que "y" vale 0.
    if a==0:
        if xigualy(lista,i)==True:
            a=c
    return a
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def xigualy(lista,i):
    d=lista[i]
    a=[]
    for elemento in d:
        if elemento != "(" and elemento !=")" and elemento !=",":
            a.append(elemento)
            #agrega a "x" e "y" en la lista pero en diferentes indices.
    #compaerea los indices y retorna True si son iguales o False en caso contrario.
    if a[0]==a[1]:
        return True
    else:
        return False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función retorna una silaba aleatoria de listaDeSilabas, azar toma el valor de un numero random y la silaba es el indice del valor azar de la listaDeSilabas.
def nuevaSilaba(listaDeSilabas):
    azar=random.randint(0,len(listaDeSilabas)-1)
    silaba=listaDeSilabas[azar]
    return silaba
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función toma cada silaba de la palabra candidata y las compara con los elementos de silabasEnPantalla por indice, en caso que coincidan guarda el valor del indice y posteriormente quita los indices de ese valor de posiciones y silabasEnPantalla.
def quitar(candidata, silabasEnPantalla, posiciones,dameSilabas):
    silabas=dameSilabas(candidata)
    quitar=[]
    for i in range(len(silabasEnPantalla)-1):
        for elemento in silabas:
            if elemento == silabasEnPantalla[i]:
                quitar.append(i)
    for elemento in quitar:
        posiciones.pop(elemento)
        silabasEnPantalla.pop(elemento)
    return silabasEnPantalla,posiciones
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función invoca a la función separador, consigue la palabra candidata en una cadena separada por un guion y luego haciendo uso de cadena.spli("-") guarda las silabas en una lista que retorna.
def dameSilabas(candidata):
    cadena=separador(candidata)
    silabas=cadena.split("-")
    return silabas
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función primero toma las silabas de la palabra candidata, las compara con las silabas que estan en pantalla y si coinciden la bandera enPantalla mantiene el valor de True; luego la función compara a candidata con las palabras del lemario
#y en caso de que esta se encuentre dentro de este la bandera enLemario mantiene el valor True; finalmente si ambas banderas son verdaderas la función retorna True.
def esValida(candidata, silabasEnPantalla, lemario):
    silabas=dameSilabas(candidata)
    enPantalla=True
    enLemario=True
    for elemento in silabas:
        if elemento in silabasEnPantalla:
            enPantalla=True
        else:
            enPantalla=False
    if candidata in lemario:
        enLemario=True
    else:
        enLemario=False
    if enPantalla==enLemario:
        return True
    else:
        return False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función toma la palabra candidata, una variable puntaje que vale 0, una variable llamada vocal que contiene a las vocales y otra llamada consonanteDificil que contiene a las consonantes que valen 5 puntos.
#Analiza cada elemento de candidata, si el elemento esta en vocal, puntaje suma 1 punto, si esta en consonante dificil suma 5, y si no esta en ninguno se da por hecho que es ua consonante normal por lo que suma 2. Finalmente retornna el puntaje.
def Puntos(candidata):
    vocal="aeiou"
    consonanteDificil="jkqwxyz"
    puntaje=0
    for elemento in candidata:
        if elemento in vocal:
            puntaje+=1
        elif elemento in consonanteDificil:
            puntaje+=5
        else:
            puntaje+=2
    return puntaje
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función invoca a esValida si esta retorna False significa que candidata no cumple los requisitos y retorna 0 puntos, pero en caso que esta retorne True la variable puntaje es el puntaje que retorne la función Puntos tomando como parametro a candidata, finalemnte retorna los puntos.
def procesar(candidata, silabasEnPantalla, posiciones, lemario,dameSilabas,puntos,esValida):
    bandera=esValida(candidata,silabasEnPantalla,lemario)
    if bandera==True:
        puntaje=Puntos(candidata)
    else:
        puntaje=0
    return puntaje
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta fución abre el archivo de texto record, en este se encuentra el record global actual, la función analiza el puntaje actual de la partida y en caso de que este supere al record escribe el puntaje (record actual) en el archivo de texto.
#Es invocada en la función dibujar.
def recordA(puntos):
    archivo=open("record.txt","r")
    record=0
    for elemento in archivo.readlines():
        if int (elemento) < puntos:
            record+=puntos
            archivo.close()
            archivo=open("record.txt","w")
            archivo.write(str(puntos))
            archivo.close()
        else:
            record+=int(elemento)
    return record
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Esta función elije 3 valores aleatorios entre 0-255 y luego los agrega a un mismo indice de una lista, este es el valor de un color. Es invocada e la función dibujar dandole un color aleatorio a cada silaba en panatalla.
def colorLetra():
    lista=[]
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)
    color=(color1,color2,color3)
    lista.append(color)
    return lista
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
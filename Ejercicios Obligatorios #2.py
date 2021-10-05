#a)
def separa_en_palabras(cadena):
    lista=[]
    agrega=""
    espacios=0
    espacioEnFor=0
    ultimo=""
    for elemento in cadena:
        if elemento==" ":
            espacios+=1
    for elemento in cadena:
        if elemento !=" " and espacioEnFor<espacios:
            agrega+=elemento
        elif elemento == " ":
            lista.append(agrega)
            espacioEnFor+=1
            agrega=""
        else:
            agrega=""
            agrega+=elemento
            ultimo+=agrega
    lista.append(ultimo)
    for i in range(len(lista)):
        if lista[i]=="la":
            lista[i]="una"
    return lista
#prueba
print(separa_en_palabras("en la luna de lana la rata blanca mata a la gata"))
#b)
def volverACadena(lista):
    cadenaNueva=""
    for i in range(len(lista)):
        cadenaNueva+=lista[i]
        cadenaNueva+=" "
    return cadenaNueva
#prueba
print(volverACadena(separa_en_palabras("en la luna de lana la rata blanca mata a la gata")))

#2)
pre=["tolera","repugna","alterna","vigila","releva"]
suf=["ante","ancia","ble","dor"]
lista=[]
suf[0]="nte"
suf[1]="ncia"
for elemento in pre:
    for i in suf:
        a=elemento+i
        lista.append(a)
print(lista)
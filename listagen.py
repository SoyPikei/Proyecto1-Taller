import random  #Libreria Necesaria para la funcion random
import time #Libreria Necesaria para calcular el tiempo entre procesos
import matplotlib.pyplot as plt #Libreria necesaria para renderizar graficos

NUMREPETICIONES = 10 #El numero de veces que se contaran los tiempos para sacar un promedio
TAMAÑOS = [10, 100, 500, 1000, 5000, 10000] #Los tamaños de las listas que seran probados
#TAMAÑOS = [10, 100, 500, 600, 700, 800]
def crear_listasrandom():  # Funcion que genera listas con valores al azar esparcidos, con largos definidos
    vector10 = []
    vector100 = []
    vector500 = []
    vector1000 = []
    vector5000 = []
    vector10000 = []
    largo = TAMAÑOS[0]
    while largo > 0:
        vector10.append(random.randint(0,100))  #Esta funcion random agrega a la lista con .append un valor al azar con el rango definido(0 a 100)
        largo -= 1
    largo = TAMAÑOS[1]  #Cambio el valor de largo para elegir la cantidad de veces que se hara el append
    while largo > 0:
        vector100.append(random.randint(0, 100))
        largo -= 1
    largo = TAMAÑOS[2]
    while largo > 0:
        vector500.append(random.randint(0, 100))
        largo -= 1
    largo = TAMAÑOS[3]
    while largo > 0:
        vector1000.append(random.randint(0, 100))
        largo -= 1
    largo = TAMAÑOS[4]
    while largo > 0:
        vector5000.append(random.randint(0, 100))
        largo -= 1
    largo = TAMAÑOS[5]
    while largo > 0:
        vector10000.append(random.randint(0, 100))
        largo -= 1
    return vector10, vector100, vector500, vector1000, vector5000, vector10000  #se retornan las listas en una tupla

LISTASDEPRUEBA=crear_listasrandom() #Se asigna la tupla como valor global para que las listas sean las mismas en todos los algoritmos
print("Listas Creadas")

def merge_sort_calcs(lista):
    calculos=[0,0] #[Comparaciones,Intercambios]
    def merge(izq, der):
        result = []
        i = 0
        j = 0
        while i < len(izq) and j < len(der):
            calculos[0]+=1
            if izq[i] < der[j]:
                result.append(izq[i])
                i += 1
            else:
                result.append(der[j])
                j += 1
            calculos[1]+=1
        result = result + izq[i:]
        result = result + der[j:]
        calculos[1]+=(len(izq[i:]) + len(der[j:]))
        return result

    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        pivote = len(lista) // 2
        izq = merge_sort(lista[:pivote])
        der = merge_sort(lista[pivote:])
        return merge(izq, der)
    merge_sort(lista)
    return calculos[0], calculos[1]

def counting_sort(lista):
    mayor=max(lista)
    lista_aux=[0]*(mayor+1)#se crea la lista con ceros para llevar la cuenta de la cantidad de veces que se repite un número y su respectiva posición
    for i in lista:
        lista_aux[i]+=1#le suma 1 a ese i número de posición las veces que se encuentra en la lista 
    res=[]
    intercambios=0
    for j in range(len(lista_aux)):
        while lista_aux[j]>0:
            res.append(j)#se le va agregando los elementos según su posisción para dar la respuesta
            lista_aux[j]-=1#se le va restando a la lista que lleva la cuenta los elementos que se agregan a la nueva lista
            intercambios+=1
    return 0, intercambios
#esta nomas es de apoyo emocional y que verifique si está ordenado o no
def ordenado(a,b):
    return a<=b


def bubble(lista):
    #variable que nos cuenta los cambios :D
    swaps=1
    comparaciones=0
    intercambios=0
    #con esto, se va a repetir el for mientras existan swaps que hacer
    while swaps:
        
        #se reinicia la variable
        swaps=0
        
        #se recorre la lista
        for i in range(0,len(lista)-1):
            comparaciones+=1
            #se verifica si los numeros estan desordenados
            if not ordenado(lista[i],lista[i+1]):
                
                #empieza a hacerle swap a las posiciones
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
                intercambios+=1
                swaps=1
    return comparaciones,intercambios

def selection_sort(lista):
    n=len(lista)
    comparaciones=0
    intercambios=0
    for i in range(n-1):
        min_index =i
        for j in range(i+1,n):
            comparaciones+=1
            if lista[j]<lista[min_index]:
                min_index=j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        intercambios+=1
    return comparaciones, intercambios

def calculoDeTiempos(i,lista):
    tiempos = []
    for _ in range(NUMREPETICIONES):
        listacopy = lista.copy()
        inicio = time.perf_counter()
        ALGORITMOS[i](listacopy)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    comparaciones, intercambios= ALGORITMOS[i](lista.copy())
    return (sum(tiempos) / NUMREPETICIONES), comparaciones, intercambios#Calcula el promedio 


def calculosMergeSort():
    tiempos_en_ms_aleatorio = []
    tiempos_en_ms_ordenado = []
    tiempos_en_ms_reverso = []
    comparaciones_aleatorio=[]
    comparaciones_ordenadas=[]
    intercambios_aleatorio=[]
    intercambios_ordenadas=[]
    for i in range(6):
        lista = LISTASDEPRUEBA[i]
        resaleatorio=calculoDeTiempos(0,lista)
        tiempos_en_ms_aleatorio.append(resaleatorio[0])
        comparaciones_aleatorio.append(resaleatorio[1])
        intercambios_aleatorio.append(resaleatorio[2])
        listasort = sorted(lista)
        resordenado=calculoDeTiempos(0,listasort)
        tiempos_en_ms_ordenado.append(resordenado[0])
        comparaciones_ordenadas.append(resordenado[1])
        intercambios_ordenadas.append(resordenado[2])
        listareverse = sorted(lista, reverse=True)
        tiempo = calculoDeTiempos(0,listareverse)[0]
        tiempos_en_ms_reverso.append(tiempo)
    print("Merge Sort Completado")
    return tiempos_en_ms_aleatorio, tiempos_en_ms_ordenado,tiempos_en_ms_reverso, comparaciones_aleatorio,comparaciones_ordenadas,intercambios_aleatorio,intercambios_ordenadas

def calculosSelectionSort():
    tiempos_en_ms_aleatorio = []
    tiempos_en_ms_ordenado = []
    tiempos_en_ms_reverso = []
    comparaciones_aleatorio=[]
    comparaciones_ordenadas=[]
    intercambios_aleatorio=[]
    intercambios_ordenadas=[]
    
    for i in range(6):
        lista = LISTASDEPRUEBA[i]
        lista = LISTASDEPRUEBA[i]
        resaleatorio=calculoDeTiempos(1,lista)
        tiempos_en_ms_aleatorio.append(resaleatorio[0])
        comparaciones_aleatorio.append(resaleatorio[1])
        intercambios_aleatorio.append(resaleatorio[2])
        listasort = sorted(lista)
        resordenado=calculoDeTiempos(1,listasort)
        tiempos_en_ms_ordenado.append(resordenado[0])
        comparaciones_ordenadas.append(resordenado[1])
        intercambios_ordenadas.append(resordenado[2])
        listareverse = sorted(lista, reverse=True)
        tiempo = calculoDeTiempos(1,listareverse)[0]
        tiempos_en_ms_reverso.append(tiempo)
    print("Selection Sort Completado")
    return tiempos_en_ms_aleatorio, tiempos_en_ms_ordenado,tiempos_en_ms_reverso, comparaciones_aleatorio,comparaciones_ordenadas,intercambios_aleatorio,intercambios_ordenadas

def calculosCountingSort():
    tiempos_en_ms_aleatorio = []
    tiempos_en_ms_ordenado = []
    tiempos_en_ms_reverso = []
    comparaciones_aleatorio=[]
    comparaciones_ordenadas=[]
    intercambios_aleatorio=[]
    intercambios_ordenadas=[]
    
    for i in range(6):
        lista = LISTASDEPRUEBA[i]
        resaleatorio=calculoDeTiempos(2,lista)
        tiempos_en_ms_aleatorio.append(resaleatorio[0])
        comparaciones_aleatorio.append(resaleatorio[1])
        intercambios_aleatorio.append(resaleatorio[2])
        listasort = sorted(lista)
        resordenado=calculoDeTiempos(2,listasort)
        tiempos_en_ms_ordenado.append(resordenado[0])
        comparaciones_ordenadas.append(resordenado[1])
        intercambios_ordenadas.append(resordenado[2])
        listareverse = sorted(lista, reverse=True)
        tiempo = calculoDeTiempos(2,listareverse)[0]
        tiempos_en_ms_reverso.append(tiempo)
    print("Counting Sort Completado")
    return tiempos_en_ms_aleatorio, tiempos_en_ms_ordenado,tiempos_en_ms_reverso, comparaciones_aleatorio,comparaciones_ordenadas,intercambios_aleatorio,intercambios_ordenadas

def calculosBubbleSort():
    tiempos_en_ms_aleatorio = []
    tiempos_en_ms_ordenado = []
    tiempos_en_ms_reverso = []
    comparaciones_aleatorio=[]
    comparaciones_ordenadas=[]
    intercambios_aleatorio=[]
    intercambios_ordenadas=[]
    for i in range(6):
        lista = LISTASDEPRUEBA[i]
        resaleatorio=calculoDeTiempos(3,lista)
        tiempos_en_ms_aleatorio.append(resaleatorio[0])
        comparaciones_aleatorio.append(resaleatorio[1])
        intercambios_aleatorio.append(resaleatorio[2])
        listasort = sorted(lista)
        resordenado=calculoDeTiempos(3,listasort)
        tiempos_en_ms_ordenado.append(resordenado[0])
        comparaciones_ordenadas.append(resordenado[1])
        intercambios_ordenadas.append(resordenado[2])
        listareverse = sorted(lista, reverse=True)
        tiempo = calculoDeTiempos(3,listareverse)[0]
        tiempos_en_ms_reverso.append(tiempo)
    print("Bubble Sort Completado")
    return tiempos_en_ms_aleatorio, tiempos_en_ms_ordenado,tiempos_en_ms_reverso, comparaciones_aleatorio,comparaciones_ordenadas,intercambios_aleatorio,intercambios_ordenadas

ALGORITMOS=[merge_sort_calcs,selection_sort, counting_sort, bubble]

def graficas(): #Funcion para renderizar la grafica con matplotlib
    Merge=calculosMergeSort()
    Selection=calculosSelectionSort()
    Counting=calculosCountingSort()
    Bubble=calculosBubbleSort()
    plt.figure(figsize=(15, 10))
    
    for i in range(3):
        plt.subplot(2,2,i+1)
        plt.plot(TAMAÑOS,Merge[i], color='blue', label="Merge Sort", marker='o')
        plt.plot(TAMAÑOS,Selection[i], color='red', label="Selection Sort", marker='o')
        plt.plot(TAMAÑOS,Counting[i], color='magenta', label="Counting Sort", marker='o')
        plt.plot(TAMAÑOS,Bubble[i], color='green', label="Bubble Sort", marker='o')
        if i==0: plt.title("Rendimiento de Algoritmos en listas Aleatorias")
        elif i ==1: plt.title("Rendimiento de Algoritmos en listas Ordenadas")
        else: plt.title("Rendimiento de Algoritmos en listas Reversas")
        plt.xlabel("Tamaño de lista")
        plt.ylabel("Tiempo en Segundos")
        plt.xscale("log")
        plt.yscale("log")
        plt.grid()
        plt.legend()
    
    plt.show()
    plt.figure(figsize=(15, 10))
    for i in range(3,5):
        if i==3: plt.subplot(1,2,1)
        else: plt.subplot(1,2,2)
        plt.plot(TAMAÑOS,Merge[i], color='blue', label="Merge Sort", marker='o')
        plt.plot(TAMAÑOS,Selection[i], color='red', label="Selection Sort", marker='o')
        plt.plot(TAMAÑOS,Counting[i], color='magenta', label="Counting Sort", marker='o')
        plt.plot(TAMAÑOS,Bubble[i], color='green', label="Bubble Sort", marker='o')
        if i==3: plt.title("Numero de Comparaciones en listas Aleatorias")
        else: plt.title("Numero de Comparaciones en listas Ordenadas")
        plt.xlabel("Tamaño de lista")
        plt.ylabel("Número de comparaciones")
        plt.xscale("log")
        plt.yscale("log")
        plt.grid()
        plt.legend()
    plt.show()
    plt.figure(figsize=(15, 10))
    for i in range(5,7):
        if i==5: plt.subplot(1,2,1)
        else: plt.subplot(1,2,2)
        plt.plot(TAMAÑOS,Merge[i], color='blue', label="Merge Sort", marker='o')
        plt.plot(TAMAÑOS,Selection[i], color='red', label="Selection Sort", marker='o')
        plt.plot(TAMAÑOS,Counting[i], color='magenta', label="Counting Sort", marker='o')
        plt.plot(TAMAÑOS,Bubble[i], color='green', label="Bubble Sort", marker='o')
        if i==5: plt.title("Numero de Intercambios en listas Aleatorias")
        else: plt.title("Numero de Intercambios en listas Ordenadas")
        plt.xlabel("Tamaño de lista")
        plt.ylabel("Número de Intercambios")
        plt.xscale("log")
        plt.yscale("log")
        plt.grid()
        plt.legend()
    plt.show()
graficas()
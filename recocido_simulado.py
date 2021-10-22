#RECOCIDO SIMULADO
#Autor: Rodrigo Antonio Arciniega Mendoza

"""Este algoritmo realiza 30 corridas de Recocido Simulado y entrega 2 listas
   que contienen los mejores costos y los mejores tiempos en cada una de esas
   corridas. Para este algoritmo dedique aproximadamente 20 minutos, todo fue 
   muy rapido"""

import random # Libreria necesaria para generar datos aleatorios
import math # Libreria necesaria para funciones trigonometricas
from time import time # Libreria necesaria para poder medir el timpo

MejoresCostos=[] # Listas en donde se guardan los 30 datos obtenidos
MejoresTiempos=[]

def FO(SolActual): # Definimos la Funcion Objetivo
    a=SolActual[0]
    b=SolActual[1]
    cte=418.9829*2
    f=cte-((a*math.sin(math.sqrt(math.fabs(a))))+(b*math.sin(math.sqrt(math.fabs(b)))))
    return f

for i in range (30):
    print("Desplegado del dato ", i+1)
    tiempo_inicial=time() # Comienzo a medir el tiempo
    MejorSol=[] # Vector para no perder la mejor solucion
    MejorCosto=0 # Flotante para no perder el mejor costo
    Temp=0  # Temperatura
    SolActual = [round(random.uniform(-500,500),4),round(random.uniform(-500,500),4)] # Generamos una solucion inicial aleatoria
    print('la solucion aleatoria es: ',SolActual)
    CostoActual = FO(SolActual)     # Calculamos el costo de la solucion aleatoria
    print('Y tiene un costo de: ',CostoActual)
    MejorSol=SolActual        # Condiciones iniciales
    MejorCosto=CostoActual
    e=10                    # Tratamos que epsilon no sea mayor a 10
    TInicial=1000.00
    TFinal=0.001
    alfa=0.95
    Iter=6000           # El numero de iteraciones fue lo unico que modifique
    Temp=TInicial
   
    """La verdad este algoritmo dio resultados mucho mejores, aunque tal vez 
        empleo un poco mas de tiempo computacional."""
    
    while Temp > TFinal:
        for i in range(Iter):
            Vecin=[round(random.uniform(-1,1),4),round(random.uniform(-1,1),4)]
            Vecino=[e*Vecin[0],e*Vecin[1]] # Generamos un vecindario diferente por cada vez que se itere el ciclo
            SolVecina=[SolActual[0]+Vecino[0],SolActual[1]+Vecino[1]] # Ese vecindario cambiara de tamaño segun cada una de las soluciones obtenidas
            if SolVecina[0]>500 or SolVecina[0]<-500: # Validamos que nuestra solucion vecina este dentro del dominio de la funcion
                if SolVecina[0]>500:
                    SolVecina[0]=500-(SolVecina[0]-500)
                else:
                    SolVecina[0]=-500-(SolVecina[0]+500)
            if SolVecina[1]>500 or SolVecina[1]<-500:
                if SolVecina[1]>500:
                    SolVecina[1]=500-(SolVecina[1]-500)
                else:
                    SolVecina[1]=-500-(SolVecina[1]+500)
            CostoVecina = FO(SolVecina) # Obtenemos el costo de la solucion vecina
            if CostoVecina < CostoActual: # Aplicamos los criterios decision de RECOCIDO SIMULADO
                CostoActual=CostoVecina
                SolActual=SolVecina
                if CostoVecina < MejorCosto:    # Evaluamos si el costo vecino es mejor que el mejor costo conocido hasta el momento
                    MejorCosto=CostoVecina      
                    MejorSol=SolVecina
            else:                           # Criterio de Metropolis
                u = round(random.uniform(0, 1),4)     #Generamos numero aleatorio entre 0 y 1
                b = math.exp(-1*((CostoVecina-CostoActual)/Temp))
                if u < b:
                    CostoActual = CostoVecina # Actualizamos los valores de las soluciones optimas 
                    SolActual = SolVecina
        Temp=Temp*alfa  # Decrementamos la temperatura
        
    tiempo_final=time() # Dejamos de medir el tiempo
    tiempo_total=tiempo_final-tiempo_inicial # Guardamos el tiempo en una variable

    print("El mejor costo encontrado por el algoritmo es: ", MejorCosto)  # Imprimimos nuestros resultados
    print('La mejor solucion encontrada es: ', MejorSol)
    print('El tiempo de ejecucion del algoritmo es: ', round(tiempo_total,4),"segundos")
    MejoresCostos.append(MejorCosto)       # Guardamos nuestros mejores costos
    MejoresTiempos.append(tiempo_total)     # Guardamos nuestros mejores tiempos
    print('\n')
    print('\n')
    
print('Los 30 mejores Costos son:', MejoresCostos)
print('Los 30 mejores tiempos son: ', MejoresTiempos)

import random
import time
from math import dist

numero_filas = int(input("introducir numero de filas: "))
numero_columnas = int(input("introducir numero de columnas: "))

laberinto =[]
#mostrar laberinto
def mostrar (laberinto):
    for filas in laberinto:
        for valor in filas:
            print( valor, end=" ")
        print()

#marcos laberinto
for i in range(0,numero_filas):
    fila=[]   
    for j in range(0,numero_columnas):         
        if i == 0 or j==0 or i == numero_filas -1 or j == numero_columnas -1 :
            fila.append(1)
        else: 
            fila.append(0)
    laberinto.append(fila)

#laberinto
numero_paredes = int((numero_columnas+numero_filas)/2)
for p in range(numero_paredes*4):
    fila_actual =random.randrange(2,numero_filas-2)
    columna_actual=random.randrange(2,numero_columnas-2)
    #evita paredes dobles
    fila_actual = int((fila_actual / 2)) * 2
    columna_actual = int((columna_actual / 2)) * 2 
   
    laberinto[fila_actual][columna_actual] = 8
    if laberinto[fila_actual][columna_actual-2] == 0:
        laberinto[fila_actual][columna_actual-2] = 8
        laberinto[fila_actual][columna_actual-1] = 8
    if laberinto[fila_actual][columna_actual+2] == 0:
        laberinto[fila_actual][columna_actual+2] = 8
        laberinto[fila_actual][columna_actual+1] = 8
    if laberinto[fila_actual-2][columna_actual] == 0:
        laberinto[fila_actual-2][columna_actual] = 8
        laberinto[fila_actual-1][columna_actual] = 8
    if laberinto[fila_actual+2][columna_actual] == 0:
        laberinto[fila_actual+2][columna_actual] = 8
        laberinto[fila_actual+1][columna_actual] = 8

#generador de personas
contador_personas = 0
personas_pos =[]
while True:
    persona_f =random.randrange(1,numero_filas-1)
    persona_c=random.randrange(1,numero_columnas-1)
    if laberinto[persona_f][persona_c] == 0:
        laberinto[persona_f][persona_c] = "*"
        contador_personas += 1
        personas_pos.append(persona_f)  
        personas_pos.append(persona_c)
    if len(personas_pos) == 6:
        break
#eliminar los 0
for i in range(0,numero_filas):
    for j in range(0,numero_columnas):
        if laberinto[i][j]==0:
            laberinto[i][j]=" "
#buscador de personas
    #(ordenando el array de las posisiones de las personas)
personas_pos_ord =[]
if personas_pos[0]+personas_pos[1] < personas_pos[2]+personas_pos[3] and personas_pos[0]+personas_pos[1] < personas_pos[4]+personas_pos[5] :
    personas_pos_ord.append(personas_pos[0])
    personas_pos_ord.append(personas_pos[1])
    if personas_pos[2]+personas_pos[3] < personas_pos[4]+personas_pos[5]:
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
    else:
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
elif personas_pos[2]+personas_pos[3] < personas_pos[0]+personas_pos[1] and personas_pos[2]+personas_pos[3] < personas_pos[4]+personas_pos[5] :
    personas_pos_ord.append(personas_pos[2])
    personas_pos_ord.append(personas_pos[3])
    if personas_pos[0]+personas_pos[1] < personas_pos[4]+personas_pos[5]:
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
    else:
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
else:
    personas_pos_ord.append(personas_pos[4])
    personas_pos_ord.append(personas_pos[5])
    if personas_pos[0]+personas_pos[1] < personas_pos[2]+personas_pos[3]:
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
    else:
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
    #buscador
laberinto[1][1]= "-"
fi=1
co=1
def encontrado(fi,co):   
    if laberinto[fi+1][co] == "*":
        print ("SE A ENCONTRADO A UNA PERSONA")
        laberinto[fi+1][co] = " "
        fi+=1
        return True
    elif laberinto[fi][co+1] == "*":
        print ("SE A ENCONTRADO A UNA PERSONA")
        laberinto[fi][co+1] = " "
        co+=1
        return True
    elif laberinto[fi][co-1] == "*":
        print ("SE A ENCONTRADO A UNA PERSONA")
        laberinto[fi][co-1] = " "
        co-=1
        return True
    elif laberinto[fi-1][co] == "*":
        print ("SE A ENCONTRADO A UNA PERSONA")
        laberinto[fi-1][co] == " "
        fi-=1
        return True
    return False
conta=3
rand=0
secs=1
persona = (personas_pos_ord[0],personas_pos_ord[1])
while True:
    #encontrado()
    d1=1000
    d2=1000
    d3=1000
    d4=1000
    if encontrado(fi,co)==True:
        print ("posision f: ",fi," posision c: ",co)
        conta-=1
    if conta == 2:
        persona = (personas_pos_ord[2],personas_pos_ord[3])
    if conta == 1:
        persona = (personas_pos_ord[4],personas_pos_ord[5])
    if conta == 0:
        break

    if laberinto[fi+1][co]== " ":
            #laberinto[fi][co]= " "
            lugar_actual = (fi+1,co)
            d1= dist(lugar_actual,persona)
            #laberinto[fi+1][co]= "-"
            #fi+=1

    if laberinto[fi][co+1] == " ":
            #laberinto[fi][co] = " "
            lugar_actual = (fi,co+1)
            d2= dist(lugar_actual,persona)
            #laberinto[fi][co+1] = "-"
            #co+=1

    if laberinto[fi-1][co] == " ":
           # laberinto[fi][co] = " "
            lugar_actual = (fi-1,co)
            d3= dist(lugar_actual,persona)
            #laberinto[fi-1][co] = "-"
            #fi-=1

    if laberinto[fi][co-1] == " ":
            #laberinto[fi][co] = " "
            #laberinto[fi][co-1] = "-"
            lugar_actual = (fi,co-1)
            d4= dist(lugar_actual,persona)
            #co-=1    
    #en caso de no contar con ningun camino se ara un retroceso
    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d1:
        laberinto[fi][co] = "R"
        #fijamos la nueva coordenada
        if laberinto[fi+1][co]== "-": 
            fi+=1

        else:
            if laberinto[fi][co+1] == "-":
                co+=1
            else:
                if laberinto[fi-1][co] == "-":
                    fi-=1
                else:
                    if laberinto[fi][co-1] == "-":
                        co-=1

    #menor distancia
    else:
        if(d1 <= d2 and d1 <= d3 and d1 <= d4):
            laberinto[fi+1][co]= "-"
            fi+=1
        else:
            if(d2 < d1 and d2 < d3 and d2 < d4):
                laberinto[fi][co+1] = "-"
                co+=1
            else:
                if(d3 <= d1 and d3 <= d2 and d3 <= d4):
                    laberinto[fi-1][co] = "-"
                    fi-=1
                else:
                    if(d4 < d1 and d4 < d2 and d4 < d3):
                        laberinto[fi][co-1] = "-"
                        co-=1
    
    mostrar (laberinto)    
    time.sleep(secs)
#mostrar laberinto
#mostrar (laberinto)
print("SE GENERARON ",contador_personas," PERSONAS")
print("posisiones generadas: ",personas_pos)
print("posisiones ordenadas: ",personas_pos_ord)


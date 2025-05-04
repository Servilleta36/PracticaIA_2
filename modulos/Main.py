from Laberinto import Laberinto
from A import A
from IDA import IDA
from GBFS import GBFS
from B_Profundidad import Profundidad
from B_Anchura import Anchura
from B_Prof_Bid import Bidireccional
from B_Prof_Iter import Iterativa
from B_Prof_Lim import Limite
import time

def MedirTiempo(algoritmo):
    inicio=time.time_ns()
    algoritmo.moverse()
    final=time.time_ns()
    duracion=(final-inicio)//1000
    print("Tiempo de ejecución: "+str(duracion)+ " ns")


def main():
    lab=Laberinto()

    print("----------LABERINTOS----------")
    print("1. Cargar Maze1.txt")
    print("2. Cargar Maze2.txt")
    print("3. Cargar Maze3.txt")
    print("4. Cargar laberinto aleatorio")
    opc_lab=input("Elige una opcion: ")

    if opc_lab=="1":
        lab.CargaLab("Maze1.txt")
        lab.MuestraLab()

    elif opc_lab=="2":
        lab.CargaLab("Maze2.txt")
        lab.MuestraLab()

    elif opc_lab=="3":
        lab.CargaLab("Maze3.txt")
        lab.MuestraLab()

    elif opc_lab=="4":
        lab.CreaLab()
        lab.GuardaLab()
        lab.MuestraLab()

    while True:
       print("\n")
       print("-------MENU-------")
       print("1. Algoritmo A*")
       print("2. Algoritmo IDA*")
       print("3. Algoritmo GBFS")
       print("4. Algoritmo de búsqueda en anchura")
       print("5. Algoritmo de búsqueda en profundidad")
       print("6. Algoritmo de búsqueda en profundidad bidireccional")
       print("7. Algoritmo de búsqueda en profundidad iterativa")
       print("8. Algoritmo de búsqueda en profundidad límite")
       print("9. Salir")
       opc=input("Elige una opcion: ")

       if opc=="1":
           a=A(lab)
           MedirTiempo(a)
           lab.MuestraLab()

       if opc=="2":
           ida=IDA(lab)
           MedirTiempo(ida)
           lab.MuestraLab()

       if opc=="3":
           gbfs=GBFS(lab)
           MedirTiempo(gbfs)
           lab.MuestraLab()

       if opc == "4":
           anchura=Anchura(lab)
           MedirTiempo(anchura)
           lab.MuestraLab()

       if opc=="5":
           profundidad=Profundidad(lab)
           MedirTiempo(profundidad)
           lab.MuestraLab()

       if opc == "6":
           bidireccional=Bidireccional(lab)
           MedirTiempo(bidireccional)
           lab.MuestraLab()

       if opc == "7":
           iterativa=Iterativa(lab)
           MedirTiempo(iterativa)
           lab.MuestraLab()

       if opc == "8":
           limite=Limite(lab)
           MedirTiempo(limite)
           lab.MuestraLab()

       if opc=="9":
            break

if __name__=="__main__":
    main()
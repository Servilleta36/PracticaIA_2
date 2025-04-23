from Laberinto import Laberinto
from A import A
from IDA import IDA
from GBFS import GBFS
from B_Profundidad import Profundidad

def main():
    lab=Laberinto()

    print("----------LABERINTOS----------")
    print("1. Cargar laberinto aleatorio")
    print("2. Cargar Maze1.txt")
    print("3. Cargar Maze2.txt")
    print("4. Cargar Maze3.txt")
    opc_lab=input("Elige una opcion: ")

    if opc_lab=="1":
        lab.CreaLab()
        lab.GuardaLab()
        lab.MuestraLab()

    elif opc_lab=="2":
        lab.CargaLab("Maze1.txt")
        lab.MuestraLab()

    elif opc_lab=="3":
        lab.CargaLab("Maze2.txt")
        lab.MuestraLab()

    elif opc_lab=="4":
        lab.CargaLab("Maze3.txt")
        lab.MuestraLab()

    while True:
       print("\n")
       print("-------MENU-------")
       print("1. Algoritmo A*")
       print("2. Algoritmo IDA*")
       print("3. Algoritmo GBFS")
       print("4. Algoritmo de búsqueda en profundidad")
       print("5. Algoritmo A*")
       print("6. Algoritmo IDA*")
       print("7. Algoritmo A*")
       print("8. Algoritmo IDA*")
       print("9. Salir")
       opc=input("Elige una opcion: ")

       if opc=="1":
           a=A(lab)
           a.moverse()
           lab.MuestraLab()

       if opc=="2":
           ida=IDA(lab)
           ida.moverse()
           lab.MuestraLab()

       if opc=="3":
           gbfs=GBFS(lab)
           gbfs.moverse()
           lab.MuestraLab()

       if opc=="4":
           profundidad=Profundidad(lab)
           profundidad.moverse()
           lab.MuestraLab()

       if opc == "5":
           ida=IDA(lab)
           ida.moverse()
           lab.MuestraLab()

       if opc == "6":
           ida = IDA(lab)
           ida.moverse()
           lab.MuestraLab()

       if opc == "7":
           gbfs = GBFS(lab)
           gbfs.moverse()
           lab.MuestraLab()

       if opc == "8":
           ida = IDA(lab)
           ida.moverse()
           lab.MuestraLab()

       if opc=="9":
            break

if __name__=="__main__":
    main()
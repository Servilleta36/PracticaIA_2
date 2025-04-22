from Laberinto import Laberinto

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
       print("1. Agente reactivo")
       print("2. Agente informado")
       print("3. Salir")
       opc=input("Elige una opcion: ")

       if opc=="1":
           n_reac=int(input("Cuantos agentes reactivos quieres, 1 o 2: "))
           print("\n")
           fin=False

           if n_reac==1:
               a_reac=A_Reactivo(lab)
               iteraciones=0

               while iteraciones<1000:
                   a_reac.moverse()
                   iteraciones+=1

                   if a_reac.termina:
                       print("El agente reactivo ha terminado el laberinto en " + str(iteraciones) + " iteraciones")
                       print(" ")
                       fin=True
                       break

               if not fin:
                    print("El agente reactivo no ha terminado el laberinto en " + str(iteraciones) + " iteraciones")
                    print(" ")

               lab.MuestraLab()

           if n_reac==2:
                a_reac1=A_Reactivo(lab)
                a_reac2=A_Reactivo(lab)
                i=0
                iteraciones1=0
                iteraciones2=0
                terminado=False

                while i<1000:
                    if not a_reac1.termina:
                        a_reac1.moverse()
                        iteraciones1=iteraciones1+1
                    else:
                        print("El agente 1 ha llegado a la salida en "+str(iteraciones1)+" iteraciones")
                        terminado=True
                        lab.MuestraLab()
                        break

                    if not a_reac2.termina:
                        a_reac2.moverse()
                        iteraciones2=iteraciones2+1
                    else:
                        print("El agente 2 ha llegado a la salida en "+str(iteraciones2)+" iteraciones")
                        terminado=True
                        lab.MuestraLab()
                        break

                    i=i+1

                if not terminado:
                    print("Ninguno de los agentes ha terminado el laberinto")
                    lab.MuestraLab()

       if opc=="2":
            a_informado=A_Informado(lab)
            a_informado.moverse()
            lab.MuestraLab()

       if opc=="3":
            break

if __name__=="__main__":
    main()
import random

class Laberinto:
    def __init__(self):
        self.x=15#random.randint(5,20)
        self.y=15#random.randint(10,20)
        self.tab=[[" "for _ in range(self.y)]for _ in range(self.x)]

    def CreaMuro (self):
        i=0

        for i in range (self.x):
            self.tab[i][0]="#"
            self.tab[i][self.y-1]="#"

        for i in range (self.y):
            self.tab[0][i]="#"
            self.tab[self.x-1][i]="#"

    def CreaES(self):
        self.tab[random.randint(1,self.x-2)][1]="E"
        self.tab[random.randint(1,self.x-2)][self.y-2]="S"

    def CreaObstaculo(self):
        for i in range(self.x-1):
            for j in range(self.y-1):
                if self.tab[i][j]!="E" and self.tab[i][j]!="S":
                    if random.randint(0,4)==1:
                        self.tab[i][j]="#"

    def CreaLab(self):
        self.CreaMuro()
        self.CreaES()
        self.CreaObstaculo()

    def MuestraLab(self):
        i=0
        posE=0
        posS=0

        for i in range (self.x-1):
            if self.tab[i][1]=="E":
                posE=i
            if self.tab[i][self.y-2]=="S":
                posS=i

        print("La posición de la entrada es ("+str(posE)+", 1) y la de salida es ("+str(posS)+", "+str(self.y-2)+")")

        for i in range(self.x):
            for j in range(self.y):
                print(self.tab[i][j],end=" ")
            print("")

    def GuardaLab(self):
        f=open("Laberinto.txt","w")

        for i in range(self.x):
            for j in range(self.y):
                f.write(self.tab[i][j])
            f.write("\n")
        f.close()

    def CargaLab(self,fichero):
        f=open(fichero,"r")
        lineas=f.readlines()
        f.close()

        self.x=len(lineas)
        self.y = len(lineas[0].rstrip('\n'))

        self.tab=[[" "for _ in range(self.y)]for _ in range(self.x)]

        for i in range(len(lineas)):
            linea_actual = lineas[i].rstrip('\n')
            for j in range(len(linea_actual)):
                self.tab[i][j]=linea_actual[j]
from queue import PriorityQueue

class GBFS:
    def __init__(self, lab):
        self.lab=lab
        self.posE_x=0
        self.posE_y=0
        self.posS_x = 0
        self.posS_y = 0
        self.padres=[[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.visitados=[[0 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.heuristica=0

        for i in range (len(self.lab.tab)): #coordenadas de la entrada
            for j in range (len(self.lab.tab[i])):
                if self.lab.tab[i][j]=="E":
                    self.posE_x=i
                    self.posE_y=j

        for i in range (len(self.lab.tab)): #coordenadas de la salida
            for j in range (len(self.lab.tab[i])):
                if self.lab.tab[i][j]=="S":
                    self.posS_x=i
                    self.posS_y=j

    def Manhattan(self, f_actual, c_actual, posS_x, posS_y):
        return abs(posS_x-f_actual)+abs(posS_y-c_actual)

    def Euclidea(self, f_actual, c_actual, posS_x, posS_y):
        return abs(posS_x-f_actual)**2 + abs(posS_y-c_actual)**2

    def Personal(self, f_actual, c_actual, posS_x, posS_y):
        return

    def SeleccionaHeuristica(self):
        correcto=False
        while not correcto:
            print("\n")
            print("---MENU HEURISTICAS---")
            print("1. Manhattan")
            print("2. Euclidea")
            print("3. Personal")
            self.heuristica=input("Selecciona la heuristica: ")

            if self.heuristica not in ["1", "2", "3"]:
                print("No es una opcion valida")
            else:
                correcto=True

    def buscarVecino(self, f_actual, c_actual):
        direcciones=[(-1,0),(1,0),(0,-1),(0,1)]
        valido=[]

        for i,j in direcciones:
            f_siguiente=f_actual+i
            c_siguiente=c_actual+j

            if self.lab.tab[f_siguiente][c_siguiente] in (" ", ".", "S"):
                valido.append((f_siguiente, c_siguiente))
        return valido

    def moverse(self):
        self.SeleccionaHeuristica()
        heu=0
        f=0

        if self.heuristica=="1":
            heu=self.Manhattan(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="2":
            heu=self.Euclidea(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="3":
            heu=self.Personal(self.posE_x, self.posS_x, self.posS_x, self.posS_y)


        cola=PriorityQueue()
        cola.put((heu, self.posE_x,self.posE_y))
        iter=0
        while not cola.empty():
            heu,a_x,a_y=cola.get()

            if (a_x,a_y)==(self.posS_x,self.posS_y):
                print ("Se ha encontrado la salida en "+str(iter)+" iteraciones")
                return

            self.visitados[a_x][a_y]=1
            confirmados=self.buscarVecino(a_x,a_y)

            for i,j in confirmados:

                if self.heuristica=="1":
                    n_heu=self.Manhattan(i, j, self.posS_x, self.posS_y)

                elif self.heuristica=="2":
                    n_heu=self.Euclidea(i, j, self.posS_x, self.posS_y)

                elif self.heuristica=="3":
                    n_heu=self.Personal(i, j, self.posS_x, self.posS_y)

                if self.visitados[i][j]==1:
                    self.padres[i][j]=(a_x,a_y)
                    cola.put((n_heu, i, j))
            iter=iter+1

    def puntos(self):
        x,y=self.posS_x, self.posS_y
        while self.padres[x][y]is not None:
            x,y=self.padres[x][y]
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y]="."


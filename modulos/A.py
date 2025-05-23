from queue import PriorityQueue

class A:
    def __init__(self, lab):
        self.lab=lab
        self.posE_x=0
        self.posE_y=0
        self.posS_x = 0
        self.posS_y = 0
        self.padres=[[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.costeAcumulado=[[100 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
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
        Man=abs(f_actual-posS_x)+abs(c_actual-posS_y)
        direcciones=[(-1,0),(1,0),(0,-1),(0,1)]
        penalizacion=0

        for i,j in direcciones:
            nx, ny = posS_x+i, posS_y+j

            if not (0<=nx<len(self.lab.tab) and 0<=ny<len(self.lab.tab[0])):
                penalizacion=penalizacion+1

            elif self.lab.tab[nx][ny]=="#":
                penalizacion=penalizacion+1

        return Man+0.5*penalizacion

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

    def buscarVecino(self, f_actual, c_actual): #busca los posibles caminos y los guarda en validos
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
        g=0
        heu=0
        f=0

        if self.heuristica=="1":
            heu=self.Manhattan(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="2":
            heu=self.Euclidea(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="3":
            heu=self.Personal(self.posE_x, self.posS_x, self.posS_x, self.posS_y)

        f=g+heu

        cola=PriorityQueue()
        cola.put((f,g,heu, self.posE_x,self.posE_y))
        cont_max=1
        while not cola.empty():
            f,g,heu,a_x,a_y=cola.get()

            if cola.qsize()>cont_max:
                cont_max=cola.qsize()

            if (a_x,a_y)==(self.posS_x,self.posS_y):
                print ("Solución encontrada usando algoritmo A*")
                self.camino()
                print ("Nodos expandidos: "+str(self.nodos()))
                print ("Número máximo en estructura de datos COLA: "+str(cont_max))
                self.puntos()
                return

            confirmados=self.buscarVecino(a_x,a_y) #guardamos en confirmados los caminos validos teniendo en cuenta la posicion actual
            n_heu=0

            for i,j in confirmados:
                n_g=g+1

                if self.heuristica=="1": #usamos una heuristica u otra dependiendo de lo que elijamos
                    n_heu=self.Manhattan(i, j, self.posS_x, self.posS_y)

                elif self.heuristica=="2":
                    n_heu=self.Euclidea(i, j, self.posS_x, self.posS_y)

                elif self.heuristica=="3":
                    n_heu=self.Personal(i, j, self.posS_x, self.posS_y)

                n_f=n_g+n_heu

                if n_g<self.costeAcumulado[i][j]: #comparamos y vemos si g es menor que el coste acumulado, lo contamos como parte del camino final
                    self.costeAcumulado[i][j]=n_g
                    self.padres[i][j]=(a_x,a_y)
                    cola.put((n_f,n_g,n_heu, i, j))

    def puntos(self):
        x,y=self.posS_x, self.posS_y
        while (x,y)!=(self.posE_x, self.posE_y):
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y]="."
            x,y=self.padres[x][y]

    def camino(self):
        print("Camino recorrido (x,y): ")

        for i in range (len(self.padres)):
            for j in range (len(self.padres[0])):
                if self.padres[i][j] is not None:
                    print ("[",i,",",j,"],", end=" ")
        print()

    def nodos(self):
        cont=0

        for i in range (len(self.costeAcumulado)):
            for j in range (len(self.costeAcumulado[0])):
                if self.costeAcumulado[i][j]!=100:
                    cont=cont+1
        return cont





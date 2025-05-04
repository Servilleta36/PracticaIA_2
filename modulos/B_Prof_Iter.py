class Iterativa:
    def __init__(self, lab):
        self.lab = lab
        self.posE_x = 0
        self.posE_y = 0
        self.posS_x = 0
        self.posS_y = 0
        self.padres = [[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.visitados = [[0 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]

        for i in range(len(self.lab.tab)):  # coordenadas de la entrada
            for j in range(len(self.lab.tab[i])):
                if self.lab.tab[i][j]=="E":
                    self.posE_x = i
                    self.posE_y = j

        for i in range(len(self.lab.tab)):  # coordenadas de la salida
            for j in range(len(self.lab.tab[i])):
                if self.lab.tab[i][j] == "S":
                    self.posS_x = i
                    self.posS_y = j

    def buscarVecino(self, f_actual, c_actual):
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valido = []

        for i, j in direcciones:
            f_siguiente = f_actual + i
            c_siguiente = c_actual + j

            if self.lab.tab[f_siguiente][c_siguiente] in (" ", ".", "S"):
                valido.append((f_siguiente, c_siguiente))
        return valido

    def moverse(self):
        profundidad_maxima=len(self.lab.tab) * len(self.lab.tab[0])  # Para ver cual es el límite de la tabla y no pasarnos
        lim=0

        while lim<profundidad_maxima: #cada vez que salimos del bucle, empezamos en E
            self.visitados = [[0 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
            self.padres = [[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
            pila=[(self.posE_x,self.posE_y,0)]
            self.visitados[self.posE_x][self.posE_y]=1
            iter=0

            while pila:

                if pila[-1]==(self.posS_x, self.posS_y): #El -1 indica la ultima posición de la pila, es decir la posicion de la meta
                    print ("Se ha encontrado la salida en "+str(iter)+" iteraciones")
                    self.puntos()
                    return

                x,y,prof=pila.pop() #saca la ultima posición de la pila

                validos=self.buscarVecino(x, y)

                if prof<=lim:
                    for i,j in validos: #comprueba si hay caminos validos
                        if self.visitados[i][j]==0:
                            self.visitados[i][j]=1
                            self.padres[i][j]=(x,y)
                            pila.append((i,j,prof+1))
                            iter=iter+1

            lim=lim+1 #si ya no hay nada en la pila y profundidad es mayor que limite, se llega aquí y se repite el bucle de nuevo

        self.puntos()

    def puntos(self):
        x,y=self.posS_x, self.posS_y
        while (x,y)!=(self.posE_x, self.posE_y):
            if self.padres[x][y]==None:
                print ("No se ha encontrado el camino")
                return

            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y] = "*"
            x,y=self.padres[x][y]



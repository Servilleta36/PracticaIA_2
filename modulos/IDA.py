class IDA:
    def __init__(self, lab):
        self.lab=lab
        self.posE_x=0
        self.posE_y=0
        self.posS_x = 0
        self.posS_y = 0
        self.padres=[[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
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
        Man = abs(f_actual - posS_x) + abs(c_actual - posS_y)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        penalizacion = 0

        for i, j in direcciones:
            nx, ny = posS_x + i, posS_y + j

            if not (0 <= nx < len(self.lab.tab) and 0 <= ny < len(self.lab.tab[0])):
                penalizacion = penalizacion + 1

            elif self.lab.tab[nx][ny] == "#":
                penalizacion = penalizacion + 1

        return Man + 0.5 * penalizacion

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
        max=0
        g=0
        if self.heuristica=="1":
            max=self.Manhattan(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="2":
            max=self.Euclidea(self.posE_x, self.posE_y, self.posS_x, self.posS_y)

        elif self.heuristica=="3":
            max=self.Personal(self.posE_x, self.posE_x, self.posS_x, self.posS_y)


        while True:
            resultado=self.IDA(self.posE_x, self.posE_y, g, max, self.posS_x, self.posS_y, [(self.posE_x, self.posE_y)])

            if resultado=="Salida":
                print("El agente ha encontrado la salida en ",max)
                self.puntos()
                break
            elif resultado==float("inf"):
                print("El agente no ha encontrado la salida")
                break
            else:
                max=resultado



    def IDA(self, x_actual, y_actual, g, max, posS_x, posS_y, visitados):
        h=0
        if self.heuristica=="1":
            h=self.Manhattan(x_actual, y_actual, self.posS_x, self.posS_y)

        elif self.heuristica=="2":
            h=self.Euclidea(x_actual, y_actual, self.posS_x, self.posS_y)

        elif self.heuristica=="3":
            h=self.Personal(x_actual, y_actual, self.posS_x, self.posS_y)

        f=g+h

        if (x_actual, y_actual)==(posS_x, posS_y):
            return "Salida"
        elif f>max:
            return f

        min=float("inf")
        validos=self.buscarVecino(x_actual, y_actual)

        for i,j in validos:
            siguientes=(i,j)
            if siguientes not in visitados:
                visitados.append(siguientes)
                self.padres[i][j] = (x_actual, y_actual)

                resultado=self.IDA(i, j, g+1, max, self.posS_x, self.posS_y, visitados)

                if resultado=="Salida":
                    return "Salida"
                if resultado<min:
                    min=resultado

                visitados.remove(siguientes)
        return min

    def puntos(self):
        x, y = self.posS_x, self.posS_y
        while self.padres[x][y] is not None:
            x, y = self.padres[x][y]
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y] = "."
            if (x, y) == (self.posE_x, self.posE_y):
                break

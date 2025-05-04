class Bidireccional:
    def __init__(self, lab):
        self.lab = lab
        self.posE_x = 0
        self.posE_y = 0
        self.posS_x = 0
        self.posS_y = 0
        self.padres = [[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.padres2 = [[None for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.visitados = [[0 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.visitados2 = [[0 for _ in range(len(self.lab.tab[0]))] for _ in range(len(self.lab.tab))]
        self.punto_encuentro=None

        for i in range(len(self.lab.tab)):  # coordenadas de la entrada
            for j in range(len(self.lab.tab[i])):
                if self.lab.tab[i][j] == "E":
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
        pila = [(self.posE_x, self.posE_y)]
        pila2=[(self.posS_x, self.posS_y)]
        self.visitados[self.posE_x][self.posE_y]=1
        self.visitados2[self.posS_x][self.posS_y]=1
        encontrado=False
        cont_max=1


        while pila and pila2 and encontrado==False:
            camino=False
            camino2=False
            p_actual=pila[-1]
            p_actual2=pila2[-1]

            if len(pila)>cont_max:
                cont_max = len(pila)

            elif len(pila2)>cont_max:
                cont_max = len(pila2)

            validos=self.buscarVecino(p_actual[0],p_actual[1])
            validos2=self.buscarVecino(p_actual2[0],p_actual2[1])

            for i, j in validos:  # comprueba si hay caminos validos y los almacena, sino se quita de la pila
                if self.visitados2[i][j]==1:
                    encontrado=True
                    self.punto_encuentro=(i, j)
                    break

                if self.visitados[i][j]==0:
                    self.visitados[i][j]=1
                    pila.append((i, j))
                    self.padres[i][j]=p_actual

                    camino=True

            for i, j in validos2:  # comprueba si hay caminos validos y los almacena, sino se quita de la pila
                if self.visitados[i][j]==1:
                    encontrado=True
                    self.punto_encuentro=(i, j)
                    self.padres2[i][j]=p_actual2
                    break

                if self.visitados2[i][j]==0:
                    self.visitados2[i][j]=1
                    pila2.append((i, j))
                    self.padres2[i][j]=p_actual2

                    camino2=True

            if not camino:
                pila.pop()

            if not camino2:
                pila2.pop()

        if encontrado==True:
            print("Solución encontrada usando el algoritmo de busqueda en profundidad bidireccional")
            self.camino()
            print("Nodos expandidos: "+str(self.nodos()))
            print("Número máximo en estructura de datos PILA: " + str(cont_max))
            self.puntos()

    def puntos(self):
        if self.punto_encuentro is None:
            print("No se ha encontrado la salida")
            return

        # Camino desde el punto de encuentro hasta la entrada (E)
        x, y = self.punto_encuentro
        while (x, y) != (self.posE_x, self.posE_y):
            if self.padres[x][y] is None:
                break
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y] = "."
            x, y = self.padres[x][y]

        # Camino desde el punto de encuentro hasta la salida (S)
        x, y = self.punto_encuentro
        while (x, y) != (self.posS_x, self.posS_y):
            if self.padres2[x][y] is None:
                break
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y] = "."
            x, y = self.padres2[x][y]

    def camino(self):
        print("Camino recorrido (x,y): ")

        for i in range(len(self.padres)):
            for j in range(len(self.padres[0])):
                if self.padres[i][j] is not None:
                    print("[", i, ",", j, "],", end=" ")

        for i in range(len(self.padres2)):
            for j in range(len(self.padres2[0])):
                if self.padres2[i][j] is not None:
                    print("[", i, ",", j, "],", end=" ")
        print()

    def nodos(self):
        cont=0

        for i in range(len(self.visitados)):
            for j in range(len(self.visitados[0])):
                if self.visitados[i][j] != 100:
                    cont=cont+1

        for i in range(len(self.visitados2)):
            for j in range(len(self.visitados2[0])):
                if self.visitados2[i][j]!=100:
                    cont=cont+1
        return cont





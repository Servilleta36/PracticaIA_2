class Limite:
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
        lim=len(self.lab.tab) * len(self.lab.tab[0])  # Para poner un límite de exloración, qe será el limite de la tabla para que pueda encontrar la salida
        pila = [(self.posE_x, self.posE_y)]
        self.visitados[self.posE_x][self.posE_y] = 1
        cont_max=1

        while pila:
            if len(pila) > cont_max:
                cont_max = len(pila)

            camino = False

            if pila[-1] == (self.posS_x, self.posS_y):  # El -1 indica la ultima posición de la pila, es decir la posicion de la meta
                print("Solución encontrada usando el algoritmo de busqueda en profundidad con límite")
                self.camino()
                print("Nodos expandidos: " + str(self.nodos()))
                print("Número máximo en estructura de datos PILA: " + str(cont_max))
                print("Profundidad máxima alcanzada: " + str(lim))
                self.puntos()
                break

            prof=len(self.padres)-1
            if prof>=lim:
                pila.pop()
                self.padres.pop()
                continue

            p_actual = pila[-1]
            validos = self.buscarVecino(p_actual[0], p_actual[1])

            for i, j in validos:  # comprueba si hay caminos validos y los almacena, sino se quita de la pila
                if self.visitados[i][j] == 0:
                    self.visitados[i][j] = 1
                    pila.append((i, j))
                    self.padres[i][j] = p_actual

                    camino = True

            if not camino:
                pila.pop()

        self.puntos()

    def puntos(self):
        x, y = self.posS_x, self.posS_y
        while (x, y) != (self.posE_x, self.posE_y):
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y] = "."
            x, y = self.padres[x][y]

    def camino(self):
        print("Camino recorrido (x,y): ")

        for i in range(len(self.padres)):
            for j in range(len(self.padres[0])):
                if self.padres[i][j] is not None:
                    print("[", i, ",", j, "],", end=" ")
        print()

    def nodos(self):
        cont = 0

        for i in range(len(self.visitados)):
            for j in range(len(self.visitados[0])):
                if self.visitados[i][j] != 100:
                    cont = cont + 1
        return cont


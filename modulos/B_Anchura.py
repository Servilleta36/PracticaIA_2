from collections import deque
import queue

class Anchura:
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
        cola=deque() #para trabajar con colas FIFO
        cola.append((self.posE_x, self.posE_y))
        self.visitados[self.posE_x][self.posE_y]=1
        iter = 0

        while cola:
            p_actual=cola.popleft() #popleft para desencolar
            if p_actual==(self.posS_x, self.posS_y):
                print("Se ha encontrado la salida en "+str(iter)+" iteraciones")
                self.puntos()
                return

            validos=self.buscarVecino(p_actual[0], p_actual[1])

            for i, j in validos:  # comprueba si hay caminos validos y los almacena
                if self.visitados[i][j]==0:
                    self.visitados[i][j]=1
                    cola.append((i,j))
                    self.padres[i][j]=p_actual
                    iter=iter+1


        print("No se ha encontrado el camino")
        self.puntos()

    def puntos(self):
        x, y = self.posS_x, self.posS_y
        while (x,y)!=(self.posE_x, self.posE_y):
            if self.lab.tab[x][y] not in ("E", "S"):
                self.lab.tab[x][y]="."
            x,y=self.padres[x][y]

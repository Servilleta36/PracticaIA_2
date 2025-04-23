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


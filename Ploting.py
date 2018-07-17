class Grid:

    def __fill_grid(self):
        self.grid = "\n".join(list(("".join(str(el) for el in line) for line in self.matrix)))

    def __init__(self, width, height):
        self.matrix = [[0] * width for _ in range(height)]
        self.__fill_grid()

    def plot_point(self, x, y):
        self.matrix[y - 1][x - 1] = 'X'
        self.__fill_grid()

    def __repr__(self):
        return self.grid

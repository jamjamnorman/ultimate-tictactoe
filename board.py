import operator

class Board:
    def __init__(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        self.finished = False
        self.winner = None
        self.color = "white"

    def handle_input(self, x, y, player):
        if self.grid[x][y] == 0 and not self.finished:
            self.grid[x][y] = player
            self.check_complete()
            return True
        else:
            return False

    def check_complete(self):
        color = {1: "blue", 2: "red"}

        if self.finished:
            return True

        if self.grid[1][1] == self.grid[2][2] == self.grid[0][0] and self.grid[1][1]:
            self.winner = self.grid[1][1]
            self.color = color[self.winner]
            self.finished = True 
        else:
            for i in xrange(3):
                if self.grid[i][i] == 0:
                    continue
                elif self.grid[1][i] == self.grid[2][i] == self.grid[0][i] or self.grid[i][1] == self.grid[i][2] == self.grid[i][0]:
                    self.winner = self.grid[1][1]
                    self.color = color[self.winner]
                    self.finished = True
        
        if reduce(operator.mul, self.grid[1], 1) and reduce(operator.mul, self.grid[2], 1) and reduce(operator.mul, self.grid[0], 1):
            self.finished = True
            self.color = "gray"
        return False
                    
class SuperBoard(Board):
    def __init__(self):
        Board.__init__(self)
        self.grid = [[Board(),Board(),Board()],
                     [Board(),Board(),Board()],
                     [Board(),Board(),Board()]]
        self.color = None
        self.forced_grid = None

    def handle_input(self, x, y, _x, _y, player):
        if not self.forced_grid or self.forced_grid == (x, y):
            if self.grid[x][y].handle_input(_x, _y, player):
                if self.grid[_x][_y].check_complete():
                    self.forced_grid = (_x, _y)
                return True
            else:
                return False
        else:
            return False

    def check_complete(self):
        if self.grid[1][1].winner == self.grid[2][2].winner == self.grid[0][0].winner and self.grid[1][1].winner:
            self.finished = True
            return self.grid[1][1].winner
        else:
            for i in xrange(3):
                if self.grid[i][i].winner == 0:
                    continue
                elif self.grid[1][i].winner == self.grid[2][i].winner == self.grid[0][i].winner or self.grid[i][1].winner == self.grid[i][2].winner == self.grid[i][0].winner:
                    self.finished = True
                    return self.grid[i][i].winner
        """
        if reduce(operator.mul, self.grid[1], 1) and reduce(operator.mul, self.grid[0], 1) and reduce(operator.mul, self.grid[0], 1):
            self.finished = True    
            return 3
        """    
        return False
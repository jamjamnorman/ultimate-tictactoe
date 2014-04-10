import sys, pygame
from pygame.locals import *
import board

pygame.init()

color = {   "black": pygame.Color(0, 0, 0),
            "white": pygame.Color(255, 255, 255),
            "red": pygame.Color(255, 30, 30),
            "blue": pygame.Color(50, 50, 255),
            "green": pygame.Color(40, 255, 40),
            "gray": pygame.Color(200, 200, 200)}

image = {1: pygame.image.load('images\\smallx.png'), 2: pygame.image.load('images\\smallo.png')}

player_turn = 1 # 1 = crosses, 2 = naughts
game_loop = True

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Ultimate Tic Tac Toe")

main_board = board.SuperBoard()

def draw():
    if main_board.finished:
    	screen.fill(pygame.Color(200, 200, 200))
    else:
    	screen.fill(pygame.Color(255, 255, 255))

    for x in [0, 1, 2]:
        for y in [0, 1, 2]:
            pygame.draw.rect(screen, color[main_board.grid[x][y].color], (x*200, y*200, 200, 200))

            for i in [1,2]:
                pygame.draw.line(screen, color["black"], (x*200 + i*50 + 25, y*200 + 25), (x*200 + i*50 + 25, y*200 + 175), 2)
                pygame.draw.line(screen, color["black"], (x*200 + 25, y*200 + i*50 + 25), (x*200 + 175, y*200 + i*50 + 25), 2)

            for _x in [0, 1, 2]:
                for _y in [0, 1, 2]:
                    value = main_board.grid[x][y].grid[_x][_y]
                    if value:
                        screen.blit(image[value], (x*200 + _x*50 + 35, y*200 + _y*50 + 35))

    for i in [1, 2]:
        pygame.draw.line(screen, color["black"], (i*200, 0), (i*200, 600), 3)
        pygame.draw.line(screen, color["black"], (0, i*200), (600, i*200), 3)

    pygame.display.update()
def handle_click(mouse_x, mouse_y):
    board = None
    
    for x in range(3):
        for y in range(3):
            if mouse_x > (25 + x*200) and mouse_x < (175 + x*200) and mouse_y > (25 + y*200) and mouse_y < (175 + y*200):
                board = [x, y]
            else:
                print mouse_y, mouse_x

    if board:
        _x = (mouse_x - board[0]*200 - 25) / 50
        _y = (mouse_y - board[1]*200 - 25) / 50
    else:
        return False

    x, y = board

    return main_board.handle_input(x, y, _x, _y, player_turn)

draw()

while game_loop:
    for event in pygame.event.get():
        if event.type is QUIT:
            game_loop = False
        if event.type is MOUSEBUTTONUP and not main_board.finished:
            if handle_click(*event.pos):
                if main_board.check_complete():
                    print "The end. {} won!".format(["Crosses", "Noughts"][player_turn - 1])
                player_turn = 2 if player_turn == 1 else 1
                draw()
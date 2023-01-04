
import sys
import pygame

from const import *
from chessboard import ChessBoard

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
        pygame.display.set_caption('Chess')
        self.chessboard = ChessBoard()

    def mainLoop(self):

        self.chessboard.create(self.screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()

main = Main()
main.mainLoop()

import sys
import pygame

from const import *
from chessboard import ChessBoard
from dragger import Dragger
from square import Square

class Main:

    def __init__(self):
        #set screen
        pygame.init()
        self.screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
        pygame.display.set_caption('Chess')

        self.chessboard = ChessBoard()
        

    def mainLoop(self):

        #simpify name
        dragger = self.chessboard.dragger
        chessboard = self.chessboard
        screen = self.screen

        #loop
        while True:
            chessboard.showBoard(screen)
            chessboard.showPieces(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updateMouse(event.pos)

                    clicked_col= dragger.mouseX // SQUARE_SIZE
                    clicked_row = dragger.mouseY //SQUARE_SIZE

                    if chessboard.squares[clicked_row][clicked_col].has_piece():
                        chesspiece = chessboard.squares[clicked_row][clicked_col].piece
                        dragger.save_init_pos(event.pos)
                        dragger.drag_piece(chesspiece)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.updateMouse(event.pos)
                        dragger.updateBlit(screen)
                
                elif event.type == pygame.MOUSEBUTTONUP: 
                    dragger.undrag_piece()

                    dragger.updateMouse(event.pos)
                    init_col = dragger.initCol
                    init_row = dragger.initRow
                    final_col= dragger.mouseX // SQUARE_SIZE
                    final_row = dragger.mouseY //SQUARE_SIZE

                    chesspiece = chessboard.squares[init_row][init_col].piece
                    chessboard.squares[init_row][init_col].piece = None
                    chessboard.squares[final_row][final_col].piece = chesspiece
                

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if dragger.dragging:
                dragger.updateBlit(screen)

            pygame.display.update()

main = Main()
main.mainLoop()
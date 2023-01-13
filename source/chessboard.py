
from const import *
import pygame

from square import Square
from chesspiece import *
from dragger import Dragger


class ChessBoard:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0]for col in range (COLUMNS)]
        self._createBoard()
        self._addChessPiece("white")
        self._addChessPiece("black")
        self.dragger = Dragger()

    def showBoard(self, surface):
        for row in range(ROWS):
            for col in range (COLUMNS):
                if (row+col) % 2 == 0:
                    color =  (234,235,200) #ligth colour
                else:
                    color = (119, 154, 88) #dark colour
            
                rect = (col*SQUARE_SIZE, row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
                pygame.draw.rect(surface,color,rect)
    
    def showPieces(self, surface):
        for row in range(ROWS):
            for col in range (COLUMNS):
                if self.squares[row][col].has_piece():
                    piece = self.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img_center = col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)
    
    def _createBoard(self):
        for row in range (ROWS):
            for col in range (COLUMNS):
                self.squares[row][col]= Square(row,col)

    def _addChessPiece(self,team):
        row_pawns, row_other_pieces = (6,7) if team == "white" else (1,0)

        #adding pawns
        for col in range(COLUMNS):
            self.squares[row_pawns][col] = Square(row_pawns,col, Pawn(team))
        
        #adding knigths
        self.squares[row_other_pieces][1] = Square(row_other_pieces, 1, Knight(team))
        self.squares[row_other_pieces][6] = Square(row_other_pieces, 6, Knight(team))

        #adding bishops
        self.squares[row_other_pieces][2] = Square(row_other_pieces, 2, Bishop(team))
        self.squares[row_other_pieces][5] = Square(row_other_pieces, 5, Bishop(team))

        #adding rooks
        self.squares[row_other_pieces][0] = Square(row_other_pieces, 0, Rook(team))
        self.squares[row_other_pieces][7] = Square(row_other_pieces, 7, Rook(team))

        #adding king and queen
        self.squares[row_other_pieces][4] = Square(row_other_pieces, 4, King(team))
        self.squares[row_other_pieces][3] = Square(row_other_pieces, 3, Queen(team))

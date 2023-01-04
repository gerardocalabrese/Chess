
from const import *
import pygame


class ChessBoard:
    def __init__(self):
        pass

    def create(self, surface):
        for row in range(ROWS):
            for col in range (COLUMNS):
                if (row+col) % 2 == 0:
                    color =  (234,235,200) #ligth colour
                else:
                    color = (119, 154, 88) #dark colour
            
                rect = (col*SQUARE_SIZE, row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
                pygame.draw.rect(surface,color,rect)
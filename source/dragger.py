
from const import * 
from chesspiece import *
import pygame

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initRow = 0
        self.initCol = 0

    def updateBlit(self, surface):
        img = pygame.image.load(self.piece.texture)
        img_center = (self.mouseX,self.mouseY)
        texture_rect = self.piece.texture_rect= img.get_rect(center=img_center)
        surface.blit(img, texture_rect)

    def updateMouse(self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_init_pos(self, pos):
        self.initRow = pos[1] // SQUARE_SIZE
        self.initCol = pos[0] // SQUARE_SIZE

    def drag_piece(self,piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False


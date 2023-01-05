import os

class Piece:
    def __init__(self, name, team, texture = None, texture_rect = None):
        self.name = name
        self.team = team
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self):
        self.texture = os.path.join( f'img/{self.team}_{self.name}.png')

class Pawn(Piece):
    def __init__(self,team):
        super().__init__("pawn", team)

class Knight(Piece):
    def __init__(self,team):
        super().__init__("knight", team)

class Bishop(Piece):
    def __init__(self,team):
        super().__init__("bishop", team)

class Rook(Piece):
    def __init__(self,team):
        super().__init__("rook", team)

class Queen(Piece):
    def __init__(self,team):
        super().__init__("queen", team)

class King(Piece):
    def __init__(self,team):
        super().__init__("king", team)

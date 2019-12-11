from pygame import sprite
from pygame import Surface
from constants import Color


class Wall(sprite.Sprite):

    def __init__(self, w: int, h: int, x: int, y: int):
        super().__init__()

        self.image = Surface([w, h])
        self.image.fill(Color.LIGHT_BLUE)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Cube(sprite.Sprite):

    def __init__(self, mass: int, color: tuple, w: int, h: int, x: int, y: int, initspeed: float, initspeedX: int):
        if initspeedX not in (1, -1):

            print("Init speed X directs the X axis.  Positive goes -> , negative <-")

            super().__init__()

            self.image = Surface([w, h])
            self.image.fill(color)

            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = y
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

    def __init__(self, mass: int, color: tuple, w: int, h: int, x: int, y: int, initspeed: int):
        super().__init__()

        self.image = Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.mass = mass
        self.vel = initspeed
        self.pos = x
        self.rect.y = y
        self.initspeed_x = 1

    def update(self):
        self.vel *= self.initspeed_x
        self.pos -= self.vel

        self.rect.x = self.pos

    def update_speed(self, v):
        self.vel = v

    def change_x(self):
        self.initspeed_x = -self.initspeed_x

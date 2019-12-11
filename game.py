import pygame
from constants import Constants as C, Color


class Game:

    def __init__(self):
        self.running = True
        self.simulating = True

        self.screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font(C.FONT_NAME)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Pi Calculation')

    def new(self):

        self.all_sprites = pygame.sprite.LayeredUpdates()  # group that lets you specify the order sprites are drawn
        self.cubes = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()

        self._run()

    def _run(self):

        while self.simulating:

            self.clock.tick(C.FPS)
            self._events()
            self._update()
            self._draw()

    def _update(self):
        self.all_sprites.update()

    def _events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.simulating = False
                self.running = False

    def _draw(self):
        self.all_sprites.draw(self.screen)
        # self._draw_text('test', 100, Color.BLUE, 100, 200)
        pygame.display.flip()

    def _draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def _wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(C.FPS/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

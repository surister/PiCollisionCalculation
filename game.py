import pygame

from constants import Constants as C, Color
from sprites import Wall, Cube


class Game:

    def __init__(self):
        self.running = True
        self.simulating = True

        self.screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font(C.FONT_NAME)
        self.hits = 0
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Pi Calculation')

    def new(self):

        self.all_sprites = pygame.sprite.LayeredUpdates()  # group that lets you specify the order sprites are drawn
        self.cubes = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.cube_big_group = pygame.sprite.Group()

        self.wall = Cube(1000000000, Color.LIGHT_BLUE2, 200, 200, 100, C.HEIGHT-250, 0)
        self.floor = Wall(C.WIDTH, 50, 0, C.HEIGHT-50)
        self.cube = Cube(10, Color.YELLOW, 100, 100, 1000, C.HEIGHT-150, 0)
        self.cube_big = Cube(1000, Color.LIGHT_BLUE2, 200, 200, 1300, C.HEIGHT-250, 5)

        self.cubes.add(self.cube, self.cube_big)
        self.all_sprites.add(self.cube, self.cube_big, self.wall, self.floor)
        self.wall_group.add(self.wall)
        self.cube_big_group.add(self.cube_big)
        self._run()

    def _run(self):
        while self.simulating:
            self.clock.tick(C.FPS)
            self._events()
            self._update()
            self._draw()

    def get_speed_on_hit(self, actor_1, actor_2):
        actor_1_speed = actor_1.vel * (actor_1.mass - actor_2.mass) / (
                actor_1.mass + actor_2.mass) + actor_2.vel * 2.0 * actor_2.mass / (
                                actor_1.mass + actor_2.mass)

        actor_2_speed = actor_2.vel * (actor_2.mass - actor_1.mass) / (
                actor_1.mass + actor_2.mass) + actor_1.vel * 2.0 * actor_1.mass / (
                                actor_1.mass + actor_2.mass)
        return actor_1_speed, actor_2_speed

    def _update(self):
        self.all_sprites.update()

        wall_hits = pygame.sprite.spritecollide(self.cube, self.wall_group, False)
        if wall_hits:
            vel_1, vel_2 = self.get_speed_on_hit(self.cube, self.wall)
            self.cube.update_speed(vel_1)
            self.wall.update_speed(vel_2)
            self.hits += 1

        cube_hits = pygame.sprite.spritecollide(self.cube, self.cube_big_group, False)
        if cube_hits:
            vel_1, vel_2 = self.get_speed_on_hit(self.cube, self.cube_big)
            self.cube.update_speed(vel_1)
            self.cube_big.update_speed(vel_2)
            self.hits += 1
            # velsmall = self.cube.vel * (self.cube.mass - self.cube_big.mass) / (
            #         self.cube.mass + self.cube_big.mass) + self.cube_big.vel * 2.0 * self.cube_big.mass / (
            #                                self.cube.mass + self.cube_big.mass)
            #
            # velbig = self.cube_big.vel * (self.cube_big.mass - self.cube.mass) / (
            #         self.cube.mass + self.cube_big.mass) + self.cube.vel * 2.0 * self.cube.mass / (
            #                                self.cube.mass + self.cube_big.mass)


    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.simulating = False
                self.running = False

    def _draw(self):
        self._draw_text('cube_1', 30, Color.RED, self.cube.pos, self.cube.rect.y)
        self.all_sprites.draw(self.screen)

        self.screen.fill(Color.BLACK)
        self._draw_text(f'Colisiones: {str(self.hits)}', 50, Color.BLUE, 200, 10)
        self._draw_text(f'Vel cube_1: {str(self.cube_big.vel)}', 40, Color.RED, 1300, 10)
        self._draw_text(f'Vel cube_2: {str(self.cube.vel)}', 40, Color.GREEN, 1300, 50)
        self._draw_text('cube_1', 30, Color.RED, self.cube.pos + 50, self.cube.rect.y - 35)
        self._draw_text('cube_2', 30, Color.GREEN, self.cube_big.pos + 50, self.cube_big.rect.y - 35)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.rect)
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

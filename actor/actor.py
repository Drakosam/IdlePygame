import pygame
import uuid

from actor.brain import Brain
from world import WORLD_HEIGHT, WORLD_WIDTH


class Actor:
    def __init__(self, world):
        self.uuid = uuid.uuid4()
        self.pos_x = 0
        self.pos_y = 0
        self.dx = 0
        self.dy = 0
        self.speed = 5
        self.max_speed = self.speed * 4
        self.size = 0
        self.selected = False
        self.world = world
        self.energy_max = 100
        self.energy_lvl = int(self.energy_max / 2)

        self.brain = Brain(self)
        self.is_alive = True

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_size(self, size):
        self.size = size

    def update(self, ):
        if not self.is_alive:
            return
        self.energy_lvl -= 1
        self.brain.act()
        self.update_position()
        if self.energy_lvl <= 0:
            self.is_alive = False

    def redraw(self, screen):
        if self.is_alive:
            color = [255, 255, 255] if not self.selected else [255, 0, 0]
        else:
            color = [0, 0, 0]
        pygame.draw.circle(screen, color, [round(self.pos_x), round(self.pos_y)], self.size)

    def is_selected(self, pos):
        self.selected = self._is_selected(pos)

    def update_position(self):
        self.pos_x += self.dx / self.speed
        self.pos_y += self.dy / self.speed

        self.pos_x = self.pos_x if self.pos_x - self.size >= 0 else self.size
        self.pos_y = self.pos_y if self.pos_y - self.size >= 0 else self.size
        self.pos_x = self.pos_x if self.pos_x + self.size <= WORLD_WIDTH else WORLD_WIDTH - self.size
        self.pos_y = self.pos_y if self.pos_y + self.size <= WORLD_HEIGHT else WORLD_HEIGHT - self.size

    def _is_selected(self, pos):
        dx = abs(pos[0] - self.pos_x)
        dy = abs(pos[1] - self.pos_y)

        if dx ^ 2 + dy ^ 2 <= self.size ^ 2:
            return True
        return False

    def move_in_x(self, new_delta):
        self.energy_lvl -= 2
        self.dx += new_delta
        if abs(self.dx) > self.max_speed:
            if self.dx > self.max_speed:
                self.dx = self.max_speed
            else:
                self.dx = self.max_speed * (-1)

    def move_in_y(self, new_delta):
        self.energy_lvl -= 2
        self.dy += new_delta
        if abs(self.dy) > self.max_speed:
            if self.dy > self.max_speed:
                self.dy = self.max_speed
            else:
                self.dy = self.max_speed * (-1)

    def eat(self):
        self.energy_lvl -= 1
        if self.energy_max - self.energy_lvl > 10:
            self.energy_lvl += self.world.eat_from(self.pos_x, self.pos_y, 10)
        else:
            self.energy_lvl += self.world.eat_from(self.pos_x, self.pos_y, self.energy_max - self.energy_lvl)

    def idle(self):
        pass

from random import randint

import pygame
import uuid

from actor.brain import Brain


class Actor:
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.pos_x = 0
        self.pos_y = 0
        self.dx = 0
        self.dy = 0
        self.speed = 5
        self.max_speed = self.speed * 4
        self.size = 0
        self.selected = False

        self.brain = Brain(self)

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_size(self, size):
        self.size = size

    def update(self, ):
        self.update_position()

    def redraw(self, screen):
        color = [255, 255, 255] if not self.selected else [255, 0, 0]
        pygame.draw.circle(screen, color, [round(self.pos_x), round(self.pos_y)], self.size)

    def is_selected(self, pos):
        self.selected = self._is_selected(pos)

    def _update_move_speed(self):
        self.brain.act()

        if abs(self.dx) > self.max_speed:
            if self.dx > self.max_speed:
                self.dx = self.max_speed
            else:
                self.dx = self.max_speed * (-1)

        if abs(self.dy) > self.max_speed:
            if self.dy > self.max_speed:
                self.dy = self.max_speed
            else:
                self.dy = self.max_speed * (-1)

    def update_position(self):
        self._update_move_speed()
        self.pos_x += self.dx / self.speed
        self.pos_y += self.dy / self.speed

        self.pos_x = self.pos_x if self.pos_x - self.size >= 0 else self.size 
        self.pos_y = self.pos_y if self.pos_y - self.size >= 0 else self.size
        self.pos_x = self.pos_x if self.pos_x + self.size <= 800 else 800 - self.size
        self.pos_y = self.pos_y if self.pos_y + self.size <= 600 else 600 - self.size

    def _is_selected(self, pos):
        dx = abs(pos[0] - self.pos_x)
        dy = abs(pos[1] - self.pos_y)

        if dx ^ 2 + dy ^ 2 <= self.size ^ 2:
            return True
        return False

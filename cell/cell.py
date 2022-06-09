import pygame

from world import CELL_SIZE


class Cell:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.size = CELL_SIZE
        self.food = 1000
        self.food_lvl = self.food
        self.growth_rate = 5

    def eat_cell(self, x, y, value):
        if x == self.pos_x and y == self.pos_y:
            if value * 10 < self.food_lvl:
                self.food_lvl -= value * 10
                return value
            else:
                value = self.food_lvl / 10
                self.food_lvl = 0
                return int(value)
        return 0

    def growth(self):
        self.food_lvl += self.growth_rate if self.food_lvl < self.food else 0

    def redraw(self, screen):
        cell_health = round(255 * self.food_lvl / self.food)
        cell_color = [0, cell_health, 0]

        cell_pos = [
            self.pos_x * self.size,
            self.pos_y * self.size,
            self.size,
            self.size
        ]
        pygame.draw.rect(screen, cell_color, cell_pos)

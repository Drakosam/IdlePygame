from typing import List

from actor.actor import Actor
from cell.cell import Cell
from world import WORLD_HEIGHT, WORLD_WIDTH, CELL_SIZE


class World:

    def __init__(self):
        self.cell_list: List[Cell] = []
        self.actors_list: List[Actor] = [Actor(self), Actor(self)]

        for y in range(int(WORLD_HEIGHT / CELL_SIZE)):
            for x in range(int(WORLD_WIDTH / CELL_SIZE)):
                cell = Cell()
                cell.pos_x = x
                cell.pos_y = y
                self.cell_list.append(cell)

        self.actors_list[0].set_size(10)
        self.actors_list[0].set_pos(300, 200)

        self.actors_list[1].set_size(10)
        self.actors_list[1].set_pos(200, 300)

    def redraw(self, screen):
        for cell in self.cell_list:
            cell.redraw(screen)

        for actor in self.actors_list:
            actor.redraw(screen)

    def act(self):
        for actor in self.actors_list:
            actor.update()
        for cell in self.cell_list:
            cell.growth()

    def check_if_selected(self, event):
        for actor in self.actors_list:
            actor.is_selected(event.pos)

    def eat_from(self, x, y, value=0):
        ix = int(x / CELL_SIZE)
        iy = int(y / CELL_SIZE)
        add_value = 0
        for cell in self.cell_list:
            add_value += cell.eat_cell(ix, iy, value)
        return add_value

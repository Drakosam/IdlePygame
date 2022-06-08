import sys
from typing import List

import pygame

from actor.actor import Actor

pygame.init()
size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
FPS = 60

actors_list: List[Actor] = [Actor(), Actor()]
actors_list[0].set_size(10)
actors_list[0].set_pos(300, 200)

actors_list[1].set_size(10)
actors_list[1].set_pos(200, 300)
update_cycle_speed = 6
update_cycle = update_cycle_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for actor in actors_list:
                actor.is_selected(event.pos)

    screen.fill(black)
    update_cycle -= 1
    if update_cycle == 0:
        update_cycle = update_cycle_speed
        for actor in actors_list:
            actor.update()

    for actor in actors_list:
        actor.redraw(screen)

    pygame.display.flip()
    fpsClock.tick(FPS)

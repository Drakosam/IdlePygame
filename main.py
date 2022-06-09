import sys
import pygame

from world import WORLD_WIDTH, WORLD_HEIGHT
from world.world import World

if __name__ == "__main__":
    pygame.init()
    size = width, height = WORLD_WIDTH, WORLD_HEIGHT
    speed = [2, 2]
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    fpsClock = pygame.time.Clock()
    FPS = 60
    update_cycle_speed = 6
    update_cycle = update_cycle_speed

    world = World()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                world.check_if_selected(event)

        screen.fill(black)
        update_cycle -= 1
        if update_cycle == 0:
            update_cycle = update_cycle_speed
            world.act()

        world.redraw(screen)

        pygame.display.flip()
        fpsClock.tick(FPS)

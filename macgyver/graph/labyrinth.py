import pygame

from macgyver.graph.images import load_image
from macgyver.constants import SPRITE_WIDTH, SPRITE_HEIGHT

class LabyrinthDisplay(pygame.Surface):
    """Draw the walls of the labyrinth and load the wall images."""

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        super().__init__((self.labyrinth.width * SPRITE_WIDTH, self.labyrinth.height * SPRITE_HEIGHT))
        self.wall, self.wall_rect = load_image("mur.png")

        self.fill((255, 255, 255))

        for y, x in self.labyrinth.walls:
            self.blit(self.wall, (x * SPRITE_WIDTH, y * SPRITE_HEIGHT))

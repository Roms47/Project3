
import os
import sys

import pygame

from macgyver.labyrinth import Labyrinth
from macgyver.directions import right, left, up, down
from macgyver.graph.labyrinth import LabyrinthDisplay
from macgyver.graph.hero import HeroSprite
from macgyver.graph.items import ItemSprite
from macgyver.graph.guardian import GuardianSprite
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH


if not pygame.font: print('Attention, polices désactivées')
if not pygame.mixer: print('Attention, son désactivé')


class Game:
    """Create the game window and add the Hero, the items and the Guardian."""
    def __init__(self):
        pygame.init()
        
        self.labyrinth = Labyrinth()
        self.labyrinth.read_file()
        self.screen = pygame.display.set_mode((SPRITE_WIDTH * self.labyrinth.width, SPRITE_HEIGHT * (self.labyrinth.height + 1)))
        self.screen.fill((0, 0, 0))
        self.background = LabyrinthDisplay(self.labyrinth)
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(HeroSprite(self.labyrinth.macgyver))
        for item in self.labyrinth.items:
            self.allsprites.add(ItemSprite(item))
        self.allsprites.add(GuardianSprite(self.labyrinth.guardian))
        self.clock = pygame.time.Clock()
    
    def start(self):
        """Launching the game and assigning the Hero's arrow keys."""
        running = True
        while running:
            self.clock.tick(40)

            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        running = self.labyrinth.macgyver.move(left)
                    elif event.key == pygame.K_RIGHT:
                        running = self.labyrinth.macgyver.move(right)
                    elif event.key == pygame.K_UP:
                        running = self.labyrinth.macgyver.move(up)
                    elif event.key == pygame.K_DOWN:
                        running = self.labyrinth.macgyver.move(down)

            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.update()
            
        if self.labyrinth.macgyver.status == "won":
            self.display_victory_or_defeat('ressource/Victory.png')
        else:
            self.display_victory_or_defeat('ressource/Defeat.png')
    
    def display_victory_or_defeat(self, image):
        """Loads an image if the player wins or loses."""
        running = True
        while running:
            self.clock.tick(20)
            self.screen.blit(pygame.image.load(image), (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
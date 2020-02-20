import pygame

from macgyver.graph.images import load_image
from macgyver.constants import SPRITE_HEIGHT, SPRITE_WIDTH

class GuardianSprite(pygame.sprite.Sprite):
    """Determines the position of the Guardian in the labyrinth and loads an image of the Guardian."""

    def __init__(self, guardian):
        """Load the image oh the Guardian."""
        super().__init__()
        self.image, self.rect = load_image("Gardien.png", -1)
        self.guardian = guardian
        self.update()

    def update(self):
        """Determines the image position."""
        self.rect.x = self.guardian.position[1] * SPRITE_WIDTH # postion horizontale depuis le coin gauche de la fenêtre (pixels)
        self.rect.y = self.guardian.position[0] * SPRITE_HEIGHT # postion verticale depuis le haut de la fenêtre (pixels)

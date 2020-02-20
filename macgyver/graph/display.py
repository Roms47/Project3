import os, pygame
from pygame.compat import geterror

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "ressource")


def __str__(self):
    """Returns the textual form of the labyrinth for display with print."""
    laby = ""
    needle, tube, ether = self.labyrinth.item_positions
    for x in range(self.labyrinth.height):
        for y in range(self.labyrinth.width):
            if (x, y) == self.labyrinth.macgyver.position:
                laby += "M"
            elif (x, y) == self.labyrinth.guardian.position:
                laby += "G"
            elif (x, y) == needle and (x, y) not in self.labyrinth.macgyver.catch_items:
                laby += "N"
            elif (x, y) == tube and (x, y) not in self.labyrinth.macgyver.catch_items:
                laby += "T"
            elif (x, y) == ether and (x, y) not in self.labyrinth.macgyver.catch_items:
                laby += "E"
            elif (x, y) in self.labyrinth.paths:
                laby += "."
            else:
                laby += "#"
        laby += "\n"

    return laby
class LabyrinthDisplay:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def __str__(self):
        """Retourne la forme textuelle du labyrinthe pour affichage avec print."""
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
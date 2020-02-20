import random

from macgyver import hero
from macgyver import guardian
from macgyver import items
from macgyver import directions
from macgyver.constants import NUM_ITEMS

class Labyrinth:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.paths = []
        self.walls = []
        self.hero = None
        self.guardian = None
        
     

    def read_file(self):
        # ouvrir le fichier labyrinthe.txt en tant que fichier
        with open("labyrinthe.txt", "r") as file:
            # POUR chaque numéro_ligne et ligne dans fichier FAIRE
            for position_line, line in enumerate(file):
                # POUR chaque numéro_caractère et caractère DANS ligne FAIRE
                for position, character in enumerate(line):
                    # SI caractère est "D" FAIRE
                    if character == "D":
                        # self.depart <- (0, numéro_caractère)
                        self.macgyver = hero.Hero((position_line, position), self)
                        self.paths.append((position_line, position))
                    # SINON SI caractère est "." FAIRE
                    elif character == ".":
                        # Ajouter (0, numéro_caractère) à la liste self.chemins
                        self.paths.append((position_line, position))
                    # SINON SI caractère est "#" FAIRE
                    elif character == "#":
                        #  Ajouter (0, numéro_caractère) à la liste self.murs
                        self.walls.append((position_line, position))  
                    #     SINON SI caractère est "A" FAIRE
                    elif character == "A":
                    #
                        # self.arrivée <- (position_ligne, numéro_caractère)
                        self.guardian = guardian.Guardian((position_line, position), self)
                        self.paths.append((position_line, position))
                    # SINON (dans tous les autres cas)
                    else:
                        # On ne fait rien
                        pass
                # FIN POUR
            # FIN POUR
            self.width = position + 1
            self.height = position_line + 1
            
            self.item_positions = random.sample(
                set(self.paths) - {self.macgyver.position, self.guardian.position}, NUM_ITEMS
            )
            item_names = ['needle', 'ether', 'tube']
            self.items = [items.Item(self, position, name) for position, name in zip(self.item_positions, item_names)]

                




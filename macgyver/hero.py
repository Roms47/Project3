from macgyver.constants import NUM_ITEMS

class Hero:

    def __init__(self, position, labyrinth):
        
        self.position = position
        self.catch_items = []
        self.make_syringe = None
        self.labyrinth = labyrinth
        self.status = "running"
    
    def fight(self):
        if len(self.catch_items) == NUM_ITEMS:
            self.status = "won"
        else :
            self.status = "lost"


    def move(self, direction):
        """Create the starting position of the hero and the positions after movement."""
        new_position = direction(self.position)
        if new_position in self.labyrinth.paths:
            self.position = new_position
        if new_position in self.labyrinth.item_positions:
            self.catch_item()    
        if new_position == self.labyrinth.guardian.position:
            self.fight()
            return False
        return True

    def catch_item(self):
        """Moving items after picking them up."""
        self.catch_items.append(self.position)
        i = self.labyrinth.item_positions.index(self.position)
        self.labyrinth.items[i].position = (self.labyrinth.height, i)



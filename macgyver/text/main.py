from macgyver.labyrinth import Labyrinth
from macgyver.directions import right, left, up, down
from macgyver.text.display import LabyrinthDisplay



def main():
    labyrinth = Labyrinth()
    labyrinth.read_file()
    display = LabyrinthDisplay(labyrinth)
    running = True
    while running:
        print(display)
        response = input("What de you want to do: ")
        if response == "q":
            running = False
        elif response == "r":
            running = labyrinth.macgyver.move(right)
        elif response == "l":
            running = labyrinth.macgyver.move(left)
        elif response == "u":
            running = labyrinth.macgyver.move(up)
        elif response == "d":
            running = labyrinth.macgyver.move(down)
        
    if labyrinth.macgyver.status == "won":
        print("Victory")
    else:
        print("Defeat")

if __name__ == "__main__":
    main()
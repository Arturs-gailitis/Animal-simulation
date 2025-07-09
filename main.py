import random
import turtle
from World import World
from Fish import Fish
from Bear import Bear
from Plant import Plant

def mainSimulation():

    turtle.register_shape("Plant.gif")

    numberOfBears = 10
    numberOfFish = 10
    numberOfPlants = 10
    worldLifeTime = 2500
    worldWidth = 50
    worldHeight = 25

    # 1
    fish_counts = []
    bear_counts = []

    myWorld = World(worldWidth, worldHeight)
    myWorld.draw()

    for _ in range(numberOfFish):
        newFish = Fish()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newFish, x, y)

    for _ in range(numberOfBears):
        newBear = Bear()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newBear, x, y)

    for _ in range(numberOfPlants):
        newPlant = Plant()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addPlant(newPlant, x, y) 

    # 1
    for time in range(worldLifeTime):
        myWorld.liveALittle()  

        # Record current fish and bear counts
        fish_counts.append(myWorld.getFishCount())
        bear_counts.append(myWorld.getBearCount())

    #1
    # Write the collected data to a file
    with open('Statistics.txt', 'w') as file:
        file.write("Time\tFish Count\tBear Count\n")  # Headers for the file
        for time in range(worldLifeTime):
            file.write(f"{time}\t{fish_counts[time]}\t\t{bear_counts[time]}\n")  # Output format

    myWorld.freezeWorld()

mainSimulation()

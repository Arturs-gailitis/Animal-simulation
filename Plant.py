import turtle
import random

class Plant:
    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape("Plant.gif")  # Set the plant image

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__breedTick = 0  # Counter for breeding

        self.__live = 10

    def setX(self, newX):
        self.__xPos = newX

    def setY(self, newY):
        self.__yPos = newY

    def getX(self):
        return self.__xPos

    def getY(self):
        return self.__yPos

    def setWorld(self, aWorld):
        self.__world = aWorld

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def liveALittle(self):
        self.__breedTick += 1  # Increment breeding tick
        if self.__breedTick >= 5:  # If it has lived enough ticks, breed
            self.tryToBreed()
            self.__breedTick = 0  # Reset breeding tick
            self.__live = self.__live - 5
        
        if self.__live == 0:
            self.__world.delThing(self)

    def tryToBreed(self):
        # Get random coordinates within the world bounds
        randomX = random.randint(0, self.__world.getMaxX() - 1)
        randomY = random.randint(0, self.__world.getMaxY() - 1)

        if self.__world.emptyLocation(randomX, randomY):  # Check if the location is empty
            # Create a new Plant
            newPlant = Plant()  
            newPlant.setWorld(self.__world)  # Set the world for the new plant
            newPlant.setX(randomX)  # Set position
            newPlant.setY(randomY)
            self.__world.addThing(newPlant, randomX, randomY)  # Add to the world
            newPlant.appear()  # Make it visible
            self.__breedTick = 0  # Reset breeding tick


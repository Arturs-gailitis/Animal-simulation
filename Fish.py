import turtle
import random
from Plant import Plant

class Fish:
    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape("Fish.gif")

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__breedTick = 0

        #2
        # Set enery level to 10
        self.__energyLevel = 10

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

    def move(self, newX, newY):
        self.__world.moveThing(self.__xPos, self.__yPos, newX, newY)
        self.__xPos = newX
        self.__yPos = newY
        self.__turtle.goto(self.__xPos, self.__yPos)

    def liveALittle(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        adjFish = 0  #count adjacent Fish
        for offset in offsetList:
            newX = self.__xPos + offset[0]
            newY = self.__yPos + offset[1]
            if 0 <= newX < self.__world.getMaxX()  and \
                  0 <= newY < self.__world.getMaxY():
                if (not self.__world.emptyLocation(newX, newY)) and \
                    isinstance(self.__world.lookAtLocation(newX, newY), Fish):
                    adjFish = adjFish + 1

        if adjFish >= 2:   #if 2 or more adjacent Fish, die
            self.__world.delThing(self)
        else:
            self.__breedTick = self.__breedTick + 1
            if self.__breedTick >= 12:  #if alive 12 or more ticks, breed
                self.tryToBreed()

            self.tryToMove()            #try to move

            self.tryToEat()

    def tryToBreed(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextX = self.__xPos + randomOffset[0]
        nextY = self.__yPos + randomOffset[1]
        while not (0 <= nextX < self.__world.getMaxX() and \
                   0 <= nextY < self.__world.getMaxY() ):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextX = self.__xPos + randomOffset[0]
            nextY = self.__yPos + randomOffset[1]

        if self.__world.emptyLocation(nextX, nextY):
           childThing = Fish()
           self.__world.addThing(childThing, nextX, nextY)
           self.__breedTick = 0   

           #2
           #Because of breeding the energy level goes down by 1
           self.__energyLevel = self.__energyLevel - 1

    def tryToMove(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextX = self.__xPos + randomOffset[0]
        nextY = self.__yPos + randomOffset[1]
        while not(0 <= nextX < self.__world.getMaxX() and \
                  0 <= nextY < self.__world.getMaxY() ):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextX = self.__xPos + randomOffset[0]
            nextY = self.__yPos + randomOffset[1]

        if self.__world.emptyLocation(nextX, nextY):
           self.move(nextX, nextY)

           #2
           #Because of moving the energy level goes down by 1
           self.__energyLevel = self.__energyLevel - 1
    
    def tryToEat(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1), (0,-1), (1,-1)]
        adjPlants = []  

        #2
        # Look for adjacent plants to eat
        for offset in offsetList:
            newX = self.__xPos + offset[0]
            newY = self.__yPos + offset[1]
            if 0 <= newX < self.__world.getMaxX() and \
               0 <= newY < self.__world.getMaxY():
                if (not self.__world.emptyLocation(newX, newY)) and \
                   isinstance(self.__world.lookAtLocation(newX, newY), Plant):
                    adjPlants.append(self.__world.lookAtLocation(newX, newY))
        

        if len(adjPlants) > 0:  # If there are any plants adjacent, eat one
            randomPlant = random.choice(adjPlants)
            self.__world.delThing(randomPlant)  # Remove the plant from the world
            self.__energyLevel =  10  # Increase energy level to 10 for eating a plant
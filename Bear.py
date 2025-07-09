import turtle
import random
from Fish import Fish

class Bear:
    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape("Bear.gif")

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__starveTick = 0
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
           childThing = Bear()
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

    def liveALittle(self):
        self.__breedTick = self.__breedTick + 1
        if self.__breedTick >= 8:  #if alive 8 or more ticks, breed
            self.tryToBreed()

        self.tryToEat()

        if self.__starveTick == 10:  #if not eaten for 10 ticks, die
            self.__world.delThing(self)
        
        #2
        #If energy level goes down to 0, the bear dies
        elif self.__energyLevel <= 0:
            self.__world.delThing(self)
        
        else:
            self.tryToMove()

    def tryToEat(self):
        offsetList = [(-1,1), (0,1) ,(1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        adjPrey = []     #create list of adjacent prey
        for offset in offsetList:
            newX = self.__xPos + offset[0]
            newY = self.__yPos + offset[1]
            if 0 <= newX < self.__world.getMaxX() and \
               0 <= newY < self.__world.getMaxY():
                if (not self.__world.emptyLocation(newX, newY)) and  \
		          isinstance(self.__world.lookAtLocation(newX, newY), Fish):
                    adjPrey.append(self.__world.lookAtLocation(newX, newY))

        if len(adjPrey) > 0:  #if any Fish are adjacent, pick random Fish to eat
            randomPrey = adjPrey[random.randrange(len(adjPrey))]
            preyX = randomPrey.getX()
            preyY = randomPrey.getY()

            self.__world.delThing(randomPrey)  #delete the Fish
            self.move(preyX, preyY)            #move to the Fishs location
            self.__starveTick = 0
            
            #2
            #Because of eating the energy level goes up to 1
            self.__energyLevel = 10

        else:
            self.__starveTick = self.__starveTick + 1

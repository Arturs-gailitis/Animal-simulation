import turtle
import random
from Fish import Fish
from Bear import Bear

class World:
    def __init__(self, mX, mY):
        self.__maxX = mX
        self.__maxY = mY
        self.__thingList = []
        self.__grid = []

        for aRow in range(self.__maxY):
            row = []
            for aCol in range(self.__maxX):
                row.append(None)
            self.__grid.append(row)

        self.__wTurtle = turtle.Turtle()
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(0, 0, self.__maxX - 1, 
                                           self.__maxY - 1)
        self.__wScreen.addshape("Bear.gif")
        self.__wScreen.addshape("Fish.gif")
        self.__wTurtle.hideturtle()
        
    def draw(self):
        self.__wScreen.tracer(0)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        for i in range(self.__maxY - 1):
            self.__wTurtle.forward(self.__maxX - 1)
            self.__wTurtle.backward(self.__maxX - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wTurtle.forward(1)
        self.__wTurtle.right(90)
        for i in range(self.__maxX - 2):
            self.__wTurtle.forward(self.__maxY - 1)
            self.__wTurtle.backward(self.__maxY - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wScreen.tracer(1)

    def addThing(self, aThing, x, y):
        aThing.setX(x)
        aThing.setY(y)
        self.__grid[y][x] = aThing       #add life-form to grid
        aThing.setWorld(self)
        self.__thingList.append(aThing)  #add to list of life-forms
        aThing.appear()

    def delThing(self, aThing):
        aThing.hide()
        self.__grid[aThing.getY()][aThing.getX()] = None
        self.__thingList.remove(aThing)

    def moveThing(self, oldX, oldY, newX, newY):
        self.__grid[newY][newX] = self.__grid[oldY][oldX]
        self.__grid[oldY][oldX] = None

    def getMaxX(self):
        return self.__maxX

    def getMaxY(self):
        return self.__maxY

    def liveALittle(self):
        if self.__thingList != [ ]:
           aThing = random.randrange(len(self.__thingList))
           randomThing = self.__thingList[aThing]
           randomThing.liveALittle()

    def emptyLocation(self, x, y):
        if self.__grid[y][x] == None:
            return True
        else:
            return False

    def lookAtLocation(self, x, y):
        return self.__grid[y][x]

    def freezeWorld(self):
        self.__wScreen.exitonclick()
    
    #1
    def getFishCount(self):
        
        fishcount = sum(1 for thing in self.__thingList if isinstance(thing, Fish))
        
        return fishcount
    
    #1
    def getBearCount(self):

        bearcount = sum(1 for thing in self.__thingList if isinstance(thing, Bear))

        return bearcount
    
    def addPlant(self, aPlant, x, y):
        aPlant.setX(x)
        aPlant.setY(y)
        self.__grid[y][x] = aPlant  # add plant to grid
        aPlant.setWorld(self)
        self.__thingList.append(aPlant)  # add to list of life-forms
        aPlant.appear()

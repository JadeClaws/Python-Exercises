from turtle import Turtle, Screen, TurtleScreen

class TriangularFractal(object):    
    TurtleScreen._RUNNING = True # to avoid crashes and Terminator exceptions
    
    screen      = Screen()
    turtle      = Turtle()
    
    
    def init(self):
        "sets init values and parameters of turtle object"
        
        self.startPosX   = -250
        self.startPosY   = -250        
        self.length      = 600
        self.angle       = 120
        self.percent     = 0.50
        
        self.turtle.speed("fastest")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(self.startPosX, self.startPosY)
        self.turtle.pendown()
        return

    def calcStartPos(self, x1, y1, x2, y2):
        "calculates middle point of section"
        
        return (((x1 + x2) / 2), ((y1 + y2) / 2))

    def drawSubShape(self, qty, length, posX, posY, side):
        "draws subshape of fractal (called recursively)"
        
        positions = {"LEFT": (0, 0),
                    "RIGHT": (0, 0),
                    "UPPER": (0, 0)}
        
        if (side == "LEFT"):
            angle = 60
        elif (side == "RIGHT"):
            angle = -180
        elif (side == "UPPER"):
            angle = -60
        
        l = length * self.percent
        
        # set pos, draw subshape and get postions for next subshapes
        self.turtle.penup()
        self.turtle.setpos(posX, posY)
        self.turtle.setheading(angle)
        self.turtle.pendown()
        
        for i in range(3):
            (x1, y1) = self.turtle.pos() # start point
            self.turtle.left(self.angle)
            self.turtle.forward(l)
            (x2, y2) = self.turtle.pos() # end point
            
            # calculate positions by drawn subshape and current side
            if (side == "LEFT"):
                if   (i == 0): positions["UPPER"] = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 1): positions["LEFT"]  = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 2): positions["RIGHT"] = self.calcStartPos(x1, y1, x2, y2)
            elif (side == "RIGHT"):
                if   (i == 0): positions["LEFT"]  = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 1): positions["RIGHT"] = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 2): positions["UPPER"] = self.calcStartPos(x1, y1, x2, y2)
            elif (side == "UPPER"):
                if   (i == 0): positions["RIGHT"] = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 1): positions["UPPER"] = self.calcStartPos(x1, y1, x2, y2)
                elif (i == 2): positions["LEFT"]  = self.calcStartPos(x1, y1, x2, y2)
                
        # recursion exit condition
        if (qty == 0):
            return

        # draw three subshapes for current subshape
        (posX, posY) = positions["LEFT"]
        self.turtle.color('#DD0000') # red
        self.drawSubShape(qty - 1, l, posX, posY, "LEFT")
        (posX, posY) = positions["RIGHT"]
        self.turtle.color('#BB00FF') #purple
        self.drawSubShape(qty - 1, l, posX, posY, "RIGHT")
        (posX, posY) = positions["UPPER"]
        self.turtle.color('#6666FF') # blue
        self.drawSubShape(qty - 1, l, posX, posY, "UPPER")
    
    
    def draw(self, qty):
        "draws fractal"
        
        self.init()
        
        # draw first triangle
        for i in range(3):
            self.turtle.forward(self.length)
            self.turtle.left(self.angle)
          
        # calculate start position for next triangle
        (posX, posY) = self.calcStartPos(self.startPosY, self.startPosY,
                                         self.startPosX + self.length, self.startPosY)
        
        # draw subshapes recursively
        if (qty >= 1):
            self.drawSubShape(qty - 1, self.length, posX, posY, "UPPER")

        self.screen.mainloop() # end statement
        return


triangularFractal = TriangularFractal()
triangularFractal.draw(7)






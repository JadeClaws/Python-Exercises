from turtle import Turtle, Screen, TurtleScreen


class RectangularFractal(object):
    TurtleScreen._RUNNING = True # to avoid crashes and Terminator exceptions
    
    screen      = Screen()
    turtle      = Turtle()
    
    def init(self):
        "sets start position, lenght of most outer rectangle and parameters of turtle object"
        self.startPosX   = -250
        self.startPosY   = -250        
        self.length      = 600
        self.angle       = 90
        self.percent     = 0.90
        
        self.turtle.speed("fastest")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(self.startPosX, self.startPosY)
        self.turtle.pendown()
        return
    
    def drawSubShape(self, _qty, _length):
        "draws sub shape of fractal"
        length = _length * self.percent # shrink next sub shape of fractal

        if (_qty == 0):
            return

        self.drawSubShape(_qty - 1, length)

        self.turtle.setpos(self.startPosX, self.startPosY)

        for i in range(4):        
            self.turtle.forward(length)
            self.turtle.left(self.angle)

    
    def draw(self, qty):
        "draws fractal, calls method that draw sub rectangles"
        self.init()        
        self.drawSubShape(qty, self.length)       
        self.screen.mainloop() # end statement
        return
    

rectangularFractal = RectangularFractal()
rectangularFractal.draw(60)




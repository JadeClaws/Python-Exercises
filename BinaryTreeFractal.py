from turtle import Turtle, Screen, TurtleScreen


class BinaryTreeFractal(object):
    TurtleScreen._RUNNING = True # to avoid crashes and Terminator exceptions
    
    turtle = Turtle()
    screen = Screen()
    
    def init(self, qty, animation):      
        "sets initial values and parameters of turtle object"
        
        self.initQty        = qty   #initial quantity of recursive steps
        self.startPosX      = 0     # start pos (root pos)
        self.startPosY      = -350  # start pos (root pos)
        self.length         = 150   # initial length
        self.colorThreshold = round(qty * 0.25, 0) # defines where color changes to leaf color
        self.percent        = 0.75  # percent of shrink
        self.initAngle      = 90    # initial angle
        self.angle          = 30    # branch angle
        
        if (not animation):
            self.screen.tracer(0, 0)
        
        self.turtle.speed("fastest")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.pensize(2)
        self.turtle.setpos(self.startPosX, self.startPosY)
        self.turtle.setheading(90)
        self.turtle.pendown()
        return
    
    def drawSubShape(self, qty, length, angle):
        "draws subtrees"
        
        if (qty == 0): # recursion exit condition
            return        
        
        # set color
        if (qty <= self.colorThreshold):
            self.turtle.color("green")
        else:
            self.turtle.color("brown")
        
        l = length * self.percent
        
        self.turtle.right(angle)
        self.turtle.forward(l)
        
        # draw two branches
        (posX, posY) = self.turtle.pos()
        heading = self.turtle.heading()
        self.drawSubShape(qty - 1, l, -self.angle) # left branch
        self.turtle.penup()
        self.turtle.setpos(posX, posY)
        self.turtle.setheading(heading)
        self.turtle.pendown()
        self.drawSubShape(qty - 1, l, self.angle) # right branch
        
        return

    
    def draw(self, qty, animation = True):
        "draws fractal, calls method that draw subtrees"
        
        self.init(qty, animation)        
        
        
        self.drawSubShape(qty, self.length, 0)      
        
        self.screen.update()
        
        self.screen.mainloop() # end statement
        return
    
    
binaryTreeFractal = BinaryTreeFractal()
binaryTreeFractal.draw(9, True)



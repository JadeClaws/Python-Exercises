from turtle import Turtle, Screen, TurtleScreen


class DragonCurveFractal(object):
    TurtleScreen._RUNNING = True # to avoid crashes and Terminator exceptions
    
    turtle = Turtle()
    screen = Screen()
    
    # angles for .setHeading()
    dir2angle = {"U":  90, # UP
                 "D": 270, # DOWN
                 "L": 180, # LEFT
                 "R":   0} # RIGHT
    
    angle2dir = { 90: "U", # UP
                 270: "D", # DOWN
                 180: "L", # LEFT
                   0: "R"} # RIGHT
    
    def init(self, animation):      
        "sets initial values and parameters of turtle object"

        self.startPosX = 0
        self.startPosY = 0
        self.length    = 5
        self.angle     = 90

        if (not animation):
            self.screen.tracer(0, 0)

        self.turtle.speed("fastest")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.pensize(2)
        self.turtle.color("red")
        self.turtle.setpos(self.startPosX, self.startPosY)
        self.turtle.pendown()
        return
    
    def drawSubShape(self, qty, directions, fold):      
        "draws next fold of dragon curve fractal"
              
        if (qty <= 0): # recursion exit condition
            return
        
        newDirections = directions
        
        # reverse list of directions
        reversedDirections = directions[::-1]
        
        # draw
        for i in reversedDirections:
            if (fold == "FOLD_LEFT"):
                angle = (self.dir2angle[i] - 90) % 360              
            elif (fold == "FOLD_RIGHT"):
                angle = (self.dir2angle[i] + 90) % 360
  
            newDirections += self.angle2dir[angle]
            self.turtle.setheading(angle)
            self.turtle.forward(self.length)

        self.drawSubShape(qty - 1, newDirections, fold)
            
        return
  
    def draw(self, qty, dragons = 1, animation = True):
        "draws fractal, calls method that draw subparts"
        
        colors      = ["red", "blue", "green", "purple"]
        directions  = ["D", "L", "U", "R"]
        
        self.init(animation)        
        self.screen.bgcolor("black")
        
        if qty >= 1 and dragons in [1, 2, 3, 4]:
            for i in range(dragons):
                color     = colors[i]
                direction = directions[i]
                
                # draw first line
                self.turtle.penup()
                self.turtle.setpos(0, 0)
                self.turtle.setheading(self.dir2angle[direction])
                self.turtle.color(color)
                self.turtle.pendown()                
                self.turtle.forward(self.length)
        
                # recursive drawing of next folds
                self.drawSubShape(qty - 1, direction, "FOLD_LEFT")
        
        self.screen.mainloop() # end statement
        return
     
dragonCurveFractal = DragonCurveFractal()
dragonCurveFractal.draw(14, 4, True)



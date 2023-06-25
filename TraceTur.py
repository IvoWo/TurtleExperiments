
# TO DO: use turtle.clear() on drawing and cleaning turtle to increase program speed
#        use another turtle to keep the visible trace visible on drawing turtle.clear
# idea: 2 drawing turtles drawing the same line, 2 cleaning turtles drawing the same line 
#       turtle.clear() switching between either of those 2 to keep drawn line short but 
#       lines visible
#       clears can happen every TraceTur.tracelengths steps
#       perhaps simply use 2 TraceTurs



import turtle as tur

#hinterlässt eine Spur, die wieder verblasst, diese Funktionalität soll an die Forward Methode der Turtle Klasse 
#gebunden werden
class TraceTur(tur.Turtle):
    def __init__ (self, tracelength):
        super().__init__()
        self.tracelength = tracelength
    
     #eine Spur mit Schrittangaben. Enthält pro Schritt die Position, die Richtung, die gelaufene Distanz
    Trace = []
    
    #adds a Footprint to the Trace-list
    def addTrace(self, distance):
        self.Trace.append((self.xcor(), self.ycor(),self.heading(), distance))

    cleaner = tur.Turtle()
    cleaner.hideturtle()

    def setbgcolor(self, backgoundcolor):
        self.cleaner.color(backgoundcolor)

    def vanishTrace(self):
        if len(self.Trace) > self.tracelength:
            self.cleaner.pu()
            self.cleaner.goto(self.Trace[0][0],self.Trace[0][1])
            self.cleaner.seth(self.Trace[0][2])
            self.cleaner.pd()
            self.cleaner.forward(self.Trace[0][3])
            self.Trace.pop(0)

    def vanishTraceBasic(self):
        self.cleaner.pu()
        self.cleaner.goto(self.Trace[0][0],self.Trace[0][1])
        self.cleaner.seth(self.Trace[0][2])
        self.cleaner.pd()
        self.cleaner.forward(self.Trace[0][3])
        self.Trace.pop(0)
    
    def forward(self, distance: float) -> None:
        self.addTrace(distance)
        return super().forward(distance)
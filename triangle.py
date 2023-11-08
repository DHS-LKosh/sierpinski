import time, math, turtle

#Set up of the turtle
frank = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

#Defining our recursive method
def triangle(x, y, length):
    #Base Case - Stope when the triangles are tiny
    if length < 30:
        return

    #Move to (x,y) - bottom left corner
    frank.penup()
    frank.goto(x,y)
    frank.pendown()

    #Making the triangle a pretty colour
    frank.color(int(x/2%255), int(y/2%255), 100)

    #Drawing our current step -> A single triangle
    frank.begin_fill()
    for i in range(3):
        frank.fd(length)
        frank.lt(120)
    frank.end_fill()
    
    #Recursive calls
    triangle(x, y, length/2) #Bottom left
    triangle(x+length/2, y, length/2) #Bottom right
    triangle(x + length/4, y + int(math.sqrt(3)* length)/4, length/2)

    
#initial method call
triangle(0, 0, 500)
time.sleep(10000)

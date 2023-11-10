import turtle
import time
import sys

# Function to handle turtle movement
def move_turtle():
    # converts stime to intervals (1 interval = 1 second)
    intervals = int(stime)
    counter = 0

    # Move the turtle in intervals with a delay of 1 second between each movement
    for _ in range(intervals):
        # Move the turtle forward to cover a specific distance in each interval (Seconds)
        alarm.forward(500 / intervals)
        # Wait for 1 second before the next movement
        time.sleep(1)
        counter += 1
        # Display a message on the Turtle canvas
    if counter == intervals:
        timer = turtle.Turtle()
        timer.penup()
        timer.hideturtle()
        timer.goto(0 , 100)
  
        timer.write("Times up!", align="center", font=("Arial", 16, "normal"))      

# Order if the button is pressed
def start_movement(x,y):
    button.hideturtle()
    word.undo()
    time_checker.undo()
    move_turtle()
    
print("[ 1 ] Seconds \n[ 2 ] Minutes (max of 59 minutes) \n[ 3 ] Hours (Max of 24 hours)")
choice = float(input("What type of Alarm?"))
if choice > 0:
    if choice == 1: # Seconds Choice
        stime = float(input("Enter the time (in Seconds): "))
        if stime.is_integer() and 0 < stime < 86400:  # Check if it's a whole number and within the valid range
            print("Start your alarm by pressing the button in Turtle Graphics.")
        elif not stime.is_integer():
            print("This program cannot alarm you in milliseconds. Please enter whole numbers only")
            sys.exit
            turtle.bye()
        else:
            print("The Time you entered exceeded 24 hours. Reminder 24 hours is the max.")
            sys.exit
            turtle.bye()

    elif choice == 2: # Minutes Choice
        mtime = float(input("Enter the time (in Minutes): "))
        stime = mtime * 60
        if mtime > 1440:
            print("The Time you entered exceeded 24 hours. Reminder 24 hours is the max.") # A Limit of 1 day only
            sys.exit
            turtle.bye()

    elif choice == 3: # Hours Choice
        htime = float(input("Enter the time (in Hours): "))
        stime = htime * (60 * 60)
        if htime > 24:
            print("The Time you entered exceeds 24 hours. Reminder 24 is the max.") # A Limit of 1 day only
            sys.exit
            turtle.bye()

    else:
        print("Invalid Input. Enter only from 1 to 3.")
        sys.exit
        turtle.bye()

else:
    print("Invalid Input. Enter only from 1 to 3")
    sys.exit
    turtle.bye()

#canvas
bg = turtle.Screen()
bg.setup(width=800, height=350)
bg.bgcolor("#C2b280")

# Create a turtle object
alarm = turtle.Turtle()
alarm.turtlesize(5)
alarm.shape("turtle")
alarm.color("green")
alarm.penup()
alarm.goto( -250, 0)
alarm.speed(1)

#ocean first so that the wave can overlap the ocean
#Ocean
blue = turtle.Turtle()
blue.hideturtle()
blue.speed(0)
blue.fillcolor("blue")
blue.penup()
blue.goto(260,175)
blue.begin_fill()
blue.pendown()
blue.goto(400,175)
blue.goto(400,-185)
blue.goto(260,-185)
# fills blue of the gaps of the ocean
blue.goto(260,-165)
blue.goto(245,-160)
blue.goto(245,-150)
blue.goto(260,-140)
blue.goto(260,-127)
blue.goto(245,-117)
blue.goto(260,-100)
blue.goto(260,-87)
blue.goto(245,-77)
blue.goto(260,-62)
blue.goto(260,-47)
blue.goto(245,-40)
blue.goto(245,-35)
blue.goto(260,-25)
blue.goto(260,-7)
blue.goto(245,0)
blue.goto(245,7)
blue.goto(260,15)
blue.goto(260,33)
blue.goto(245,40)
blue.goto(245,50)
blue.goto(260,55)
blue.goto(260,72)
blue.goto(245,78)
blue.goto(245,90)
blue.goto(260,100)
blue.goto(260,112)
blue.goto(245,122)
blue.goto(245,130)
blue.goto(260,140)
blue.goto(260,152)
blue.goto(245,162)
blue.goto(245,172)
blue.goto(260,175)

# Wave Effects of the ocean and on the sands
wave = turtle.Turtle()
wave.hideturtle()
wave.speed(0)
wave.penup()
wave.fillcolor("white")
wave.goto(250,175)
wave.begin_fill()
wave.pendown()
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.penup()
wave.goto(250,175)
wave.pendown()
wave.forward(10)
wave.penup()

wave.goto(260,175)
wave.pendown()
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.right(180)
wave.circle(10, 180)
wave.left(180)
wave.circle(10, -180)
wave.backward(10)
wave.end_fill()
blue.end_fill()

# the text under the path of the turtle
button = turtle.Turtle()
word = turtle.Turtle()
button.penup()
word.penup()
button.shape("square")
button.goto(-100, -90)  # Position the button under the turtle's path | the button to start the turtle to move
word.hideturtle()
word.goto(0, -100)
word.write("Start Moving Turtle", align="center", font=("Arial", 14, "normal"))

time_checker = turtle.Turtle()
time_checker.penup()
time_checker.goto(0, -130)
time_checker.hideturtle()


# Tells us the time the user wants to alarm in the canvas
if choice == 1: #Seconds Choice
    if stime in range( 0 , 60): # seconds, reads 1 to 59 seconds.
        time_output = f"The alarm is set in {stime} Second/s"
    elif stime in range( 59 , 3600): # minutes, reads 60 seconds ( 1 minute ) to 3599 seconds (less 1 hour ).
        Converted_Minute = stime // 60
        Remaining_seconds = stime % 60
        time_output = f"The alarm is set in {Converted_Minute} Minute/s and {Remaining_seconds} Second/s"
    elif stime in range( 3599 , 86400): # hours, reads 3600 seconds ( 1 hour ) to 86399 ( less than 1 day ).
        Converted_Hour = stime // ( 60 * 60 )
        Remaining_hour = stime % ( 60 * 60)
        Converted_Minute = Remaining_hour // 60
        Remaining_seconds = stime % 60
        time_output = f"The alarm is set in {Converted_Hour} Hour/s and {Converted_Minute} Minute/s and {Remaining_seconds} Second/s"

elif choice == 2: #Minutes Choice
    if mtime in range(0, 60): # minutes, reads 1 minute to 59 minutes.
        time_output = (f"The alarm is set in {mtime} Minute/s")
    elif 0 < mtime < 60: # decimal input
        Converted_Minute = int(mtime) # converts to int
        Remaining_seconds = (  mtime - Converted_Minute) * 60  # to convert the decimal to seconds.
        time_output = f"The alarm is set in {Converted_Minute} Minute/s and {Remaining_seconds} Second/s"


    elif mtime in range(59, 1440): # hours, reads 60 minutes ( 1 hour ) to 1439 Hours (Less than a day ).
        Converted_Hour = mtime // 60
        Remaining_minute = mtime % 60
        time_output = f"The alarm is set in {Converted_Hour} Hour/s and {Remaining_minute} Minute/s"
    elif 59 < mtime < 1440: # decimal input
        Converted_Hour = int(mtime) // 60  # converts to int
        Remaining_Minute = int(mtime) % 60  # getting the remaing minutes
        Decimal_Part = mtime - int(mtime)  # getting the remaining seconds
        Remaining_Seconds = int(Decimal_Part * 60)  # Converts the decimal to seconds
        time_output = f"The alarm is set in {Converted_Hour} Hour/s, {Remaining_Minute} Minute/s, and {Remaining_Seconds} Second/s."


elif choice == 3: #Hours Choice
    if htime in range(0, 25):
        time_output = (f"The alarm is set in {htime} Hours")
    elif 0 < htime < 25:
        Converted_Hour = int(htime)  # Converts it to int
        decimal_part = htime - Converted_Hour  # getting the remaining minutes
        converted_minutes = int(decimal_part * 60)  # Convert decimal hours to minutes
        remaining_seconds = int((decimal_part * 60 - converted_minutes) * 60)
        time_output = f"The alarm is set in {Converted_Hour} Hour/s, {converted_minutes} Minute/s, and {remaining_seconds} Second/s."


time_checker.write(time_output, align="center", font=("Arial", 14, "normal"))


# The button to start the movement
button.onclick(start_movement)

turtle.done()
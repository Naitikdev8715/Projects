import turtle # Bring in the turtle drawing tools

# 1. Set up the turtle
artist = turtle.Turtle()
artist.shape("turtle") # You can see your turtle now!
artist.color("blue")   # Let's make it blue

# 2. Draw the square using a loop
for side in range(4): # This loop will run 4 times, once for each side
    artist.forward(100) # Move forward 100 steps
    artist.right(90)    # Turn right 90 degrees

# 3. Keep the window open until you close it
turtle.done()
"""
Create the classic Flappy Bird game!
"""

def setup():
    pass
    # 1. Use the size(width, height) function to set the width and height
    # of the game window
    size(800, 600)
    
    # 2. Remove the comment (the '#') in the line below 
    global bg, bird, lower_pipe, upper_pipe
    
    # 3. Use the loadImage function to inialize the 'bg' variable with the
    # flappyBackground.jpg image
    bg = loadImage("flappyBackground.jpg") 
    
    # 4. Use the bg variable's resize(width, height) method to set
    # the background to the width and height of the game window
    bg.resize(width, height)
    
    # 5. Initialize the 'bird' variable using the Bird class defined below
    bird = Bird('bird.png', 100, height/2)
    
    # 6. Initialize the 'lower_pipe' and 'upper_pipe' variables using
    # the Pipe class defined below.
    lower_pipe = Pipe("lower_pipe.png") # and "lower_pipe.png"
    upper_pipe = Pipe("upper_pipe.png")

    # 7. Call the reset_pipes(lower_pipe, upper_pipe) function to set
    # the initial positions of the pipes
    reset_pipes(lower_pipe, upper_pipe)

def draw():
    pass
    # 8. Use the background() function to draw the game's background
    # Do you see the background when you run the program?
    background(bg)

    # 9. Call the bird's draw() method.
    # Do you see the bird when you run the program?
    bird.draw()
    
    # 10. Change the bird's y variable so that the bird slowly falls
    # down when the game runs. This is the game's gravity.
    bird.y += 2
    
    # 11. Use and if statement and the mousePressed variable to move
    # the bird's y variable upwards when the mouse is pressed
    # Does the bird jump up when the mouse is pressed?
    if mousePressed:
        bird.y -= 6

    # 12. Call the upper and lower pipe's update methods.
    lower_pipe.update()
    upper_pipe.update()
    
    # 13. Call the upper and lower pipe's draw methods. 
    # Do the pipes move across the screen?
    lower_pipe.draw()
    upper_pipe.draw()

    # 14. Call the reset_pipes function defined below when the pipes
    # move past the screen (lower_pipe.x < 0) to reset their position.
    if lower_pipe.x < 0:
        reset_pipes(lower_pipe, upper_pipe)

    # 15. Use an if statement along with the
    # intersects_pipes(bird, lower_pipe, upper_pipe) function defined
    # below to check if the bird collided with one of the pipes.
    if intersects_pipes(bird, lower_pipe, upper_pipe):
        
        # 16. If there's a collision, stop the game by calling noLoop()
        noLoop()
    
    # 17. End the game if the bird flies too low (hitting the ground)
    # OR flies too high (above the screen)

        
        
    # *** ENHANCEMENTS ***
    # * Change the bird image to something else!
    # * Add a score that increments every time the bird gets through the pipes.
    # * Add a way to reset the game when it's over.
    # * Make the pipes move faster the longer the game goes.


# =================== DO NOT MODIFY THE CODE BELOW ======================

class Bird:
    def __init__(self, image_file, bird_x, bird_y):
        self.x = bird_x
        self.y = bird_y
        self.width = 50
        self.height = ( 3 * self.width ) / 4
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)

    def draw(self):
        image(self.image, self.x, self.y)


class Pipe:
    pipe_gap = 125
    
    def __init__(self, image_file, pipe_y=0, pipe_height=0):
        self.x = width
        self.y = pipe_y
        self.width = 50
        self.height = pipe_height
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
    
    def update(self):
        self.x -= 3
    
    def draw(self):
        image(self.image, self.x, self.y)

    def teleport(self, pipe_y, pipe_height):
        self.x = width
        self.y = pipe_y
        self.height = pipe_height
        self.image.resize(self.width, self.height)
        

def reset_pipes(lower_pipe, upper_pipe):
    random_height = int((2 * random(height) / 3) + 50)
    upper_pipe.teleport(0, random_height)
    lower_pipe.teleport(random_height + Pipe.pipe_gap, height - random_height)
    
    
def intersects_pipes(bird, lower_pipe, upper_pipe):
    # Check upper pipe collision
    if (bird.x + bird.width >= upper_pipe.x and
        bird.x <= upper_pipe.x + upper_pipe.width and
        bird.y + bird.height >= upper_pipe.y and
        bird.y <= upper_pipe.y + upper_pipe.height):
        return True

    # Check lower pipe collision
    if (bird.x + bird.width >= lower_pipe.x and
        bird.x <= lower_pipe.x + lower_pipe.width and
        bird.y + bird.height >= lower_pipe.y and
        bird.y <= lower_pipe.y + lower_pipe.height):
        return True

    return False

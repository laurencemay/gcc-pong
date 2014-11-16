import sys, pygame
pygame.init()
 
# Chain together some variables
# to store the screen size
size = width, height = 1024, 700
 
# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [2, -2]
left_hits = 0

# Create a Tuple to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
black = (0, 0, 0)
white = (255, 255, 255)
something = (125, 56, 100)
# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncy Face")
 
# Load the image we want to bounce
# and store it in a variable called 'sprite'
sprite = pygame.image.load("sprite.png")
left_paddle=pygame.image.load("paddle.png")
left_paddle_rect = left_paddle.get_rect()
left_paddle_rect.top = 250
# Get a bounding rectangle from the sprite
spriterect = sprite.get_rect()

font = pygame.font.Font(None, 36)

# Loop forever
while True:
    # Check the event list for a 'quit' event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
 
    # Move the bounding rectangle according to the
    # current velocity
    spriterect = spriterect.move(velocity)
    # Check of the bounding rectangle has touched the
    # edges of the window.
    if ((spriterect.left < left_paddle_rect.right) and (spriterect.bottom > left_paddle_rect.top) and (spriterect.top  < left_paddle_rect.bottom)):
           velocity[0] = -velocity[0]
    elif spriterect.left < 0:
           velocity[0] = -velocity[0]
           left_hits = left_hits + 1
    if spriterect.right > width:
        # Yes - touching sides of screen so reverse X
        # velocity value
        velocity[0] = -velocity[0]
    if spriterect.top < 0 or spriterect.bottom > height:
        # Yes - touching top/bottom of screen so
        # reverse the Y velocity value
        velocity[1] = -velocity[1]
 
    # Draw everything
    # First clear the screen
    screen.fill(white)
    # Blit the sprite to the current rectangle position
    screen.blit(sprite, spriterect)
    screen.blit(left_paddle, left_paddle_rect)
    text = font.render(str(left_hits), True,white,black)
    screen.blit(text, text.get_rect())
    # Flip the screen we've just drawn to the front
    pygame.display.flip()
# end of while loop - go round the loop again! 

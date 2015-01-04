import sys, pygame, time
pygame.init()
 
# Chain together some variables
# to store the screen size
size = width, height = 1024, 700
gamestatus = 0

 
# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [5, -10]
left_hits = 0
right_hits = 0
# Create a Tuple to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
black = (0, 0, 0)
white = (255, 255, 255)
something = (125, 56, 100)
# g
# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("georgia", 36)
pygame.display.set_caption("Pong game")

# Load the image we want to bounce
# and store it in a variable called 'sprite'
sprite = pygame.image.load("pongball.png")
screen0 = pygame.image.load("Amazing start screen.png")
screen0rect = screen0.get_rect()
left_paddle=pygame.image.load("paddle.png")
right_paddle = pygame.image.load("paddle.png")
left_paddle_rect = left_paddle.get_rect()
right_paddle_rect = right_paddle.get_rect()
left_paddle_rect.top = 250
right_paddle_rect.right = 1024
right_paddle_rect.top = 250

# Get a bounding rectangle from the sprite
spriterect = sprite.get_rect()

# Loop forever
while True:
        #do starting stuff                  
        # Check the event list for a 'quit' event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        
        # Check if we need to move the paddle
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            if right_paddle_rect.bottom < 700:
                right_paddle_rect.top= right_paddle_rect.top + 10
        if key[pygame.K_UP]:
            if right_paddle_rect.top > 0:
                       right_paddle_rect.bottom = right_paddle_rect.bottom - 10
        if key[pygame.K_s]:
            if left_paddle_rect.bottom < 700:
                left_paddle_rect.top= left_paddle_rect.top + 10
        if key[pygame.K_w]:
            if left_paddle_rect.top > 0:
                       left_paddle_rect.bottom = left_paddle_rect.bottom - 10
        if key[pygame.K_SPACE]:
            gamestatus = 1
              
        # Move the bounding rectangle according to the
        # current velocity
        spriterect = spriterect.move(velocity)
        # Check of the bounding rectangle has touched the
        # edges of the window.
        if ((spriterect.left < left_paddle_rect.right) and (spriterect.bottom > left_paddle_rect.top) and (spriterect.top  < left_paddle_rect.bottom)):
               velocity[0] = -velocity[0]
        elif spriterect.left < 0:
               velocity[0] = -velocity[0]
               right_hits = right_hits + 1
        if ((spriterect.right > right_paddle_rect.left ) and (spriterect.bottom > right_paddle_rect.top) and (spriterect.top < right_paddle_rect.bottom)):
            velocity[0] = -velocity[0]
        elif spriterect.right > 1024:
            velocity[0] = -velocity[0]
            left_hits = left_hits + 1
        if spriterect.top < 0 or spriterect.bottom > height:
            # Yes - touching top/bottom of screen so
            # reverse the Y velocity value
            velocity[1] = -velocity[1]
        if gamestatus == 0:
            screen.fill(white)
            screen.blit(screen0, screen0rect)
            pygame.display.flip()
#        if left_hits + 3 >= right_hits:
#            gamestatus = 2
#        if right_hits + 3 >= left_hits:
#            gamestatus = 2
       #if gamestatus == 1:           
            # Draw everything
                    # First clear the screen
        elif gamestatus == 1:
                
            
                screen.fill(white)
            # Blit the sprite to t current rectangle position
                text = font.render(str(left_hits), True,something,white)
                text2 = font.render(str(right_hits), True,something,white)
                textrect = text.get_rect()
                text2rect = text2.get_rect()
                text2rect.right = 1024
                screen.blit(text, textrect)
                screen.blit(text2, text2rect)
                screen.blit(sprite, spriterect)
                screen.blit(left_paddle, left_paddle_rect)
                screen.blit(right_paddle, right_paddle_rect)
       # Flip the screen we've just drawn to the front
                pygame.display.flip()
      # end of while loop - go round the loop again!
 #      elif gamestatus == 2:
                

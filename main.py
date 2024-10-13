import pygame
import random
from nlp import process_command

# Initialize the game 
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("NLP Game")

# Set up some character features
char_color = (0, 128, 255)
char_pos = [300, 200]
char_radius = 30
speed = 5

def draw_character():
    pygame.draw.circle(screen, char_color, char_pos, char_radius)

def move_character(action):
    global char_pos, char_color
    if action == "left":
        char_pos[0] -= speed
    elif action == "right":
        char_pos[0] += speed
    elif action == "jump":
        char_pos[1] -= speed * 2 
    elif action == "change color":
        char_color = [random.randint(0, 255) for _ in range(3)]    


# Main game loop
# if __name__ == "__main__":
running = True
while running:
    screen.fill((255, 255, 255))  # Background color in the game 
    draw_character()

    # Next up, we need to manage text commands.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_character("turn left")
                elif event.key == pygame.K_RIGHT:
                    move_character("turn right")
                elif event.key == pygame.K_UP:
                    move_character("jump")
                elif event.key == pygame.K_c:
                    move_character("change color")
    #command = input("Enter command: (left, right, jump, change) ")
    #action = process_command(command)
    #if action != "Unregistered command":
    #    move_character(action)
    #else:
    #    print("Unregistered command. You must try again :( ")

    #pygame.time.wait(1000) # Add some delay for input processing

    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        running = False

    pygame.display.update()
        

# Stop the game
pygame.quit()
print("Game Over")


import math
import pygame

# Constants
length_a = 300
initial_theta_a = math.pi /2 - 0.01
g = 980

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
trail_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
trail_surface.set_alpha(1000)  # Set transparency

# Define pendulum variables
pivot_x, pivot_y = 400, 200
pivot_xy = (pivot_x, pivot_y)
omega_a = (g / length_a) ** 0.5
start_time = pygame.time.get_ticks()

# Function to draw a pendulum
def draw_pendulum(pivot_xy, theta, length, color):
    pivot_x, pivot_y = pivot_xy
    opp = length * math.sin(theta)
    adj = length * math.cos(theta)
    bob_x = pivot_x + opp
    bob_y = pivot_y + adj
    bob_xy = (bob_x, bob_y)
    line_start = pivot_xy
    line_end = bob_xy
    pygame.draw.line(screen, color, line_start, line_end, 1)
    pygame.draw.circle(screen, (0,0,0),bob_xy , 21)

    pygame.draw.circle(screen, color, bob_xy, 20)  # bob
    return bob_xy

# Set up font for text
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
text1 = font1.render('Ten Pendulums', True, (255, 255, 255))
textRect1 = text1.get_rect()
textRect1.center = (400, 100)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time
    current_time = pygame.time.get_ticks()
    t = (current_time - start_time) / 1000

    # Calculate and draw each pendulum
    colors = [(255, 255, 255) for _ in range(10)]  # White color for all pendulums
    thetas = [(initial_theta_a * math.cos((omega_a + i * 0.05) * t)) for i in range(10)]
    
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(trail_surface, (0, 0))  # Draw the trail

    # Draw all pendulums
    for i in range(10):
        draw_pendulum(pivot_xy, thetas[i], length_a, colors[i])

    # Draw text
    screen.blit(text1, textRect1)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock = pygame.time.Clock()
    clock.tick(120)

pygame.quit()

import math
import pygame


length_a = int(input("Enter length 1 "))
length_b = int(input("Enter lentgh 2 "))
length_c = int(input("Enter lentgh 3"))

initial_theta_a = math.pi / 4
initial_theta_b = math.pi / 2
initial_theta_c = math.pi

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

centre = (400, 300)
running = True
g = 980
pivot_x = 400
pivot_y = 150
pivot_xy = (pivot_x, pivot_y)


start_time = pygame.time.get_ticks()
omega_a = (g / length_a) ** 0.5
omega_b = (g / length_b) ** 0.5
omega_c = (g / length_c) ** 0.5
bob3_history = []
text_fade = (255,255,255)

def draw_pendulum(pivot_xy, theta, length):
    blue = (98, 3, 252)
    red = (135, 5, 31)
    pivot_x, pivot_y = pivot_xy
    opp = length * math.sin(theta)
    adj = length * math.cos(theta)
    bob_x = pivot_x + opp
    bob_y = pivot_y + adj
    bob_xy = (bob_x, bob_y)
    line_start = pivot_xy
    line_end = bob_xy
    pygame.draw.line(screen, red, line_start, line_end, 2)
    pygame.draw.circle(screen, blue, bob_xy, 10)  # bob
    return bob_xy

trail_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
trail_surface.set_alpha(1000)  # Set transparency

font1 = pygame.font.SysFont('freesanbold.ttf', 50)

text1 = font1.render('Double Pendulum', True, (255,255,255))
textRect1 = text1.get_rect()
textRect1.center = (400, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    t = (current_time - start_time) / 1000

    theta_a = initial_theta_a * math.cos(omega_a * t)
    theta_b = initial_theta_b * math.cos(omega_b * t)
    theta_c = initial_theta_c * math.cos(omega_c * t)
    
    bob1_xy = draw_pendulum(pivot_xy, theta_a, length_a)
    bob2_xy = draw_pendulum(bob1_xy, theta_b, length_b)
    bob3_xy = draw_pendulum(bob2_xy,theta_c,length_c)
    
    bob3_history.append(bob3_xy)
    
    
    if len(bob3_history) >= 5000:
        bob3_history.pop(0)

    # Draw the trail
    for i in range(1, len(bob3_history)):
        start_pos = bob3_history[i-1]
        end_pos = bob3_history[i]
        alpha = int(255 * (i / len(bob3_history)))  # Gradual transparency
        color = (255,255,255, alpha)
        pygame.draw.line(trail_surface, color, start_pos, end_pos, 2)

    screen.fill((0, 0, 0))
    screen.blit(trail_surface, (0, 0))
    draw_pendulum(pivot_xy, theta_a, length_a)  # Draw pendulum on main screen
    draw_pendulum(bob1_xy, theta_b, length_b)
    draw_pendulum(bob2_xy,theta_c,length_c)
    screen.blit(text1, textRect1)
    font2 = pygame.font.SysFont('freesanbold.ttf', 30)
    text2 = font2.render('Length a: '+str(length_a), True, text_fade)
    text3 = font2.render('Length b: '+str(length_b), True, text_fade)
    text4 = font2.render('Theta a: '+str(round(initial_theta_a,2)), True, text_fade)
    text5 = font2.render('Theta b: '+str(round(initial_theta_b,2)), True,text_fade)
    text6 = font2.render('Length c: '+str(length_c), True, text_fade)
    text7 = font2.render('Theta c: '+str(round(initial_theta_c,2)), True,text_fade)

    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()

    textRect4 = text4.get_rect()
    textRect5 = text5.get_rect()

    textRect6 = text6.get_rect()
    textRect7 = text7.get_rect()

    textRect3.center = (650,500)
    textRect2.center = (650, 478)

    textRect4.center  = (650 , 566)
    textRect5.center = (650 , 544)
    
    textRect6.center  = (650 , 522)
    textRect7.center = (650 , 588)   
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4,textRect4)
    screen.blit(text5,textRect5)

    screen.blit(text6,textRect6)
    screen.blit(text7,textRect7)

    pygame.display.flip()
    if (int(t) % 2 == 0):
        if text_fade == (0,0,0):
            continue
        a,b,c = text_fade
  
        a -= 1
        b -= 1
        c -= 1
        text_fade = (a,b,c)
        
    trail_surface.fill((0, 0, 0, 0))  # Clear the trail surface

    clock = pygame.time.Clock()
    clock.tick(120)

    


pygame.quit()

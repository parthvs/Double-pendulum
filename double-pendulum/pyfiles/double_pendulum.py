import pygame
import math
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")

# Font for displaying text
font = pygame.font.Font(None, 24)

running = True
clock = pygame.time.Clock()

r1 , r2 = 170, 170
m1 , m2 = 15, 15
a1 = 0.0000
a2 = 0.0000
v1 = 0
v2 = 0
s1 = 1
s2 = 1
theta1, theta2 = 90,90
g = 9.8
dt = 0.05

theta1,theta2 = 0,0  # math.radians(theta1), math.radians(theta2)
pivot_x, pivot_y = 400,100
pivot_xy = (pivot_x, pivot_y)

trace = []


display_text = 1

# Function to draw the pendulum
def draw_pend(x1,y1,x2,y2):
    pygame.draw.line(screen,(0,0,0), pivot_xy, (x1,y1),2)
    pygame.draw.circle(screen,(0,0,0), (x1,y1), m1)
    pygame.draw.line(screen,(0,0,0),(x1,y1), (x2,y2),2)
    pygame.draw.circle(screen,(0,0,0),(x2,y2), m2)

# Function to draw the trace of pendulum
def draw_trace(ls):
    n = len(ls)
    color = (0,0,0)

    for i in range(1,n):
        ratio =  i/n
        temp = int(255 * ratio)
        temp = 255 - temp
        color = (temp,temp,temp)
        pygame.draw.aaline(screen,color,(ls[i-1][0],ls[i-1][1]),(ls[i][0],ls[i][1]),5)

# Function to display variable information
def display_info():
    info_text = [
        f"Radius 1 : {r1}",
        f"Radius 2 : {r2}",
        f"Mass 1 : {m1}",
        f"Mass 2 : {m2}",
        f"Velocity 1: {math.degrees(v1):.2f}m/s",
        f"Velocity 2: {math.degrees(v2):.2f}m/s"
    ]

    for i, text in enumerate(info_text):
        rendered_text = font.render(text, True, (0, 0, 0))
        screen.blit(rendered_text, (width - 200, height - 150 + i * 25))  # Bottom right

# Function to display key control instructions
def display_controls():
    control_text = [
        "Controls:",
        "Left/Right - Adjust V2",
        "A/D - Adjust V1",
        "H/J - Adjust Radius 1",
        "K/L - Adjust Radius 2",
        "M/N - Adjust Mass 1",
        "V/B - Adjust Mass 2",
        "T - Toggle screen text on or off",
        "R - Start at a random position",
        "Q - Quit"
    ]

    for i, text in enumerate(control_text):
        rendered_text = font.render(text, True, (0, 0, 0))
        screen.blit(rendered_text, (width - 250, 10 + i * 25))  # Top right

# Function to calculate angular accelerations and update velocities and angles
def calculate(theta1,theta2):
    global a1,a2,v1,v2
    a1 = ((-1 * g * ((2 * m1) + m2) * math.sin(theta1))- (m2 * g * math.sin(theta1 - (2* theta2))) - (2* math.sin(theta1 - theta2) * m2 * (((v2**2) * r2) + ((v1**2) * r1 * math.cos(theta1-theta2)))))/(r1 * (2 * m1) + m2 - (m2 * math.cos((2*theta1) - (2 * theta2))) )
    a2 = ((2 * math.sin(theta1 - theta2) * ((v1**2) * r1 * (m1 + m2) + ((g*(m1 + m2)) * math.cos(theta1)) + ((v2**2) * r2 * m2 * math.cos(theta1-theta2) ))))/(r2*((2 * m1) + m2 - (m2 * math.cos((2*theta1) - (2*theta2))) ))
    v1 += a1 * dt
    v2 += a2 * dt
    theta1 += v1 * dt
    theta2 += v2 * dt
    return(theta1,theta2)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                v1 += 0.05
            if event.key == pygame.K_RIGHT:
                v1 -= 0.05
                
            if event.key == pygame.K_a:
                v2 += 0.05
            if event.key == pygame.K_d:
                v2 -= 0.05
                
            if event.key == pygame.K_h:
                r1 += 1 
            if event.key == pygame.K_j:
                if r1 > 1 :
                    r1 -= 1   
                
            if event.key == pygame.K_k:
                r2 += 1 
            if event.key == pygame.K_l:
                if r2 > 1 :
                    r2 -= 1   
                
            if event.key == pygame.K_m:
                m1 += 1 
            if event.key == pygame.K_n:
                if m1 > 1:
                    m1 -= 1

            if event.key == pygame.K_v:
                m2 += 1 
            if event.key == pygame.K_b:
                if m2 > 1:
                    m2 -= 1
                
            if event.key == pygame.K_t:
                display_text *= -1
            if event.key == pygame.K_r:
                theta1,theta2 = random.uniform(-math.pi,math.pi),random.uniform(-math.pi,math.pi)
                trace = []
                v1,v2 = 0,0
                m1,m2 = 15,15
                r1,r2 = 170,170
            if event.key == pygame.K_q:
                running = False

    screen.fill((255,255,255))
    
    # Calculate positions of pendulum
    x1 = pivot_x + r1 * math.sin(theta1)
    y1 = pivot_y + r1 * math.cos(theta1)
    x2 = x1 + r2 * math.sin(theta2)
    y2 = y1 + r2 * math.cos(theta2)
    
    draw_pend(x1,y1,x2,y2)
    
    # Track trace of pendulum movement
    trace.append([x2,y2])
    if(len(trace) > 5000):
        trace.pop(0)
    draw_trace(trace)
    
    # Update angles using physics calculations
    theta1,theta2 = calculate(theta1,theta2)
    
    # Display variable info and controls
    if display_text == 1:
        display_info()
        display_controls()
    
    pygame.display.flip()
    clock.tick(120)

pygame.quit()

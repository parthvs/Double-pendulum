import pygame
import math
import random

error = random.uniform(0,0.001)

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triple Double Pendulum Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE , BLACK = BLACK , WHITE
L1, L2 = 145,150
m1, m2 = 10,10
g = 9.86
dt = 0.15
origin = (width // 2, (height // 4) -100)

bob1_history = []
bob2_history = []
bob2_history_new = []
bob2_history_third = []


twoseventydeg = 4.71239
fourfiftydeg = 7.85398
rad1 = random.uniform( twoseventydeg,fourfiftydeg)
rad2 = random.uniform(twoseventydeg,fourfiftydeg)

theta1, theta2 = rad1, rad2
omega1, omega2 = 0, 0

theta1_new, theta2_new = theta1, theta2 + error
omega1_new, omega2_new = 0, 0

theta1_third, theta2_third = theta1, theta2 - error
omega1_third, omega2_third = 0, 0

setls1x,setls1y,setls2x,setls2y,setls3x,setls3y = [],[],[],[],[],[]

def calculate_positions(theta1, theta2):
    x1 = L1 * math.sin(theta1)
    y1 = L1 * math.cos(theta1)
    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 + L2 * math.cos(theta2)
    return (x1, y1), (x2, y2)

def keeprange(angle):
  twopi = 2 * math.pi
  while abs(angle)>=twopi:
      if angle > 0:
        angle -= twopi
      else:
        angle += twopi
  return(angle)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # First pendulum
    num1 = -g * (2 * m1 + m2) * math.sin(theta1) - m2 * g * math.sin(theta1 - 2 * theta2)
    num2 = -2 * math.sin(theta1 - theta2) * m2 * (omega2**2 * L2 + omega1**2 * L1 * math.cos(theta1 - theta2))
    den = L1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))
    alpha1 = (num1 + num2) / den

    num1 = 2 * math.sin(theta1 - theta2)
    num2 = omega1**2 * L1 * (m1 + m2) + g * (m1 + m2) * math.cos(theta1) + omega2**2 * L2 * m2 * math.cos(theta1 - theta2)
    den = L2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))
    alpha2 = num1 * num2 / den

    omega1 += alpha1 * dt
    omega2 += alpha2 * dt
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    pos1, pos2 = calculate_positions(theta1, theta2)
    pos1 = (origin[0] + int(pos1[0]), origin[1] + int(pos1[1]))
    pos2 = (origin[0] + int(pos2[0]), origin[1] + int(pos2[1]))

    bob1_history.append(pos1)
    bob2_history.append(pos2)

    if len(bob2_history) > 1500:
        bob2_history.pop(0)

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, origin, pos1, 2)
    pygame.draw.line(screen, BLACK, pos1, pos2, 2)
    pygame.draw.circle(screen, BLACK, pos1, 10)
    pygame.draw.circle(screen, BLACK, pos2, 10)

    for i in range(1, len(bob2_history)):
        start_pos = bob2_history[i - 1]
        end_pos = bob2_history[i]
        alpha = int(255 * (i / len(bob2_history)))
        color = (255, 0, 0, alpha)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

    # Second pendulum
    num1_new = -g * (2 * m1 + m2) * math.sin(theta1_new) - m2 * g * math.sin(theta1_new - 2 * theta2_new)
    num2_new = -2 * math.sin(theta1_new - theta2_new) * m2 * (omega2_new**2 * L2 + omega1_new**2 * L1 * math.cos(theta1_new - theta2_new))
    den_new = L1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1_new - 2 * theta2_new))
    alpha1_new = (num1_new + num2_new) / den_new

    num1_new = 2 * math.sin(theta1_new - theta2_new)
    num2_new = omega1_new**2 * L1 * (m1 + m2) + g * (m1 + m2) * math.cos(theta1_new) + omega2_new**2 * L2 * m2 * math.cos(theta1_new - theta2_new)
    den_new = L2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1_new - 2 * theta2_new))
    alpha2_new = num1_new * num2_new / den_new

    omega1_new += alpha1_new * dt
    omega2_new += alpha2_new * dt
    theta1_new += omega1_new * dt
    theta2_new += omega2_new * dt

    pos1_new, pos2_new = calculate_positions(theta1_new, theta2_new)
    pos1_new = (origin[0] + int(pos1_new[0]), origin[1] + int(pos1_new[1]))
    pos2_new = (origin[0] + int(pos2_new[0]), origin[1] + int(pos2_new[1]))

    bob1_history.append(pos1_new)
    bob2_history_new.append(pos2_new)

    if len(bob2_history_new) > 1500:
        bob2_history_new.pop(0)

    pygame.draw.line(screen, BLACK, origin, pos1_new, 2)
    pygame.draw.line(screen, BLACK, pos1_new, pos2_new, 2)
    pygame.draw.circle(screen, BLACK, pos1_new, 10)
    pygame.draw.circle(screen, BLACK, pos2_new, 10)

    for i in range(1, len(bob2_history_new)):
        start_pos = bob2_history_new[i - 1]
        end_pos = bob2_history_new[i]
        alpha = int(255 * (i / len(bob2_history_new)))
        color = (0, 0, 255, alpha)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

    # Third pendulum
    num1_third = -g * (2 * m1 + m2) * math.sin(theta1_third) - m2 * g * math.sin(theta1_third - 2 * theta2_third)
    num2_third = -2 * math.sin(theta1_third - theta2_third) * m2 * (omega2_third**2 * L2 + omega1_third**2 * L1 * math.cos(theta1_third - theta2_third))
    den_third = L1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1_third - 2 * theta2_third))
    alpha1_third = (num1_third + num2_third) / den_third

    num1_third = 2 * math.sin(theta1_third - theta2_third)
    num2_third = omega1_third**2 * L1 * (m1 + m2) + g * (m1 + m2) * math.cos(theta1_third) + omega2_third**2 * L2 * m2 * math.cos(theta1_third - theta2_third)
    den_third = L2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1_third - 2 * theta2_third))
    alpha2_third = num1_third * num2_third / den_third

    omega1_third += alpha1_third * dt
    omega2_third += alpha2_third * dt
    theta1_third += omega1_third * dt
    theta2_third += omega2_third * dt

    pos1_third, pos2_third = calculate_positions(theta1_third, theta2_third)
    pos1_third = (origin[0] + int(pos1_third[0]), origin[1] + int(pos1_third[1]))
    pos2_third = (origin[0] + int(pos2_third[0]), origin[1] + int(pos2_third[1]))

    bob1_history.append(pos1_third)
    bob2_history_third.append(pos2_third)

    if len(bob2_history_third) > 1500:
        bob2_history_third.pop(0)

    pygame.draw.line(screen, BLACK, origin, pos1_third, 2)
    pygame.draw.line(screen, BLACK, pos1_third, pos2_third, 2)
    pygame.draw.circle(screen, BLACK, pos1_third, 10)
    pygame.draw.circle(screen, BLACK, pos2_third, 10)

    for i in range(1, len(bob2_history_third)):
        start_pos = bob2_history_third[i - 1]
        end_pos = bob2_history_third[i]
        alpha = int(255 * (i / len(bob2_history_third)))
        color = (0, 255, 0, alpha)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)
    set1x = theta1
    set1y = theta2
    set1x *= 30
    set1y *= 30
    setls1x.append(set1x  - 0)
    setls1y.append(set1y + 300)
    
    if len(setls1x) >2000:
      setls1x.pop(0)
      setls1y.pop(0)
    
    if len(setls1x) > 2:
      for i in range(1,len(setls1x)):
        pygame.draw.line(screen,(255,0,0),(setls1x[i-1],setls1y[i-1]),(setls1x[i],setls1y[i]),1)
    
    set2x = theta1_new
    set2y = theta2_new
    set2x *= 30
    set2y *= 30
    setls2x.append(set2x+ 220)
    setls2y.append(set2y + 300)
    
    if len(setls2x) >2000:
      setls2x.pop(0)
      setls2y.pop(0)
    
    if len(setls2x) > 2:
      for i in range(1,len(setls2x)):
        pygame.draw.line(screen,(0,0,255),(setls2x[i-1],setls2y[i-1]),(setls2x[i],setls2y[i]),1)
    
    set3x = theta1_third
    set3y = theta2_third
    set3x *= 30
    set3y *= 30
    setls3x.append(set3x+ 440)
    setls3y.append(set3y + 300)
    
    if len(setls3x) >2000:
      setls3x.pop(0)
      setls3y.pop(0)
    
    if len(setls3x) > 2:
      for i in range(1,len(setls3x)):
        pygame.draw.line(screen,(0,255,0),(setls3x[i-1],setls3y[i-1]),(setls3x[i],setls3y[i]),1)
    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

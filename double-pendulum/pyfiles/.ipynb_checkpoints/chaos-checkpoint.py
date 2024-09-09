import pygame
import math


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")


running = True
clock = pygame.time.Clock()


r1 , r2 = 200, 200
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

theta1,theta2 = math.radians(theta1), math.radians(theta2)
pivot_x, pivot_y = 400,100
pivot_xy = (pivot_x, pivot_y)

trace = []
def draw_pend(x1,y1,x2,y2):
    pygame.draw.line(screen,(0,0,0), pivot_xy, (x1,y1),2)
    pygame.draw.circle(screen,(0,0,0), (x1,y1), m1)
    pygame.draw.line(screen,(0,0,0),(x1,y1), (x2,y2),2)
    pygame.draw.circle(screen,(0,0,0),(x2,y2), m2)

def draw_trace(ls):
    n = len(ls)
    color = (0,0,0)

    for i in range(1,n):
        ratio =  i/n
        temp = int(255 * ratio)
        temp = 255 - temp
        color = (temp,temp,temp)
        pygame.draw.aaline(screen,color,(ls[i-1][0],ls[i-1][1]),(ls[i][0],ls[i][1]),5)
        
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
    screen.fill((255,255,255))
    x1 = pivot_x + r1 * math.sin(theta1)
    y1 = pivot_y + r1 * math.cos(theta1)
    x2 = x1 + r2 * math.sin(theta2)
    y2 = y1 + r2 * math.cos(theta2)
    
    draw_pend(x1,y1,x2,y2)
    trace.append([x2,y2])
    if(len(trace) > 5000):
        trace.pop(0)
    draw_trace(trace)

    theta1,theta2 = calculate(theta1,theta2)
    if(abs(theta2) >6):
        print(theta1,theta2)
    
    
    
    
    
   
    pygame.display.flip()

    

pygame.quit()
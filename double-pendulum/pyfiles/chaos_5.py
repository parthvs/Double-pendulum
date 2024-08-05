import pygame
import math


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")


running = True
clock = pygame.time.Clock()

theta1, theta2 = 90,90.0001
theta3, theta4 = 90,90.0002
theta5, theta6 = 90,90
theta7, theta8 = 90,89.9999
theta9, theta10= 90,89.9998
# pend1
r1, r2 = 200, 200
m1, m2 = 15, 15
a1 = 0.0
a2 = 0.0
v1 = 0
v2 = 0

# pend2
r3, r4 = 200, 200
m3, m4 = 15, 15
a3 = 0.0
a4 = 0.0
v3 = 0
v4 = 0

# pend3
r5, r6 = 200, 200
m5, m6 = 15, 15
a5 = 0.0
a6 = 0.0
v5 = 0
v6 = 0

# pend4
r7, r8 = 200, 200
m7, m8 = 15, 15
a7 = 0.0
a8 = 0.0
v7 = 0
v8 = 0

# pend5
r9, r10 = 200, 200
m9, m10 = 15, 15
a9 = 0.0
a10 = 0.0
v9 = 0
v10 = 0




theta1,theta2  = math.radians(theta1), math.radians(theta2)
theta3,theta4  = math.radians(theta3), math.radians(theta4)
theta5,theta6  = math.radians(theta5), math.radians(theta6)
theta7,theta8  = math.radians(theta7), math.radians(theta8)
theta9,theta10 = math.radians(theta9), math.radians(theta10)

trace1 =[]
trace2 =[]
trace3 =[]
trace4 =[]
trace5 =[]
trace1_color = (255,0,0)
trace2_color = (0,0,255)
trace3_color = (0,255,0)
trace4_color = (0,255,255)
trace5_color = (255,255,0)

pivot_x, pivot_y = 400,100
pivot_xy = (pivot_x, pivot_y)
g = 9.8
dt = 0.05

def draw_pend(theta1,theta2,r1,r2,trace,tc):
    x1 = pivot_x + r1 * math.sin(theta1)
    y1 = pivot_y + r1 * math.cos(theta1)
    x2 = x1 + r2 * math.sin(theta2)
    y2 = y1 + r2 * math.cos(theta2)
    trace.append([x2,y2])
    if(len(trace) > 1000):
        trace.pop(0)
    draw_trace(trace,tc)
    pygame.draw.line(screen,(0,0,0), pivot_xy, (x1,y1),2)
    pygame.draw.circle(screen,(0,0,0), (x1,y1), m1)
    pygame.draw.line(screen,(0,0,0),(x1,y1), (x2,y2),2)
    pygame.draw.circle(screen,(0,0,0),(x2,y2), m2)

def draw_trace(ls,tc):
    n = len(ls)
    a,b,c = tc
    for i in range(1,n):
        r = i / n  
        a_new = 255 - int(r * (255 - a))
        b_new = 255 - int(r * (255 - b))
        c_new = 255 - int(r * (255 - c))
        color = (a_new, b_new, c_new)
        pygame.draw.aaline(screen,color,(ls[i-1][0],ls[i-1][1]),(ls[i][0],ls[i][1]),5)
        
def calculate(theta1,theta2,a1,a2,v1,v2):
    a1 = ((-1 * g * ((2 * m1) + m2) * math.sin(theta1))- (m2 * g * math.sin(theta1 - (2* theta2))) - (2* math.sin(theta1 - theta2) * m2 * (((v2**2) * r2) + ((v1**2) * r1 * math.cos(theta1-theta2)))))/(r1 * (2 * m1) + m2 - (m2 * math.cos((2*theta1) - (2 * theta2))) )
    a2 = ((2 * math.sin(theta1 - theta2) * ((v1**2) * r1 * (m1 + m2) + ((g*(m1 + m2)) * math.cos(theta1)) + ((v2**2) * r2 * m2 * math.cos(theta1-theta2) ))))/(r2*((2 * m1) + m2 - (m2 * math.cos((2*theta1) - (2*theta2))) ))
    v1 += a1 * dt
    v2 += a2 * dt
    theta1 += v1 * dt
    theta2 += v2 * dt
    return(theta1,theta2,a1,a2,v1,v2)
    
while running:
    global a1,a2,v1,v2,trace1
    global a3,a4,v3,v4,trace2
    global a5,a6,v5,v6,trace3
    global a7,a8,v7,v8,trace4
    global a9,a10,v9,v10,trace5

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    
    
    draw_pend(theta1,theta2,r1,r2,trace1,trace1_color)
    theta1,theta2,a1,a2,v1,v2 = calculate(theta1,theta2,a1,a2,v1,v2)

    draw_pend(theta3, theta4, r3, r4, trace2, trace2_color)
    theta3, theta4, a3, a4, v3, v4 = calculate(theta3, theta4, a3, a4, v3, v4)
    
    draw_pend(theta5, theta6, r5, r6, trace3, trace3_color)
    theta5, theta6, a5, a6, v5, v6 = calculate(theta5, theta6, a5, a6, v5, v6)
    
    draw_pend(theta7, theta8, r7, r8, trace4, trace4_color)
    theta7, theta8, a7, a8, v7, v8 = calculate(theta7, theta8, a7, a8, v7, v8)
    
    draw_pend(theta9, theta10, r9, r10, trace5, trace5_color)
    theta9, theta10, a9, a10, v9, v10 = calculate(theta9, theta10, a9, a10, v9, v10)
    

    pygame.display.flip()

    

pygame.quit()
import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

L1, L2 = 120, 150
m1, m2 = 40, 40
g = 9.8
dt = 0.1
origin = (width // 2, height // 4)

bob1_history = []
bob2_history = []
bob2_history_new = []

theta1, theta2 = math.pi / 2, math.pi / 2
omega1, omega2 = 0, 0

theta1_new, theta2_new = math.pi / 2 , math.pi / 2 + 0.0000000000000000001
omega1_new, omega2_new = 0, 0

def calculate_positions(theta1, theta2):
    x1 = L1 * math.sin(theta1)
    y1 = L1 * math.cos(theta1)
    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 + L2 * math.cos(theta2)
    return (x1, y1), (x2, y2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        color = (133, 0, 4, alpha)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

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
        color = (49, 21, 209, alpha)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

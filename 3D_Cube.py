# TO DO ADD PAINTERS ALGORITHM

import pygame
import OpenGL.GL
from math import sin, cos

pygame.init()
WINDOW_SIZE = 800
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
size = 100
MAX_HIS = 30
font = pygame.font.SysFont("consolas", 24)
fps_history = []
hold_w = False
hold_d = False
hold_a = False
hold_s = False
angal_x = angal_y = angal_z = 0
clock = pygame.time.Clock()

cude_matrix = [[1,0,0],
               [0,1,0],
               [0,0,0]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]


def multi_m(a, b):
    result = [[0] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][0] += a[i][k] * b[k][j]
    return result

def connect_line(s, j, points):
    pygame.draw.line(window, (0, 0, 0), (points[s][0], points[s][1]), (points[j][0], points[j][1]),5)

def draw_faces(s, j, k, o, points):
    pygame.draw.polygon(window, (255, 0, 0), [(points[s][0], points[s][1]), (points[j][0], points[j][1]), (points[k][0], points[k][1]), (points[o][0], points[o][1])])

while True:
    clock.tick(60)
    window.fill((155,155,155))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hold_w = True
            if event.key == pygame.K_d:
                hold_a = True
            if event.key == pygame.K_a:
                hold_d = True
            if event.key == pygame.K_s:
                hold_s = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hold_w = False
            if event.key == pygame.K_d:
                hold_a = False
            if event.key == pygame.K_a:
                hold_d = False
            if event.key == pygame.K_s:
                hold_s = False
    
    
    if hold_w == True:
        angal_x += 0.1
    if hold_a == True:
        angal_y += 0.1
    if hold_d == True:
        angal_z += 0.1
    if hold_s == True:
        angal_x -= 0.1



    rotation_x = [[1, 0, 0],
                    [0, cos(angal_x), -sin(angal_x)],
                    [0, sin(angal_x), cos(angal_x)]]

    rotation_y = [[cos(angal_y), 0, sin(angal_y)],
                    [0, 1, 0,],
                    [-sin(angal_y), 0, cos(angal_y)]]
                
    rotation_z = [[cos(angal_z), -sin(angal_z), 0],
                    [sin(angal_z), cos(angal_z), 0],
                    [0, 0, 1]]

    angal_x += 0
    angal_y += 0
    angal_z += 0

    points = [0 for _ in range(len(cube_points))]
    s = 0
    for point in cube_points:
        rotate_x = multi_m(rotation_x, point)
        rotate_y = multi_m(rotation_y, rotate_x)
        rotate_z = multi_m(rotation_z, rotate_y)

        point_2d = multi_m(cude_matrix, rotate_z)

        x = point_2d[0][0] * size + WINDOW_SIZE/2
        y = point_2d[1][0] * size + WINDOW_SIZE/2

        points[s] = (x,y)
        s +=1 
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

    current_fps =  clock.get_fps()
    fps_history.append(current_fps)
    if len(fps_history) > MAX_HIS:
        fps_history.pop(0)
        avg_fps = sum(fps_history) / len(fps_history)
        fps_text = font.render(f"{avg_fps:.1f}", True, (255, 255, 0))
        window.blit(fps_text, (10, 10))


    draw_faces(1, 2, 6, 5, points)
    draw_faces(0, 3, 7, 4, points)
    draw_faces(2, 3, 7, 6, points)
    draw_faces(0, 1, 5, 4, points)
    draw_faces(4, 5, 7, 6, points)
    draw_faces(0, 1, 2, 3, points)
    connect_line(0, 1, points)
    connect_line(0, 3, points)
    connect_line(0, 4, points)
    connect_line(1, 2, points)
    connect_line(1, 5, points)
    connect_line(2, 6, points)
    connect_line(2, 3, points)
    connect_line(3, 7, points)
    connect_line(4, 5, points)
    connect_line(4, 7, points)
    connect_line(6, 5, points)
    connect_line(6, 7, points)
    
    pygame.display.update()

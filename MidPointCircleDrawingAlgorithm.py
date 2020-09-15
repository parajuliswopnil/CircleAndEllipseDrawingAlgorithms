import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

pygame.init()
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)

originalCoordinateList = []
coordinateList = []

radius = int(input("Enter the radius of the circle"))
x = int(input("Enter the x coordinate of the centre"))
y = int(input("Enter the y coordinate of the centre"))
originalCoordinateList.append((0, radius))
coordinateList.append((0 + x, radius + y))
x1 = 0
y1 = radius

p = 5/4 - radius
while x1 <= y1:
    if p <= 0:
        x1 = x1 + 1
        y1 = y1
        p = p + 2 * x1 +1
        print(p)
        originalCoordinateList.append((x1, y1))
        coordinateList.append((x1 + x, y1 + y))

    elif p > 0:
        x1 = x1 + 1
        y1 = y1 - 1
        p = p + 2 * x1 + - 2 * y1
        originalCoordinateList.append((x1, y1))
        coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1, 0, -1):
    (x1, y1) = originalCoordinateList[i]
    temp = x1
    x1 = y1
    y1 = temp
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1):
    (x1, y1) = originalCoordinateList[i]
    temp = x1
    x1 = y1
    y1 = -temp
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1, 0, -1):
    (x1, y1) = originalCoordinateList[i]
    x1 = x1
    y1 = -y1
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1):
    (x1, y1) = originalCoordinateList[i]
    x1 = -x1
    y1 = -y1
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1, 0, -1):
    (x1, y1) = originalCoordinateList[i]
    temp = x1
    x1 = -y1
    y1 = -temp
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1):
    (x1, y1) = originalCoordinateList[i]
    temp = x1
    x1 = -y1
    y1 = temp
    coordinateList.append((x1 + x, y1 + y))

for i in range(len(originalCoordinateList) - 1, 0, -1):
    (x1, y1) = originalCoordinateList[i]
    x1 = -x1
    y1 = y1
    coordinateList.append((x1 + x, y1 + y))




print(coordinateList)

drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

for i in range(len(coordinateList) - 1):
        pygame.draw.line(drawingSurface, colorBlack, coordinateList[i], coordinateList[i+1], 2)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()







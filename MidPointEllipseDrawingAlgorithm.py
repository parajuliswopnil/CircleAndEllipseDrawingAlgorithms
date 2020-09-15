import math
import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

pygame.init()
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)

originalCoordinateList = []
coordinateList = []

xRadius = int(input("Enter the x radius of the ellipse: "))
yRadius = int(input("Enter the y radius of the ellipse: "))
x = int(input("Enter the x coordinate of centre: "))
y = int(input("Enter the y coordinate of centre: "))
originalCoordinateList.append((0, yRadius))
coordinateList.append((0 + x, yRadius + y))

x1 = 0
y1 = yRadius

p = pow(yRadius, 2) - pow(xRadius, 2) * yRadius + 0.25 * pow(xRadius, 2)

while 2 * pow(yRadius, 2) * x1 <= 2 * pow(xRadius, 2) * y1:
    if p <= 0:
        x1 = x1 + 1
        y1 = y1
        p = p + 2 * pow(yRadius, 2) * x1 + pow(yRadius, 2)
        originalCoordinateList.append((x1, y1))
        coordinateList.append((x1 + x, y1 + y))
    elif p > 0:
        x1 = x1 + 1
        y1 = y1 - 1
        p = p + 2 * pow(yRadius, 2) * x1 - 2 * pow(xRadius, 2) * y1 + pow(yRadius, 2)
        originalCoordinateList.append((x1, y1))
        coordinateList.append((x1 + x, y1 + y))

(x2, y2) = originalCoordinateList[len(originalCoordinateList)-1]
p = pow(yRadius, 2) * pow(x2 + 0.5, 2) + pow(xRadius, 2) * pow(y2 - 1, 2) - pow(xRadius, 2) * pow(yRadius, 2)
while y2 > 0:
    if p <= 0:
        x2 = x2 + 1
        y2 = y2 - 1
        p = p + 2 * pow(yRadius, 2) * x2 - 2 * pow(xRadius, 2) * y2 + pow(xRadius, 2)
        originalCoordinateList.append((x2, y2))
        coordinateList.append((x2 + x, y2 + y))
    elif p > 0:
        x2 = x2
        y2 = y2 - 1
        p = p - 2 * pow(xRadius, 2) * y2 + pow(xRadius, 2)
        originalCoordinateList.append((x2, y2))
        coordinateList.append((x2 + x, y2 + y))

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
    x1 = -x1
    y1 = y1
    coordinateList.append((x1 + x, y1 + y))






print(coordinateList)

drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

for i in range(len(coordinateList) - 1):
        pygame.draw.line(drawingSurface, colorBlack, coordinateList[i], coordinateList[i+1], 2)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

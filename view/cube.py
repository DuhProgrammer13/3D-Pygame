__author__ = 'Kody'

import pygame, sys
from pygame.surface import Surface
from pygame.draw import *

class Cube(Surface):
    def __init__(self, size, images):
        Surface.__init__(self, images.get_size(), pygame.SRCALPHA)

        self.location = (0, 35)
        self.blit(images, (0, 0))
        self.xChange = 100

        self.surfaces = [pygame.Surface(images.get_size(), pygame.SRCALPHA) for x in range(6)]
        self.surfaces[0].blit(images, (0, 0))
        self.surfaces[1].blit(images, (0, 0))

        self.ORIGINAL_SURFACES = [pygame.Surface((100, 100), pygame.SRCALPHA) for x in range(6)]
        self.ORIGINAL_SURFACES[0].blit(images, (0, 0))

        self.testingSurf = self.skewSurface(pygame.transform.scale(self.surfaces[0], (self.xChange, 100)), 0, 33)
        print self.testingSurf.get_size()
    def draw(self, drawToSurface):
        line(drawToSurface, (255, 0, 0), (0, 60), (100, 60))
        drawToSurface.blit(pygame.transform.scale(pygame.transform.rotate(self.surfaces[0], 45), (200, 71)), (0, 0))
        drawToSurface.blit(self.testingSurf, self.location)
        drawToSurface.blit(pygame.transform.flip(self.testingSurf, True, False), (self.xChange- 1, 35))
        #self.xChange -= 2
        if self.xChange == 0:
            self.xChange = 100

    def skewSurface(self, surface, scewX, scewY):
        surfSizeX, surfSizeY = surface.get_size()
        returnSurf = pygame.Surface((surfSizeX + abs(scewX), surfSizeY + abs(scewY)), pygame.SRCALPHA)

        if (scewX > 0):
            lastX = 0

            slope = (scewX * 1.0) / (surfSizeY * 1.0)

            surfAreaToGet = pygame.Rect(0, 0, surfSizeX, 1)

            for y in range(surfSizeY + 1):
                if (int(y * slope) > lastX) or y == surfSizeY:
                    lastX = int(y * slope)
                    returnSurf.blit(surface, (lastX, surfAreaToGet.y), surfAreaToGet)
                    surfAreaToGet.y = y
                    surfAreaToGet.height = 0
                surfAreaToGet.height += 1
        elif scewX < 0:
            lastX = 0

            slope = (scewX * 1.0) / (surfSizeY * 1.0)

            surfAreaToGet = pygame.Rect(0, 0, surfSizeX, 1)

            for y in range(surfSizeY + 1, 0, -1):
                print y
                if (int(y * slope) > lastX) or y == 1:
                    lastX = int(y * slope)
                    returnSurf.blit(surface, (lastX, surfAreaToGet.y), surfAreaToGet)
                    surfAreaToGet.y = y
                    surfAreaToGet.height = 0
                surfAreaToGet.height += 1
        else:
            returnSurf = surface

        if (scewY > 0):
            surfSizeX, surfSizeY = surface.get_size()
            lastY = 0
            slope = (scewY * 1.0) / (surfSizeX * 1.0)

            surfAreaToGet = pygame.Rect(0, 0, 1, surfSizeY)
            surface = returnSurf

            returnSurf = pygame.Surface((surfSizeX + abs(scewX), surfSizeY + abs(scewY) + scewX/2), pygame.SRCALPHA)

            for x in range(returnSurf.get_size()[0] + 1):
                if (int(x * slope) > lastY) or x == surfSizeX:
                    lastY = int(x * slope)

                    returnSurf.blit(surface, (surfAreaToGet.x, lastY), surfAreaToGet)
                    surfAreaToGet.x = x
                    surfAreaToGet.width = 0
                    print ("top: %s\nbottom: %s" % (lastY, lastY + surfAreaToGet.bottom))
                else:
                    #print "x * slope = %s" % (x * slope)
                    b = 1
                surfAreaToGet.width += 1
        elif (scewY < 0):
            surfSizeX, surfSizeY = surface.get_size()
            lastY = scewY
            print "lastY : " + str(lastY)
            slope = (scewY * 1.0) / (surfSizeX * 1.0)
            print "slope: " + str(slope)

            surfAreaToGet = pygame.Rect(0, 0, 0, surfSizeY)
            surface = returnSurf

            returnSurf = pygame.Surface((surfSizeX + abs(scewX), surfSizeY + abs(scewY) + scewX / 2), pygame.SRCALPHA)

            print "surfSizeY : %s\n surfSizeY + abs(scewY) : %s blurb" % (surfSizeY, (surfSizeY + abs(scewY)))

            for x in range(returnSurf.get_size()[0], -1, -1):
                if (int(x * slope) > lastY) or x == 0:
                    lastY = int(x * slope)

                    returnSurf.blit(surface, (surfAreaToGet.x, lastY - scewY/2), surfAreaToGet)
                    surfAreaToGet.x = x
                    surfAreaToGet.width = 0
                    print ("top: %s\nbottom: %s" % (lastY, lastY + surfAreaToGet.bottom))
                else:
                    print "x * slope = %s" % (x * slope)
                    b = 1
                surfAreaToGet.width += 1


        print(returnSurf.get_size()[1])
        return returnSurf
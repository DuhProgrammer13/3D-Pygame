__author__ = 'Kody'

import pygame
import Transform
from pygame.surface import Surface
from pygame.draw import *


class Cube(Surface):
    def __init__(self, size, images):
        Surface.__init__(self, images[0].get_size(), pygame.SRCALPHA)

        self.location = (0, 34)
        self.blit(images[0], (0, 0))
        self.xChange = 100

        self.rotationX = 45
        self.rotationY = 33

        self.surfaces = [CubeSide(images[x], images[0].get_size(), x) for x in range(6)]
        self.surfaces[0].blit(images[0], (0, 0))
        self.surfaces[1].blit(images[1], (0, 0))

        self.ORIGINAL_SURFACES = [pygame.Surface((100, 100), pygame.SRCALPHA) for _ in range(6)]
        self.ORIGINAL_SURFACES[0].blit(images[0], (0, 0))

        self.testingSurf = Transform.skew_surface(pygame.transform.scale(self.surfaces[0], (self.xChange, 100)), 0, 33)
        self.testingSurf2 = Transform.skew_surface(pygame.transform.scale(self.surfaces[4], (self.xChange, 100)), 0, -33)

    def draw(self, draw_to_surface):
        for surf in self.surfaces:
            surf.update(self.rotationX, self.rotationY)
            if (surf.isVisible and surf.side != 2):
                surf.redraw(self.rotationX, self.rotationY)
        line(draw_to_surface, (255, 0, 0), (0, 60), (100, 60))
        draw_to_surface.blit(pygame.transform.scale(pygame.transform.rotate(self.surfaces[2], -self.rotationX % 180), (200, 68)), (0, 0))
        for surf in self.surfaces:
            if surf.isVisible and surf.side:
                draw_to_surface.blit(surf, (self.location[0] + 100 - self.rotationX%90, self.location[1]))
        #draw_to_surface.blit(self.testingSurf, (-100 + self.xChange, 34))
        #draw_to_surface.blit(self.testingSurf2, (self.xChange, 34))
        self.rotationX += 2


class CubeSide(Surface):
    def __init__(self, surface_image, front_size, side):
        Surface.__init__(self, front_size, pygame.SRCALPHA)
        self.originalImage = surface_image
        self.blit(surface_image, (0, 0))
        self.side = side
        self.isVisible = True

        self.originalRotationX = 0
        self.originalRotationY = 0

        self.get_rotation()

    def update(self, rotation_x, rotation_y):
        if ((90 <= rotation_x + self.originalRotationX <= 270)
            or (90 <= rotation_y + self.originalRotationY <= 270)):
            self.isVisible = False
        else:
            self.isVisible = True

        if Debug.debug:
            print "Side %s\nrotation_x + self.originalRotationX = %s\nrotation_y + self.originalRotationY = %s" % (
                self.side, rotation_x + self.originalRotationX, rotation_y + self.originalRotationY)

            print ("Side %s %s visible" % (self.side + 1, ("is" if self.isVisible else "is not")))
            print "-" * 10

    def get_rotation(self):
        if self.side == 0:
            self.originalRotationX = 0
        elif self.side == 1:
            self.originalRotationX = 90
        elif self.side == 2:
            self.originalRotationY = 270
        elif self.side == 3:
            self.originalRotationY = 90
        elif self.side == 4:
            self.originalRotationX = 270
        elif self.side == 5:
            self.originalRotationX = 180
            self.originalRotationY = 180

    def redraw(self, rotation_x, rotation_y):
        resize_width = 0
        resize_height = 0
        if (rotation_x + self.originalRotationX > 360):
            resize_width = (rotation_x + self.originalRotationX * 1.0) % 90.0
            resize_width = int(resize_width * 100)

        Surface.__init__(self, self.get_size(), pygame.SRCALPHA)
        Transform.skew_surface(self.originalImage, 0, -rotation_y), (0, 0)
        self.blit(pygame.transform.scale(Transform.skew_surface(self.originalImage, 0, -rotation_y), (resize_width, self.get_size()[1])), (-rotation_x,0))


class Test(Surface):
    def __init__(self, image):
        Surface.__init__(self, (300, 300))

        self.rotation = 0
        self.originalImage = image

        self.cubeSide = CubeSide(image, (100, 100), 0)

        self.imageLocation = (100, 100)

    def draw(self, surface):
        self.fill((0,0,0))
        self.cubeSide.update(self.rotation, 0)
        self.cubeSide.redraw(self.rotation, 0)
        print ("Equation = %s" % (-33 + int(((self.rotation * 1.0) % 90)/ 90.0 * 66)))
        if self.rotation <= 90:
            self.blit(pygame.transform.scale(Transform.skew_surface(self.originalImage, 0, -33 + int(((self.rotation * 1.0) % 90)) ), (int((self.rotation%90.0)/90*100), 100)), self.imageLocation)
        else:
            self.blit(pygame.transform.scale(Transform.skew_surface(self.originalImage, 0, -33 + int(((self.rotation * 1.0) % 90))),
                                             (100 - int((self.rotation % 90.0) / 90 * 100), 100)), self.imageLocation)

        if (self.rotation == 90):
            self.rotation = 0
        self.rotation += 1

        self.imageLocation = (100 - int((self.rotation % 90.0) / 90 * 100), self.imageLocation[1])

        surface.blit(self, (200, 200))
class Debug:
    debug = False
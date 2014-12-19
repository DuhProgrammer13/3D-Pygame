__author__ = 'Kody'
import  pygame

def skew_surface(surface, scew_x, scew_y, anti_alias=False):
    surf_size_x, surf_size_y = surface.get_size()
    return_surf = pygame.Surface((surf_size_x + abs(scew_x), surf_size_y + abs(scew_y)), pygame.SRCALPHA)

    flip_x, flip_y = False, False

    if scew_y < 0:
        flip_x = True

    if scew_x < 0:
        flip_y = True

    scew_x = abs(scew_x)
    scew_y = abs(scew_y)

    if scew_x != 0:
        last_x = 0

        slope = (scew_x * 1.0) / (surf_size_y * 1.0)

        surf_area_to_get = pygame.Rect(0, 0, surf_size_x, 1)

        for y in range(surf_size_y + 1):
            if (int(y * slope) > last_x) or y == surf_size_y:
                last_x = int(y * slope)
                return_surf.blit(surface, (last_x, surf_area_to_get.y), surf_area_to_get)
                surf_area_to_get.y = y
                surf_area_to_get.height = 0
            surf_area_to_get.height += 1
    else:
        return_surf = surface

    # #######################################
    # ## - SCEW VERTICALLY USING SCEW_Y - ###
    # #######################################

    if scew_y != 0:
        surf_size_x, surf_size_y = surface.get_size()
        last_y = 0
        slope = (scew_y * 1.0) / (surf_size_x * 1.0)

        surf_area_to_get = pygame.Rect(0, 0, 1, surf_size_y)
        surface = return_surf

        return_surf = pygame.Surface((surf_size_x + abs(scew_x), surf_size_y + abs(scew_y) + scew_x / 2), pygame.SRCALPHA)

        for x in range(return_surf.get_size()[0] + 1):
            if (int(x * slope) > last_y) or x == surf_size_x:
                last_y = int(x * slope)

                return_surf.blit(surface, (surf_area_to_get.x, last_y), surf_area_to_get)
                surf_area_to_get.x = x
                surf_area_to_get.width = 0

            surf_area_to_get.width += 1

    return_surf = pygame.transform.flip(return_surf, flip_x, flip_y)

    return return_surf
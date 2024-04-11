from framework.utils.imports import *


def fade_out(delay, surface, display_surface, screen, render) -> None:
    for alpha in range(0, 255):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        surface.set_alpha(alpha)
        render()
        display_surface.blit(surface, (0, 0))
        screen.blit(pygame.transform.scale(display_surface, screen.get_size()), (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)
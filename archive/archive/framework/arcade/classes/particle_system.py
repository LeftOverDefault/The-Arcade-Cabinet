from framework.arcade.utils.imports import *


class ParticleSystem(pygame.sprite.Group):
    def __init__(self, display_surface, config) -> None:
        super().__init__()
        self.config = config
        self.display_surface: pygame.Surface = display_surface

        self.max_particles = 0


    def draw(self) -> None:
        for particle in self:
            # alive = random.randint(0, 20)
            # if alive == 1:
                # particle.alive = False
            # if particle.alive == True:
                if len(self) > self.max_particles:
                    self.remove(particle)
                    particle.alive = False
                else:
                    self.display_surface.blit(particle.image, particle.rect)
            # else:
                # self.remove(particle)


    def update(self, delta_time) -> None:
        for particle in self:
            particle.update(delta_time)
from world_engine.classes.camera import Camera
from world_engine.utils.imports import *

from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos


class WorldEngine:
    """
    An Engine for generating worlds stored as JSON files to be read by the `arcade` module.
    """
    def __init__(self) -> None:
        self.version = "0.1.0"
        pygame.init()
        pygame.display.set_caption(f"World Engine v{self.version}")
        self.on_init()

    
    def on_init(self):
        self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
        self.display_surface = pygame.Surface((198 * 2, 108 * 2))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.running = True
        self.fullscreen = False

        self.camera = Camera(self.display_surface)

        mouse_image = pygame.image.load("./assets/sprite/mouse.png").convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), mouse_image)
        pygame.mouse.set_cursor(cursor)

        self.origin = pygame.Vector2()
        self.pan_active = False
        self.pan_offset = pygame.Vector2()

        # support lines 
        self.support_line_surf = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.support_line_surf.set_colorkey('green')
        self.support_line_surf.set_alpha(30)
    

    def get_current_cell(self):
        distance_to_origin = pygame.Vector2(mouse_pos()) - self.origin
        col = int(distance_to_origin.x / 64)
        row = int(distance_to_origin.y / 64)
        
        return col, row


    def render(self) -> None:
        self.camera.draw()


    def update(self) -> None:
        self.camera.update(self.delta_time)
    

    def draw_lines(self):
        cols = self.screen.get_width() // 64
        rows = self.screen.get_height() // 64

        origin_offset = pygame.Vector2(
            x = self.origin.x - int(self.origin.x / 64) * 64,
            y = self.origin.y - int(self.origin.y / 64) * 64
        )

        self.support_line_surf.fill('green')

        for col in range(cols + 1):
            x = origin_offset.x + col * 64
            pygame.draw.line(self.support_line_surf, "black", (x, 0), (x, self.screen.get_height()))

        for row in range(rows + 1):
            y = origin_offset.y + row * 64
            pygame.draw.line(self.support_line_surf, "black", (0, y), (self.screen.get_width(), y))

        self.display_surface.blit(self.support_line_surf,(0,0))


    def events(self, event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                self.fullscreen = not self.fullscreen
                if self.fullscreen == True:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        # middle mouse button pressed / released 
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_active = True
            self.pan_offset = pygame.Vector2(mouse_pos()) - self.origin

        if not mouse_buttons()[1]:
            self.pan_active = False

        # mouse wheel 
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50


        # panning update
        if self.pan_active:
            self.origin = pygame.Vector2(mouse_pos()) - self.pan_offset


    def canvas_add(self):
        if mouse_buttons()[0]:
            self.get_current_cell()


    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                self.events(event)
                self.canvas_add()
            
            self.delta_time = self.clock.tick(self.fps) / 1000

            self.display_surface.fill((255, 255, 255))

            self.render()
            self.update()

            self.draw_lines()
            pygame.draw.circle(self.display_surface, "red", self.origin, 4)
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()
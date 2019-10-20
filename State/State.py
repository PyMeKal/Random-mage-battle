import pygame
from Root import Root

class State:
    class Slot:
        def __init__(self, x, y):
            self.x, self.y = x, y

    class Pointer:
        def __init__(self, x, y):
            self.x, self.y = x - 15, y + 5

        def draw(self):
            pygame.draw.polygon(Root.win, Root.text_color,
                                ((self.x, self.y), (self.x + 8, self.y + 8), (self.x, self.y + 16)))

    class Input:
        def __init__(self, x, y, name, func):
            self.x, self.y = x, y
            self.name = Root.typing(name)
            self.func = func

    def __init__(self):
        self.slot = []
        self.menu = []
        self.place = 0

    def show_menu(self):
        pass

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Root.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.menu[self.place].func()
                elif event.key == pygame.K_UP:
                    self.place -= 1
                    self.pointer_limit()
                elif event.key == pygame.K_DOWN:
                    self.place += 1
                    self.pointer_limit()

    def pointer_limit(self):
        if self.place < 0:
            self.place = 0
        elif self.place >= len(self.menu):
            self.place = len(self.menu) - 1
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)

    def tick(self):
        self.control()
        self.show_menu()



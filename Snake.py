import pygame.event

from Cube import Cube


class Snake:
    def __init__(self, color, position):
        self.body = []
        self.turns = {}
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction_x = 0
        self.direction_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.direction_x = -1
                self.direction_y = 0
                self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
            elif keys[pygame.K_RIGHT]:
                self.direction_x = 1
                self.direction_y = 0
                self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
            elif keys[pygame.K_UP]:
                self.direction_x = 0
                self.direction_y = -1
                self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
            elif keys[pygame.K_DOWN]:
                self.direction_x = 0
                self.direction_y = 1
                self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.direction_x == -1 and c.position[0] <= 0:
                    c.position = (c.rows - 1, c.position[1])
                if c.direction_x == 1 and c.position[0] == c.rows - 1:
                    c.position = (0, c.position[1])
                if c.direction_y == 1 and c.position[1] == c.rows - 1:
                    c.position = (c.position[0], 0)
                if c.direction_y == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows - 1)
                else:
                    c.move(c.direction_x, c.direction_y)

    def reset(self, position):
        self.head = Cube(position)
        self.body = [self.head]
        self.turns = {}
        self.direction_x = 0
        self.direction_y = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.position[0], tail.position[1] + 1)))

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface, i == 0)

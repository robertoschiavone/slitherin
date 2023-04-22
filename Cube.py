import pygame.draw


class Cube:
    rows = 20
    w = 500

    def __init__(self, start, direction_x=1, direction_y=0, color=(255, 0, 0)):
        self.position = start
        self.direction_x = 1
        self.direction_y = 0
        self.color = color

    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.position = (self.position[0] + self.direction_x,
                         self.position[1] + self.direction_y)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1,
                                               dis - 2, dis - 2))

        if eyes:
            center = dis // 2
            radius = 3
            circle_middle = (i * dis + center - radius, j * dis + 8)
            circle_middle_2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle_2, radius)

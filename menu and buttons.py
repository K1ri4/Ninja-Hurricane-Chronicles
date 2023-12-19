import pygame
pygame.init()
font_type = pygame.font.SysFont('arial', 36)


class Button:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                if click[0] == 1:
                    if action is not None:
                        action()
        text = font_type.render(message, True, (0, 0, 0))
        screen.blit(text, (x + 5, y + 5))


def main(screen):
    screen.fill((60, 240, 231))

    game_button = Button(125, 50, (2, 217, 16))
    game_button.draw(188, 100, 'Играть')

    stat_button = Button(201, 50, (2, 217, 16))
    stat_button.draw(150, 200, 'Статистика')

    exit_button = Button(125, 50, (2, 217, 16))
    exit_button.draw(188, 300, 'Выход', exit)


pygame.display.set_caption('Менюшки')
size = width, height = 501, 501
screen = pygame.display.set_mode(size)


running = True
main_menu = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if main_menu:
        main(screen)
    pygame.display.flip()

import pygame
import os
import sys


class Cursor(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.cursor = load_image('arrow.png')

        self.image = self.cursor
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args) -> None:
        if args:
            event = args[0]
            if event.type == pygame.MOUSEMOTION:
                self.rect.x = event.pos[0]
                self.rect.y = event.pos[1]


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def main():
    pygame.init()
    size = 500, 500

    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    running = True

    group_cursor = pygame.sprite.Group()
    Cursor(group_cursor)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                group_cursor.update(event)
        screen.fill('black')

        group_cursor.update()
        if pygame.mouse.get_focused():
            group_cursor.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

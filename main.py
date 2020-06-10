import pygame
from apple import Apple
from random import randrange, choice
from segment import Segment


def relocate_apple(parts):
    possible_coords = []
    for x in range(0, 700, 20):
        for y in range(0, 500, 20):
            if [x, y] not in parts:
                possible_coords.append([x, y])
    return choice(possible_coords)


score = 4
size = width, height = 700, 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
parts_list = []
x_change = 0
y_change = 0

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
all_sprites_list = pygame.sprite.Group()

apple = Apple(RED, 20, 20)
apple.rect.x = randrange(20, width - 20, 20)
apple.rect.y = randrange(20, height - 20, 20)
all_sprites_list.add(apple)

x = width / 2 + 10
y = height / 2 + 10
for i in range(4):
    segment = Segment(GREEN, 20, 20, x, y)
    parts_list.append(segment)
    all_sprites_list.add(segment)
x_change = 20
y_change = 0

running = True

clock = pygame.time.Clock()
run = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_change != 20:
        x_change = 0
        y_change = -20
    if keys[pygame.K_DOWN] and y_change != -20:
        x_change = 0
        y_change = 20
    if keys[pygame.K_RIGHT] and x_change != -20:
        x_change = 20
        y_change = 0
    if keys[pygame.K_LEFT] and x_change != 20:
        x_change = -20
        y_change = 0

    old_segment = parts_list.pop()
    all_sprites_list.remove(old_segment)

    x = parts_list[0].rect.x + x_change
    y = parts_list[0].rect.y + y_change
    segment = Segment(GREEN, 20, 20, x, y)

    parts_list.insert(0, segment)
    all_sprites_list.add(segment)

    if parts_list[0].rect.y < 0:
        running = False
    if parts_list[0].rect.y > height:
        running = False
    if parts_list[0].rect.x < 0:
        running = False
    if parts_list[0].rect.x > width:
        running = False

    for i in range(1, len(parts_list)):
        if parts_list[0].rect == parts_list[i].rect:
            running = False

    if pygame.sprite.collide_mask(segment, apple):
        new_coords = relocate_apple(parts_list)
        apple.rect.x = new_coords[0]
        apple.rect.y = new_coords[1]
        parts_list.append(Segment(GREEN, 20, 20, parts_list[len(parts_list) - 1].rect.x + x_change,
                                  parts_list[len(parts_list) - 1].rect.y + y_change))
        score += 1

    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 20)
    text = font.render('Score: ' + str(score), 1, GREEN)
    screen.blit(text, (width - 75, 10))

    pygame.display.flip()

    clock.tick(15)
    run += 1

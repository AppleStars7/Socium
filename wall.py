import pygame
import gfx
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        wall_size = gfx.wall.get_rect().size
        self.width = wall_size[0]
        self.height = wall_size[1]
    # 벽그리기용함수
    def draw(self):
        screen.blit(gfx.wall, (self.x, self.y))
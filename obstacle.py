import pygame
import gfx
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        obstacle_size = gfx.obstacle.get_rect().size
        self.width = obstacle_size[0]
        self.height = obstacle_size[1]
    # 장애물 그리기용 변수
    def draw(self):
        screen.blit(gfx.obstacle, (self.x, self.y))
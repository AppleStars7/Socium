import pygame
import gfx
import playerdata as p
import grid
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Portal:
    def __init__(self, x, y):
        portal_size = gfx.portal.get_rect().size
        self.width = portal_size[0]
        self.height = portal_size[1]
        self.x = x
        self.y = y
    # 포탈 그리기용 함수
    def draw(self):
        if not p.stage == 3:
            screen.blit(gfx.portal, (self.x, self.y))
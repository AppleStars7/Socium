import pygame
import gfx
from item import Item
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Box:
    def __init__(self, x, y, item_code):
        self.x = x
        self.y = y
        self.item_code = item_code
        self.collected = False
        self.box = gfx.box
        box_size = self.box.get_rect().size
        self.width = box_size[0]
        self.height = box_size[1]
        self.check = True
    # 박스 그리기용 함수
    def draw(self):
        screen.blit(self.box, (self.x, self.y))
    # 박스 획득
    def collect(self):
        if not self.collected:
            self.collected = True
            self.box = gfx.box_open
            box_size = self.box.get_rect().size
            self.width = box_size[0]
            self.height = box_size[1]
    # 박스 아이템생성
    def item_generate(self):
        if self.collected and self.check:
            new_item = Item(self.x, self.y-50, self.item_code)
            self.check = False
            return new_item
        else:
            return 0
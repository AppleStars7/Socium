import pygame
import gfx
import math
import playerdata as p
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Bat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 15 * p.monsterhp # 박쥐 체력
        bat_size = gfx.bat.get_rect().size
        self.width = bat_size[0]
        self.height = bat_size[1]
        self.speed = 0.2 * p.monsterspeed # 박쥐 이속
        
    # 박쥐 그리기용 함수
    def draw(self): 
        screen.blit(gfx.bat, (self.x, self.y))
    # 박쥐 이동용 함수
    def move_bat(self, character_x, character_y, dt):
        if not p.timestop:
            dx = character_x - self.x
            dy = character_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                self.bat_to_x = (dx / distance) * self.speed
                self.bat_to_y = (dy / distance) * self.speed
            self.x += self.bat_to_x * dt
            self.y += self.bat_to_y * dt
    # 박쥐 피격
    def damage(self):
        self.health -= p.realdamage
    # 박쥐 사망
    def is_dead(self):
        return self.health <= 0
        
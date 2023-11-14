import pygame
import gfx
import font
import playerdata as p
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Devilitem:
    def __init__(self, x, y, item_code):
        self.x = x
        self.y = y
        self.item_code = item_code
        self.collected = False
        self.item = None
        self.health = 30
        # 아이템 코드별 이미지 저장 및 가격설정
        if item_code == 1:
            devilitem_size = gfx.item1.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item1
            self.health = 15
            self.des = '체력 +30'
        elif item_code == 2:
            devilitem_size = gfx.item2.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item2
            self.health = 60
            self.des = '공격속도 +0.7'
        elif item_code == 3:
            devilitem_size = gfx.item3.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item3
            self.health = 30
            self.des = '이동속도 +0.15'
        elif item_code == 4:
            devilitem_size = gfx.item4.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item4
            self.health = 90
            self.des = '데미지 +2'
        elif item_code == 5:
            devilitem_size = gfx.item5.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item5
            self.health = 15
            self.des = '돈 획득량 +50%'
        elif item_code == 6:
            devilitem_size = gfx.item6.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item6
            self.health = 60
            self.des = '방어력 +15%'
        elif item_code == 7:
            devilitem_size = gfx.item7.get_rect().size
            self.width = devilitem_size[0]
            self.height = devilitem_size[1]
            self.item = gfx.item7
            self.health = 30
            self.des = '스킬쿨타임 +15%'
    # 그리기용함수
    def draw(self):
        if not self.collected and self.item is not None:
            screen.blit(self.item, (self.x, self.y))
            health_text = font.game_font.render(f"{self.health}", True, (255, 255, 255))
            screen.blit(health_text, (self.x, self.y+35))
            item_des = font.game_font.render(f"{self.des}", True, (255, 255, 255))
            screen.blit(item_des, (self.x-self.width/2, self.y-35))
    # 수집용함수 및 효과
    def collect(self):
        if not self.collected:
            self.collected = True
            if self.item:
                p.character_health -= self.health #가격
                if self.item == gfx.item1:
                    p.character_health += 30
                elif self.item == gfx.item2:
                    p.itemdelay += 0.7
                elif self.item == gfx.item3:
                    p.speed += 0.15
                elif self.item == gfx.item4:
                    p.itemdamage += 2.0
                elif self.item == gfx.item5:
                    p.monstermoney *= 1.5
                elif self.item == gfx.item6:
                    p.monsterdamage *= 0.85
                elif self.item == gfx.item7:
                    p.skilcooltime *= 0.85
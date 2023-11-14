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
class Shopitem:
    def __init__(self, x, y, item_code):
        self.x = x
        self.y = y
        self.item_code = item_code
        self.collected = False
        self.item = None
        self.money = 100
        # 아이템 코드별 이미지 저장 및 가격설정
        if item_code == 1:
            shopitem_size = gfx.item1.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item1
            self.money = 160
            self.des = '체력 +30'
        elif item_code == 2:
            shopitem_size = gfx.item2.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item2
            self.money = 200
            self.des = '공격속도 +0.7'
        elif item_code == 3:
            shopitem_size = gfx.item3.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item3
            self.money = 300
            self.des = '이동속도 +0.15'
        elif item_code == 4:
            shopitem_size = gfx.item4.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item4
            self.money = 400
            self.des = '데미지 +2'
        elif item_code == 5:
            shopitem_size = gfx.item5.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item5
            self.money = 360
            self.des = '돈 획득량 +50%'
        elif item_code == 6:
            shopitem_size = gfx.item6.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item6
            self.money = 200
            self.des = '방어력 +15%'
        elif item_code == 7:
            shopitem_size = gfx.item7.get_rect().size
            self.width = shopitem_size[0]
            self.height = shopitem_size[1]
            self.item = gfx.item7
            self.money = 300
            self.des = '스킬쿨타임 +15%'
    # 그리기용함수
    def draw(self):
        if not self.collected and self.item is not None:
            screen.blit(self.item, (self.x, self.y))
            money_text = font.game_font.render(f"{self.money*p.itemprice}", True, (255, 255, 255))
            screen.blit(money_text, (self.x, self.y+35))
            item_des = font.game_font.render(f"{self.des}", True, (255, 255, 255))
            screen.blit(item_des, (self.x-self.width/2, self.y-35))
    # 수집용함수 및 효과
    def collect(self):
        if not self.collected and p.money >= self.money*p.itemprice:
            self.collected = True
            if self.item:
                p.money -= self.money*p.itemprice #가격
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
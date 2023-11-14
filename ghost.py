import pygame
import gfx
import random
import grid
import playerdata as p
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        ghost_size = gfx.ghost.get_rect().size
        self.width = ghost_size[0]
        self.height = ghost_size[1]
        self.disappearing = False
        self.last_update_time = pygame.time.get_ticks() 
        self.update_interval = random.randint(1000, 10000)  # 유령 텔포 속도
        self.health = 15 * p.monsterhp
    def update(self):
        if not p.timestop:
            current_time = pygame.time.get_ticks()  # 현재 시간 가져오기
            time_since_last_update = current_time - self.last_update_time

            if time_since_last_update >= self.update_interval:
                self.last_update_time = current_time

                # 유령 상태 변경
                self.disappearing = not self.disappearing

                # 유령이 나타날 랜덤한 위치 설정
                if self.disappearing:
                    self.x = grid.grid_pos_x(random.randint(0, 12))
                    self.y = grid.grid_pos_y(random.randint(0, 6))
    # 유령 피격
    def damage(self):
        self.health -= p.realdamage
    # 유령 사망
    def is_dead(self):
        return self.health <= 0
    # 유령 그리기용 함수
    def draw(self):
        if not self.disappearing:
            screen.blit(gfx.ghost, (self.x, self.y))
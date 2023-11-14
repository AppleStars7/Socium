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
class Skeleton:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        skeleton_size = gfx.skeleton.get_rect().size
        self.width = skeleton_size[0]
        self.height = skeleton_size[1]
        self.speed = p.monstershotspeed
        self.health = 20 * p.monsterhp
        projectile_size = gfx.skeleton.get_rect().size
        self.projectile_width = projectile_size[0]
        self.projectile_height = projectile_size[1]
        self.projectiles = []
        self.shoot_timer = pygame.time.get_ticks()
    # 스켈레톤 투사체 저장
    def update(self, player_x, player_y, dt):
        if not p.timestop:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_timer > p.monstershotdelay:  # 1초마다 발사
                player_to_skeleton_x = player_x - self.x_pos
                player_to_skeleton_y = player_y - self.y_pos
                angle = math.atan2(player_to_skeleton_y, player_to_skeleton_x)
                self.projectiles.append([self.x_pos, self.y_pos, math.cos(angle) * self.speed, math.sin(angle) * self.speed])
                self.shoot_timer = current_time

            for proj in self.projectiles:
                proj[0] += proj[2] * dt
                proj[1] += proj[3] * dt
    # 그리기용함수
    def draw(self):
        screen.blit(gfx.skeleton, (self.x_pos, self.y_pos))
        for proj in self.projectiles:
            screen.blit(gfx.skeleton_projectile, (proj[0], proj[1]))
    # 피격
    def damage(self):
        self.health -= p.realdamage
    # 사망
    def is_dead(self):
        return self.health <= 0
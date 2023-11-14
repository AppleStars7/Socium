import pygame
import gfx
import math
from bat import Bat
import playerdata as p
# 기본 초기화
pygame.init()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
class Boss:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        boss_size = gfx.boss.get_rect().size
        self.width = boss_size[0]
        self.height = boss_size[1]
        self.speed = p.monstershotspeed # 보스 투사체속도
        self.health = 300 * p.monsterhp # 보스 체력
        projectile_size = gfx.boss_projectile.get_rect().size
        self.projectile_width = projectile_size[0]
        self.projectile_height = projectile_size[1]
        self.projectiles = []
        self.can_shoot = True
        self.can_summon = True
        self.pattern = 1
        self.last_pattern_switch = pygame.time.get_ticks()

    def update(self, player_x, player_y, dt):
        if not p.timestop:
            # 보스 패턴 돌아가는 시간
            if p.stage == 1:
                pattern = 2500
            else:
                pattern = 1000
            current_time = pygame.time.get_ticks()
            if current_time - self.last_pattern_switch >= pattern:  # 패턴 순환용
                self.pattern = (self.pattern % 2) + 1  # 패턴 번호를 1, 2 순환
                self.last_pattern_switch = current_time
                self.can_shoot = True
                self.can_summon = False
            # 패턴 1 - 박쥐소환
            if self.pattern == 1 and self.can_summon:
                self.bat_generate()
                self.can_summon = False
            # 패턴 2 - 탄환 발사
            elif self.pattern == 2 and self.can_shoot:
                boss_center_x = self.x_pos + self.width / 2
                boss_center_y = self.y_pos + self.height / 2
                player_to_boss_x = player_x - boss_center_x
                player_to_boss_y = player_y - boss_center_y
                # 5발 발사(1~2스테이지)
                if p.stage != 3:
                    for angle_offset in [0, 5, 10, -5, -10]:
                        angle = math.atan2(player_to_boss_y, player_to_boss_x) + math.radians(angle_offset)
                        # 총알 초기 위치를 보스 중앙으로 설정
                        initial_bullet_x = boss_center_x
                        initial_bullet_y = boss_center_y
                        self.projectiles.append([initial_bullet_x, initial_bullet_y, math.cos(angle) * self.speed, math.sin(angle) * self.speed])
                # 8발 발사(3스테이지)
                else:
                    for angle_offset in [0, 45, 90, 135, 180, 225, 270, 305]:
                        angle = math.atan2(player_to_boss_y, player_to_boss_x) + math.radians(angle_offset)
                        # 총알 초기 위치를 보스 중앙으로 설정
                        initial_bullet_x = boss_center_x
                        initial_bullet_y = boss_center_y
                        self.projectiles.append([initial_bullet_x, initial_bullet_y, math.cos(angle) * self.speed, math.sin(angle) * self.speed])
                if p.stage != 3:
                    self.can_shoot = False

            for proj in self.projectiles:
                proj[0] += proj[2] * dt
                proj[1] += proj[3] * dt
    # 보스 그리기용 함수
    def draw(self):
        screen.blit(gfx.boss, (self.x_pos, self.y_pos))
        for proj in self.projectiles:
            screen.blit(gfx.boss_projectile, (proj[0], proj[1]))
    # 보스피격
    def damage(self):
        self.health -= p.realdamage
    # 보스사망
    def is_dead(self):
        return self.health <= 0
    # 박쥐 소환용 함수
    def bat_generate(self):
            new_bat = Bat(self.x_pos+self.width/2, self.y_pos+50)
            return new_bat
    
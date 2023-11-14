import pygame
import gfx
import playerdata as p
import sfx
def start():
    pygame.init()
    screen_width = 960
    screen_height = 540
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("소시움")
    clock = pygame.time.Clock()
    scene = 1 # 현재 화면
    running = True
    current_sound = sfx.startsound
    current_sound.play(-1)
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 화면 이동
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if scene <= 6:
                        scene += 1
                if event.key == pygame.K_BACKSPACE:
                    if scene >= 2:
                        scene -= 1
                # 캐릭 선택
                if scene == 7:
                    if event.key == pygame.K_1:
                        p.dealer = True
                        current_sound.stop()
                        running = False
                    elif event.key == pygame.K_2:
                        p.healer = True
                        current_sound.stop()
                        running = False
                    elif event.key == pygame.K_3:
                        p.tanker = True
                        current_sound.stop()
                        running = False
                    elif event.key == pygame.K_4:
                        p.prist = True
                        current_sound.stop()
                        running = False
                    elif event.key == pygame.K_5:
                        p.thief = True
                        current_sound.stop()
                        running = False
        # 화면 그리기
        if scene == 1:
            screen.blit(gfx.title, (0,0))
        elif scene == 2:
            screen.blit(gfx.start1, (0,0))
        elif scene == 3:
            screen.blit(gfx.start2, (0,0))
        elif scene == 4:
            screen.blit(gfx.start3, (0,0))
        elif scene == 5:
            screen.blit(gfx.start4, (0,0))
        elif scene == 6:
            screen.blit(gfx.start5, (0,0))
        elif scene == 7:
            screen.blit(gfx.select, (0,0))
        pygame.display.update()
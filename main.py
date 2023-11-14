import pygame
import math
import maparray
import gfx
import time
from roommake import Roommake
import playerdata as p
import start
import random
import sfx
import font
# 기본 초기화
pygame.init()
# 시작화면
start.start()
# 화면 크기 설정
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))

# 미니맵 크기 설정
mini_map_x = 820
mini_map_y = 10
mini_map_cell_size = 10
#그리드 시각화용 변수(테스트용)
grid_start_x = 146
grid_end_x = 812
grid_step_x = 52
grid_start_y = 79
grid_end_y = 460
grid_step_y = 55
# 공격 딜레이 변수 초기값
last_key_time = 0
# 화면 타이틀
pygame.display.set_caption("소시움")

# fps
clock = pygame.time.Clock()
# 무적시간 함수
invincibility_start_time = 0  # 무적 시작 시간을 추적할 변수
def draw_invincibility_text():
    current_time = time.time()
    remaining_time = max(0, invincibility_start_time + p.invincibility_time - current_time)
    if remaining_time > 0:
        invincibility_text = font.game_font.render(f"무적 : {remaining_time:.1f} 초", True, (255, 0, 0))  # 무적 상태 메시지 설정
        screen.blit(invincibility_text, (10, 150))  # 화면에 메시지 그리기
# 탱딜힐 변수 초기값

dealer_skill_active = False
tanker_skill_active = False
healer_skill_active = False
revive_skill_active = False
dealer_skill_direction = (0, 0)
dealer_effect_start_time = 0
tanker_effect_start_time = 0
healer_effect_start_time = 0
dealer_effect_duration = 0.2
tanker_effect_duration = 0.2
healer_effect_duration = 0.2
revive_effect_duration = 0.2
# 스킬 쿨타임 설정
dealer_cooldown = {'duration': 3, 'last_used': 0}
healer_cooldown = {'duration': 30, 'last_used': 0}
tanker_cooldown = {'duration': 6, 'last_used': 0}
# 캐릭터 이미지 설정
if p.dealer:
    character = gfx.dealer1
    character1 = gfx.dealer1
    character2 = gfx.dealer2
    skillicon = gfx.dealerskill
    skillicon_cd = gfx.dealerskill_cd
    p.character_health = 90
    p.basedamge = 7
    p.damagemultiple *= 1.5
    p.revive = 0
if p.healer:
    character = gfx.healer1
    character1 = gfx.healer1
    character2 = gfx.healer2
    skillicon = gfx.healerskill
    skillicon_cd = gfx.healerskill_cd
    p.character_health = 120
    p.basedamge = 7
    p.revive = 0
if p.tanker:
    character = gfx.tanker1
    character1 = gfx.tanker1
    character2 = gfx.tanker2
    skillicon = gfx.tankerskill
    skillicon_cd = gfx.tankerskill_cd
    p.character_health = 60
    p.basedamge = 9
    p.revive = 0
if p.prist:
    character = gfx.prist1
    character1 = gfx.prist1
    character2 = gfx.prist2
    skillicon = gfx.pristskill
    skillicon_cd = gfx.pristskill_cd
    p.character_health = 60
    p.basedamge = 9
    remaining_time = 0
    p.revive = 1
if p.thief:
    character = gfx.thief1
    character1 = gfx.thief1
    character2 = gfx.thief2
    skillicon = gfx.thiefskill
    skillicon_cd = gfx.thiefskill_cd
    p.character_health = 90
    p.basedamge = 7
    remaining_time = 0
    p.revive = 0
    thiefcount = 5
# 캐릭터 크기 저장
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2) - (character_height / 2)
# 캐릭터 히트박스 설정
character_hitbox = 22

# 탄환
projectile_size = gfx.projectile.get_rect().size
projectile_width = projectile_size[0]
projectile_height = projectile_size[1]
projectiles = []
# 보스 몹 소환용 변수
boss_summon = True

# 이동 좌표 변수
to_x = 0
to_y = 0

# 이동 속도 설정
character_speed = 0.3 * p.speed

# 화면 경계값 설정
upscreen = 34
downscreen = 454
leftscreen = 130
rightscreen = 830
# 맵 배열 생성
mapdata = maparray.stage1
# 플레이어 시작 좌표 설정
player_x = 7
player_y = 7
# 문 히트박스 설정
door_hitbox1 = pygame.Rect(457, 38 - 11, gfx.dooropen1.get_width(), gfx.dooropen1.get_height() + 11)
door_hitbox2 = pygame.Rect(104, 247 - 11, gfx.dooropen2.get_width(), gfx.dooropen2.get_height() + 11)
door_hitbox3 = pygame.Rect(818, 247 - 11, gfx.dooropen3.get_width(), gfx.dooropen3.get_height() + 11)
door_hitbox4 = pygame.Rect(457, 464 - 11, gfx.dooropen4.get_width(), gfx.dooropen4.get_height() + 11)
# 방 및 포탈 모듈 가져오기
room = Roommake()
walldata = [[0 for j in range(15)] for i in range(15)]
obstacledata = [[0 for j in range(15)] for i in range(15)]
itemdata = [[0 for j in range(15)] for i in range(15)]
shopitemdata = [[0 for j in range(15)] for i in range(15)]
boxdata = [[0 for j in range(15)] for i in range(15)]
portaldata = [[0 for j in range(15)] for i in range(15)]
devilitemdata = [[0 for j in range(15)] for i in range(15)]
roomcode = [[0 for j in range(15)] for i in range(15)]
roomclear = [[0 for j in range(15)] for i in range(15)]
def save():
    walldata[player_y][player_x] = room.walls
    boxdata[player_y][player_x] = room.boxes
    itemdata[player_y][player_x] = room.items
    shopitemdata[player_y][player_x] = room.shopitems
    obstacledata[player_y][player_x] = room.obstacles
    portaldata[player_y][player_x] = room.portals
    devilitemdata[player_y][player_x] = room.devilitems
def load():
    room.walls = walldata[player_y][player_x]
    room.boxes = boxdata[player_y][player_x]
    room.items = itemdata[player_y][player_x]
    room.shopitems = shopitemdata[player_y][player_x]
    room.obstacles = obstacledata[player_y][player_x]
    room.portals = portaldata[player_y][player_x]
    room.devilitems = devilitemdata[player_y][player_x]
    room.bats = []
    room.skeletons = []
    room.bosses = []
    room.ghosts = []
for i in range(15):
    for j in range(15):
        if mapdata[i][j] != 0:
            roomcode[i][j] = random.randint(1, 5)
# 이벤트 루프
running = True
gameend = False
current_sound = sfx.stage1sound
current_sound.set_volume(0.5)
current_sound.play(-1)
while running:
    dt = clock.tick(60)
    # 캐릭터 스텟 업데이트
    # 캐릭터 데미지 세팅
    p.realdamage = (p.basedamge * math.sqrt(p.itemdamage * 1.2 + 1) + p.extradamage)* p.damagemultiple
    if p.realdamage <= 0.01:
        p.realdamage = 0.01
    # 캐릭터 공격속도 세팅
    if p.itemdelay >= 0:  
        p.totaldelay = (16 - (6 * math.sqrt(p.itemdelay * 1.3 + 1))) * p.delaymultiple
    elif p.itemdelay <= -0.77:
        p.totaldelay = (16 - (6 * p.itemdelay)) * p.delaymultiple
    else:
        p.totaldelay = (16 - 6 * math.sqrt(p.itemdelay * 1.3 + 1) - 6 * p.itemdelay) * p.delaymultiple
    if p.totaldelay <= -0.75:
        p.totaldelay = -0.75
    elif p.totaldelay >= 120:
        p.totaldelay = 120
    elif p.totaldelay <= p.delaylimit:
        p.totaldelay = p.delaylimit
    # 캐릭터 이속 설정
    if p.speed >= 2:
        p.speed = 2
    if p.character_health >= 360:
        p.character_health = 360
    character_speed = 0.3 * p.speed
    p.shotdelay = 1000/(30/(p.totaldelay+1))
    # 캐릭터 쿨타임 설정
    dealer_cooldown['duration'] = 3 * p.skilcooltime
    healer_cooldown['duration'] = 30 * p.skilcooltime
    tanker_cooldown['duration'] = 6 * p.skilcooltime
    # 캐릭터 무적시간 설정
    p.invincibility_time = p.invtimeitem * p.invtimemultiple

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # 캐릭터 이동(wasd)
            if event.key == pygame.K_a:
                character = character1
                to_x -= character_speed
            elif event.key == pygame.K_d:
                character = character2
                to_x += character_speed
            elif event.key == pygame.K_w:
                to_y -= character_speed
            elif event.key == pygame.K_s:
                to_y += character_speed
            # 캐릭터 발사(방향키)
            elif event.key == pygame.K_LEFT:
                current_time = pygame.time.get_ticks()
                if current_time - last_key_time >= p.shotdelay:
                    last_key_time = current_time
                    projectiles.append([character_x_pos, character_y_pos + character_height / 2, -p.shotspeed * p.shotspeedmultiple, "horizontal"])
            elif event.key == pygame.K_RIGHT:
                current_time = pygame.time.get_ticks()
                if current_time - last_key_time >= p.shotdelay:
                    last_key_time = current_time
                    projectiles.append([character_x_pos + character_width, character_y_pos + character_height / 2, p.shotspeed * p.shotspeedmultiple, "horizontal"])
            elif event.key == pygame.K_UP:
                current_time = pygame.time.get_ticks()
                if current_time - last_key_time >= p.shotdelay:
                    last_key_time = current_time
                    angle = math.atan2(-1, 0)  # 위쪽으로의 각도 (라디안)
                    projectiles.append([character_x_pos + character_width / 2, character_y_pos + character_height / 2, angle, "diagonal"])
            elif event.key == pygame.K_DOWN:
                current_time = pygame.time.get_ticks()
                if current_time - last_key_time >= p.shotdelay:
                    last_key_time = current_time
                    angle = math.atan2(1, 0)  # 아래쪽으로의 각도 (라디안)
                    projectiles.append([character_x_pos + character_width / 2, character_y_pos + character_height / 2, angle, "diagonal"])
            # 아이템 획득(스페이스바)
            elif event.key == pygame.K_SPACE:
                # 일반 아이템
                p.timestop = True
                print(p.timestop)
                for item in room.items:
                    if (
                        not item.collected
                        and item.x < character_x_pos + character_width
                        and item.x + item.width > character_x_pos
                        and item.y < character_y_pos + character_height
                        and item.y + item.height > character_y_pos
                    ):
                        item.collect()
                # 상점 아이템
                for shopitem in room.shopitems:
                    if (
                        not shopitem.collected
                        and shopitem.x < character_x_pos + character_width
                        and shopitem.x + shopitem.width > character_x_pos
                        and shopitem.y < character_y_pos + character_height
                        and shopitem.y + shopitem.height > character_y_pos
                    ):
                        shopitem.collect()
                for devilitem in room.devilitems:
                    if (
                        not devilitem.collected
                        and devilitem.x < character_x_pos + character_width
                        and devilitem.x + devilitem.width > character_x_pos
                        and devilitem.y < character_y_pos + character_height
                        and devilitem.y + devilitem.height > character_y_pos
                    ):
                        devilitem.collect()
                # 상자
                for box in room.boxes:
                    if (
                        not box.collected
                        and box.x < character_x_pos + character_width
                        and box.x + box.width > character_x_pos
                        and box.y < character_y_pos + character_height
                        and box.y + box.height > character_y_pos
                    ):
                        box.collect()
                        room.item_genetate()
        # 캐릭터 이동
            # 캐릭터 스킬
            elif event.key == pygame.K_LSHIFT:
                current_time = time.time()
                # 탱커
                if p.tanker:
                    if current_time - tanker_cooldown['last_used'] >= tanker_cooldown['duration']:
                        tanker_cooldown['last_used'] = current_time
                        tanker_skill_active = True
                        invincibility_start_time = time.time()
                        tanker_effect_start_time = current_time
                # 딜러
                if p.dealer:
                    if current_time - dealer_cooldown['last_used'] >= dealer_cooldown['duration']:
                        dealer_cooldown['last_used'] = current_time
                        dealer_skill_active = True
                        dealer_skill_direction = (to_x, to_y)
                        dealer_effect_start_time = current_time
                # 힐러
                if p.healer:
                    if current_time - healer_cooldown['last_used'] >= healer_cooldown['duration']:
                        healer_cooldown['last_used'] = current_time
                        healer_skill_active = True
                        p.character_health += 30
                        healer_effect_start_time = current_time
                if p.thief and thiefcount != 0:
                    thiefcount -= 1
                    for y in range(15):
                        for x in range(15):
                            if mapdata[y][x] == 4:
                                save()
                                character_x_pos = (screen_width / 2) - (character_width / 2)
                                character_y_pos = (screen_height / 2) - (character_height / 2) + 30
                                player_x = x
                                player_y = y
                                room_type = mapdata[player_y][player_x]
                                if (player_y, player_x) not in p.visited_rooms:
                                    p.visited_rooms.append((player_y, player_x))
                                    projectiles = []
                                    room.roomnumber(roomcode[player_y][player_x], room_type)
                                    invincibility_start_time = time.time()
                                else:
                                    if not roomclear[player_y][player_x]:
                                        room.roomnumber(roomcode[player_y][player_x], room_type)
                                    else:
                                        load()
                                    projectiles = []
        # 캐릭터 이동
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
    
    # 캐릭터 이동
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    # 캐릭터 경계값
    if character_x_pos < leftscreen:
        character_x_pos = leftscreen
    elif character_x_pos > rightscreen - character_width:
        character_x_pos = rightscreen - character_width
    if character_y_pos < upscreen:
        character_y_pos = upscreen
    elif character_y_pos > downscreen - character_height:
        character_y_pos = downscreen - character_height
    # 방 구조 확인
    room_type = mapdata[player_y][player_x]
    updoor = mapdata[player_y-1][player_x]
    leftdoor = mapdata[player_y][player_x-1]
    rightdoor = mapdata[player_y][player_x+1]
    downdoor = mapdata[player_y+1][player_x]

    # 문 접촉 감지
    if door_hitbox1.colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)) and roomclear[player_y][player_x] and updoor != 0:
        save()
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = 387
        player_y -= 1
        room_type = mapdata[player_y][player_x]
        if (player_y, player_x) not in p.visited_rooms:
            p.visited_rooms.append((player_y, player_x))
            projectiles = []
            room.roomnumber(roomcode[player_y][player_x], room_type)
            invincibility_start_time = time.time()
        else:
            if not roomclear [player_y][player_x]:
                room.roomnumber(roomcode[player_y][player_x], room_type)
            else:
                load()
            projectiles = []

    if door_hitbox2.colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)) and roomclear[player_y][player_x] and leftdoor!=0:
        save()
        character_x_pos = 762
        character_y_pos = (screen_height / 2) - (character_height / 2)
        player_x -= 1
        room_type = mapdata[player_y][player_x]
        if (player_y, player_x) not in p.visited_rooms:
            p.visited_rooms.append((player_y, player_x))
            projectiles = []
            room.roomnumber(roomcode[player_y][player_x], room_type)
            invincibility_start_time = time.time()
        else:
            if not roomclear [player_y][player_x]:
                room.roomnumber(roomcode[player_y][player_x], room_type)
            else:
                load()
            projectiles = []
            
    if door_hitbox3.colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)) and roomclear[player_y][player_x] and rightdoor!=0:
        save()
        character_x_pos = 142
        character_y_pos = (screen_height / 2) - (character_height / 2)
        player_x += 1
        room_type = mapdata[player_y][player_x]
        if (player_y, player_x) not in p.visited_rooms:
            p.visited_rooms.append((player_y, player_x))
            projectiles = []
            room.roomnumber(roomcode[player_y][player_x], room_type)
            invincibility_start_time = time.time()
        else:
            if not roomclear [player_y][player_x]:
                room.roomnumber(roomcode[player_y][player_x], room_type)
            else:
                load()
            projectiles = []

    if door_hitbox4.colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)) and roomclear[player_y][player_x] and downdoor!=0:
        save()
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = 76
        player_y += 1
        room_type = mapdata[player_y][player_x]
        if (player_y, player_x) not in p.visited_rooms:
            p.visited_rooms.append((player_y, player_x))
            projectiles = []
            room.roomnumber(roomcode[player_y][player_x], room_type)
            invincibility_start_time = time.time()
        else:
            if not roomclear [player_y][player_x]:
                room.roomnumber(roomcode[player_y][player_x], room_type)
            else:
                load()
            projectiles = []
    # 방 클리어 확인
    p.monsternum = len(room.skeletons) + len(room.bats) + len(room.ghosts) + len(room.bosses)
    if p.monsternum <= 0:
        roomclear[player_y][player_x] = True
    
    # 캐릭터 총알 생성
    new_projectiles = []
    for proj in projectiles:
        if proj[3] == "horizontal":
            proj[0] += proj[2] * dt
        elif proj[3] == "diagonal":
            proj[0] += math.cos(proj[2]) * p.shotspeed * dt * p.shotspeedmultiple
            proj[1] += math.sin(proj[2]) * p.shotspeed * dt * p.shotspeedmultiple

        if leftscreen <= proj[0] <= rightscreen and upscreen <= proj[1] <= downscreen:
            new_projectiles.append(proj)
    projectiles = new_projectiles
    
    # 배경 그리기
    screen.blit(gfx.basebg, (0, 0))
    # 배경 체크
    if room_type != 3 or 7:
        screen.blit(gfx.background1, (64, 0))
        screen.blit(gfx.background2, (480, 0))
        screen.blit(gfx.background3, (64, 270))
        screen.blit(gfx.background4, (480, 270))
    else:
        screen.blit(gfx.background_shop1, (64, 0))
        screen.blit(gfx.background_shop2, (480, 0))
        screen.blit(gfx.background_shop3, (64, 270))
        screen.blit(gfx.background_shop4, (480, 270))
    # 문 체크
    if updoor == 1 and room_type == 1:
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen1, (457,38))
        else:
            screen.blit(gfx.doorclose11, (457,38))
            screen.blit(gfx.doorclose21, (480,38))
        screen.blit(gfx.door1, (435,21))
    elif (updoor == 2 and room_type != 7) or (room_type == 2 and updoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen1, (457,38))
        else:
            screen.blit(gfx.doorclose11, (457,38))
            screen.blit(gfx.doorclose21, (480,38))
        screen.blit(gfx.door1_boss, (424,10))
    elif (updoor == 3 and room_type != 7) or (room_type == 3 and updoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen1, (457,38))
        else:
            screen.blit(gfx.doorclose11, (457,38))
            screen.blit(gfx.doorclose21, (480,38))
        screen.blit(gfx.door1_shop, (435,19))
    elif (updoor == 4 and room_type != 7) or (room_type == 4 and updoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen1, (457,38))
        else:
            screen.blit(gfx.doorclose11, (457,38))
            screen.blit(gfx.doorclose21, (480,38))
        screen.blit(gfx.door1_treasure, (435,11))
    elif (updoor == 7 and room_type == 2) or (room_type == 7 and updoor == 2):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen1, (457,38))
        else:
            screen.blit(gfx.doorclose11, (457,38))
            screen.blit(gfx.doorclose21, (480,38))
        screen.blit(gfx.door1_shop, (435,19))
    if leftdoor == 1 and room_type == 1:
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen2, (104,247))
        else:
            screen.blit(gfx.doorclose12, (104,270))
            screen.blit(gfx.doorclose22, (104,247))
        screen.blit(gfx.door2, (87,225))
    elif (leftdoor == 2 and room_type != 7) or (room_type == 2 and leftdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen2, (104,247))
        else:
            screen.blit(gfx.doorclose12, (104,270))
            screen.blit(gfx.doorclose22, (104,247))
        screen.blit(gfx.door2_boss, (76,214))
    elif (leftdoor == 3 and room_type != 7) or (room_type == 3  and leftdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen2, (104,247))
        else:
            screen.blit(gfx.doorclose12, (104,270))
            screen.blit(gfx.doorclose22, (104,247))
        screen.blit(gfx.door2_shop, (85,225))
    elif (leftdoor == 4 and room_type != 7) or (room_type == 4 and leftdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen2, (104,247))
        else:
            screen.blit(gfx.doorclose12, (104,270))
            screen.blit(gfx.doorclose22, (104,247))
        screen.blit(gfx.door2_treasure, (77,225))
    elif (leftdoor == 7 and room_type == 2) or (room_type == 7 and leftdoor == 2):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen2, (104,247))
        else:
            screen.blit(gfx.doorclose12, (104,270))
            screen.blit(gfx.doorclose22, (104,247))
        screen.blit(gfx.door2_shop, (85,225))
    if rightdoor == 1 and room_type == 1:
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen3, (818,247))
        else:
            screen.blit(gfx.doorclose13, (818,247))
            screen.blit(gfx.doorclose23, (818,270))
        screen.blit(gfx.door3, (813,225))
    if (rightdoor == 2 and room_type != 7) or (room_type == 2 and rightdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen3, (818,247))
        else:
            screen.blit(gfx.doorclose13, (818,247))
            screen.blit(gfx.doorclose23, (818,270))
        screen.blit(gfx.door3_boss, (813,214))
    elif (rightdoor == 3 and room_type != 7) or (room_type == 3 and rightdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen3, (818,247))
        else:
            screen.blit(gfx.doorclose13, (818,247))
            screen.blit(gfx.doorclose23, (818,270))
        screen.blit(gfx.door3_shop, (813,225))
    if (rightdoor == 4 and room_type != 7) or (room_type == 4 and rightdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen3, (818,247))
        else:
            screen.blit(gfx.doorclose13, (818,247))
            screen.blit(gfx.doorclose23, (818,270))
        screen.blit(gfx.door3_treasure, (813,225))
    elif (rightdoor == 7 and room_type == 2) or (room_type == 7 and rightdoor == 2):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen3, (818,247))
        else:
            screen.blit(gfx.doorclose13, (818,247))
            screen.blit(gfx.doorclose23, (818,270))
        screen.blit(gfx.door3_shop, (813,225))
    if downdoor == 1 and room_type == 1:
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen4, (457,464))
        else:
            screen.blit(gfx.doorclose14, (480,464))
            screen.blit(gfx.doorclose24, (457,464))
        screen.blit(gfx.door4, (435,459))
    elif (downdoor == 2 and room_type != 7) or (room_type == 2 and downdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen4, (457,464))
        else:
            screen.blit(gfx.doorclose14, (480,464))
            screen.blit(gfx.doorclose24, (457,464))
        screen.blit(gfx.door4_boss, (424,459))
    elif (downdoor == 3 and room_type != 7) or (room_type == 3 and downdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen4, (457,464))
        else:
            screen.blit(gfx.doorclose14, (480,464))
            screen.blit(gfx.doorclose24, (457,464))
        screen.blit(gfx.door4_shop, (435,459))
    elif (downdoor == 4 and room_type != 7) or (room_type == 4 and downdoor == 1):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen4, (457,464))
        else:
            screen.blit(gfx.doorclose14, (480,464))
            screen.blit(gfx.doorclose24, (457,464))
        screen.blit(gfx.door4_treasure, (435,459))
    elif (downdoor == 7 and room_type == 2) or (room_type == 7 and downdoor == 2):
        if roomclear[player_y][player_x]:
            screen.blit(gfx.dooropen4, (457,464))
        else:
            screen.blit(gfx.doorclose14, (480,464))
            screen.blit(gfx.doorclose24, (457,464))
        screen.blit(gfx.door4_shop, (435,459))
    # 오브젝트 접촉 처리
    # 장애물
    for obstacle in room.obstacles:
        if (
            character_x_pos + character_hitbox < obstacle.x + obstacle.width
            and character_x_pos + character_width - character_hitbox > obstacle.x
            and character_y_pos + character_hitbox < obstacle.y + obstacle.height
            and character_y_pos + character_height - character_hitbox > obstacle.y
        ):
            if time.time() - invincibility_start_time > p.invincibility_time:
                invincibility_start_time = time.time()
                p.character_health -= 10 * p.obstacledamage
                p.devilper -= 5
            character_x_pos -= to_x * dt
            character_y_pos -= to_y * dt
    # 벽
    for wall in room.walls:
        if (
            character_x_pos + character_hitbox < wall.x + wall.width
            and character_x_pos + character_width - character_hitbox> wall.x
            and character_y_pos + character_hitbox < wall.y + wall.height
            and character_y_pos + character_height - character_hitbox> wall.y
        ):
            character_x_pos -= to_x * dt
            character_y_pos -= to_y * dt
    for portal in room.portals:
        if (
            character_x_pos + character_hitbox< portal.x + portal.width
            and character_x_pos + character_width - character_hitbox > portal.x
            and character_y_pos + character_hitbox< portal.y + portal.height
            and character_y_pos + character_height - character_hitbox > portal.y
            and p.monsternum <= 1
        ):
            if p.stage == 1:
                room.portals = []
                mapdata = maparray.stage2
                player_x = 7
                player_y = 7
                p.visited_rooms = [(6, 6)]
                p.stage = 2
                p.monsternum = 0
                gfx.bat = gfx.bat2
                gfx.skeleton = gfx.skeleton2
                gfx.ghost = gfx.ghost2
                gfx.boss = gfx.boss2
                gfx.background = gfx.background_2
                gfx.background1 = gfx.background1_2
                gfx.background2 = gfx.background2_2
                gfx.background3 = gfx.background3_2
                gfx.background4 = gfx.background4_2
                p.monsterdamage *= 2
                p.monsterhp *= 2
                p.itemprice *= 2
                p.monstermoney *= 2
                room.roomnumber(0, 0)
                current_sound.stop()
                current_sound = sfx.stage2sound
                current_sound.play(-1)
                p.bossclear = False
                p.devilper = 100
            elif p.stage == 2:
                room.portals
                mapdata = maparray.stage3
                player_x = 7
                player_y = 7
                p.visited_rooms = [(6, 6)]
                p.stage = 3
                p.monsternum = 0
                gfx.bat = gfx.bat3
                gfx.skeleton = gfx.skeleton3
                gfx.ghost = gfx.ghost3
                gfx.boss = gfx.boss3
                gfx.background = gfx.background_3
                gfx.background1 = gfx.background1_3
                gfx.background2 = gfx.background2_3
                gfx.background3 = gfx.background3_3
                gfx.background4 = gfx.background4_3
                p.monsterdamage *= 1.5
                p.monsterhp *= 1.5
                p.monstermoney *= 1.5
                p.itemprice *= 1.5
                room.roomnumber(0, 0)
                current_sound.stop()
                current_sound = sfx.stage3sound
                current_sound.play(-1)
                p.bossclear = False
                p.devilper = 100
    # 상자
    for box in room.boxes:
        if (
            character_x_pos + character_hitbox< box.x + box.width
            and character_x_pos + character_width - character_hitbox> box.x
            and character_y_pos + character_hitbox < box.y + box.height
            and character_y_pos + character_height - character_hitbox > box.y
        ):
            character_x_pos -= to_x * dt
            character_y_pos -= to_y * dt
    # 박쥐 경계값
    for bat in room.bats:
        if bat.x < leftscreen:
            bat.x = leftscreen
        elif bat.x > rightscreen - bat.width:
            bat.x = rightscreen  - bat.width
        if bat.y < upscreen:
            bat.y = upscreen
        elif bat.y > downscreen - bat.height:
            bat.y = downscreen - bat.height
    # 박쥐
    for bat in room.bats:
        if (
            character_x_pos + character_hitbox< bat.x + bat.width
            and character_x_pos + character_width - character_hitbox > bat.x
            and character_y_pos + character_hitbox < bat.y + bat.height
            and character_y_pos + character_height - character_hitbox > bat.y
        ):
            dx_b = bat.x - character_x_pos
            dy_b = bat.y - character_y_pos
            distance_b = math.sqrt(dx_b ** 2 + dy_b ** 2)
            if distance_b > 0:
                move_x_b = (dx_b / distance_b) * p.collision_distance
                move_y_b = (dy_b / distance_b) * p.collision_distance

                # 플레이어와 좀비에게 넉백 효과 적용
                #character_x_pos -= move_x_b
                #character_y_pos -= move_y_b
                bat.x += move_x_b
                bat.y += move_y_b
            if time.time() - invincibility_start_time > p.invincibility_time:
                invincibility_start_time = time.time()
                p.character_health -= 10 * p.monsterdamage
                p.devilper -= 5
    # 박쥐 피격
    for bat in room.bats:
        for proj in projectiles:
            if (
                bat.x < proj[0] + projectile_width
                and bat.x + bat.width > proj[0]
                and bat.y < proj[1] + projectile_height
                and bat.y + bat.height > proj[1]
            ):
                if proj in projectiles:
                    projectiles.remove(proj)
                bat.damage()
                dx_bat = bat.x - proj[0]
                dy_bat = bat.y - proj[1]
                distance_bat = math.sqrt(dx_bat ** 2 + dy_bat ** 2)
                if distance_bat > 0:
                    # 충돌 방향으로 조금 밀어내기 (투사체의 반대 방향)
                    move_x_bat = (dx_bat / distance_bat) * p.collision_distance_bullet
                    move_y_bat = (dy_bat / distance_bat) * p.collision_distance_bullet
                    bat.x += move_x_bat
                    bat.y += move_y_bat

    # 스켈레톤 경계값
    for skeleton in room.skeletons:
        if skeleton.x_pos < leftscreen:
            skeleton.x_pos = leftscreen
        elif skeleton.x_pos > rightscreen - skeleton.width:
            skeleton.x_pos = rightscreen - skeleton.width
        if skeleton.y_pos < upscreen:
            skeleton.y_pos = upscreen
        elif skeleton.y_pos > downscreen - skeleton.height:
            skeleton.y_pos = downscreen - skeleton.height
    # 스켈레톤 피격
    for skeleton in room.skeletons:
        for proj in projectiles:
            if (
                skeleton.x_pos < proj[0] + projectile_width
                and skeleton.x_pos + skeleton.width > proj[0]
                and skeleton.y_pos < proj[1] + projectile_height
                and skeleton.y_pos + skeleton.height > proj[1]
            ):
                if proj in projectiles:
                    projectiles.remove(proj)
                skeleton.damage()
                dx_skeleton = skeleton.x_pos - proj[0]
                dy_skeleton = skeleton.y_pos - proj[1]
                distance_skeleton = math.sqrt(dx_skeleton ** 2 + dy_skeleton ** 2)
                if distance_skeleton > 0:
                    move_x_skeleton = (dx_skeleton / distance_skeleton) * p.collision_distance_bullet
                    move_y_skeleton = (dy_skeleton / distance_skeleton) * p.collision_distance_bullet
                    skeleton.x_pos += move_x_skeleton
                    skeleton.y_pos += move_y_skeleton

    # 스켈레톤
    for skeleton in room.skeletons:
        if (
            character_x_pos + character_hitbox < skeleton.x_pos + skeleton.width
            and character_x_pos + character_width - character_hitbox > skeleton.x_pos
            and character_y_pos + character_hitbox < skeleton.y_pos + skeleton.height
            and character_y_pos + character_height - character_hitbox > skeleton.y_pos
        ):
            dx_s = skeleton.x_pos - character_x_pos
            dy_s = skeleton.y_pos - character_y_pos
            distance_s = math.sqrt(dx_s ** 2 + dy_s ** 2)

            if distance_s > 0:
                # 충돌 방향으로 조금 밀어내기
                move_x_s = (dx_s / distance_s) * p.collision_distance
                move_y_s = (dy_s / distance_s) * p.collision_distance

                skeleton.x_pos += move_x_s
                skeleton.y_pos += move_y_s
            if time.time() - invincibility_start_time > p.invincibility_time:
                invincibility_start_time = time.time()
                p.character_health -= 10 * p.monsterdamage
                p.devilper -= 5
    # 스켈레톤 투사체
    for skeleton in room.skeletons:
        for proj in skeleton.projectiles:
            if (
                character_x_pos + character_hitbox < proj[0] + skeleton.projectile_width
                and character_x_pos + character_width - character_hitbox > proj[0]
                and character_y_pos + character_hitbox < proj[1] + skeleton.projectile_height
                and character_y_pos + character_height - character_hitbox > proj[1]
            ):
                if proj in skeleton.projectiles:
                    skeleton.projectiles.remove(proj)
                if time.time() - invincibility_start_time > p.invincibility_time:
                    invincibility_start_time = time.time()
                    p.character_health -= 10 * p.monsterdamage
                    p.devilper -= 5
            if not leftscreen <= proj[0] <= rightscreen and upscreen <= proj[1] <= downscreen:
                if proj in skeleton.projectiles:
                    skeleton.projectiles.remove(proj)
    # 보스
    for boss in room.bosses:
        if (
            character_x_pos + character_hitbox < boss.x_pos + boss.width
            and character_x_pos + character_width - character_hitbox > boss.x_pos
            and character_y_pos + character_hitbox < boss.y_pos + boss.height
            and character_y_pos + character_height - character_hitbox> boss.y_pos
        ):
            character_x_pos -= to_x * dt
            character_y_pos -= to_y * dt
            if time.time() - invincibility_start_time > p.invincibility_time:
                invincibility_start_time = time.time()
                p.character_health -= 10 * p.monsterdamage
                p.devilper -= 5
    # 보스 피격
    for boss in room.bosses:
        for proj in projectiles:
            if (
                boss.x_pos < proj[0] + projectile_width
                and boss.x_pos + boss.width > proj[0]
                and boss.y_pos < proj[1] + projectile_height
                and boss.y_pos + boss.height > proj[1]
            ):
                if proj in projectiles:
                    projectiles.remove(proj)
                boss.damage()
    # 보스 투사체
    for boss in room.bosses:
        for proj in boss.projectiles:
            if (
                character_x_pos + character_hitbox < proj[0] + boss.projectile_width
                and character_x_pos + character_width - character_hitbox > proj[0]
                and character_y_pos + character_hitbox < proj[1] + boss.projectile_height
                and character_y_pos + character_height - character_hitbox > proj[1]
            ):
                if proj in boss.projectiles:
                    boss.projectiles.remove(proj)
                if time.time() - invincibility_start_time > p.invincibility_time:
                    invincibility_start_time = time.time()
                    p.character_health -= 10 * p.monsterdamage
                    p.devilper -= 5
            if not leftscreen <= proj[0] <= rightscreen and upscreen <= proj[1] <= downscreen:
                if proj in boss.projectiles:
                    boss.projectiles.remove(proj)

    # 유령
    for ghost in room.ghosts:
        if (
            character_x_pos + character_hitbox< ghost.x + ghost.width
            and character_x_pos + character_width - character_hitbox > ghost.x
            and character_y_pos + character_hitbox < ghost.y + ghost.height
            and character_y_pos + character_height - character_hitbox > ghost.y
            and not ghost.disappearing
        ):
            if time.time() - invincibility_start_time > p.invincibility_time:
                invincibility_start_time = time.time()
                p.character_health -= 10 * p.monsterdamage
                p.devilper -= 5
    # 유령 피격
    for ghost in room.ghosts:
        for proj in projectiles:
            if (
                ghost.x < proj[0] + projectile_width
                and ghost.x + ghost.width > proj[0]
                and ghost.y < proj[1] + projectile_height
                and ghost.y + ghost.height > proj[1]
                and not ghost.disappearing
            ):
                if proj in projectiles:
                    projectiles.remove(proj)
                ghost.damage()
    # 게임 구성요소 그리기
    # 캐릭터
    screen.blit(character, (character_x_pos, character_y_pos))
    # 방
    room.draw(character_x_pos, character_y_pos, dt)
    # 보스패턴
    for boss in room.bosses:
        if boss.pattern == 1 and boss_summon:
            room.bat_generate()
            p.monsternum += 1
            boss_summon = False
        elif boss.pattern == 2:
            boss_summon = True
    
    # 악마방생성
    if p.devilroom:
        if updoor != 2:
            mapdata[player_y-1][player_x] = 6
        else:
            mapdata[player_y][player_x+1] = 6
        p.devilroom = False
    if p.bossclear:
        p.devilper = 0
    # 체력바
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, p.character_health, 10))
    # 보스 체력바
    for boss in room.bosses:
        pygame.draw.rect(screen, (255, 0, 0), (480-boss.health/2/2, 400, boss.health/2, 20))
    # 캐릭터 총알
    for proj in projectiles:
        screen.blit(gfx.projectile, (proj[0], proj[1]))
    # 딜러스킬 이펙트
    if dealer_skill_active:
        if time.time() - dealer_effect_start_time <= dealer_effect_duration:
            character_x_pos += dealer_skill_direction[0] * (dt * 2)  # 이펙트 속도 증가
            character_y_pos += dealer_skill_direction[1] * (dt * 2)  # 이펙트 속도 증가
            pygame.draw.circle(screen, (255, 0, 0), (int(character_x_pos+character_width/2), int(character_y_pos+character_height/2)), 50)
        else:
            dealer_skill_active = False
    # 탱커스킬 이펙트
    if tanker_skill_active:
        if time.time() - tanker_effect_start_time <= tanker_effect_duration:
            pygame.draw.circle(screen, (0, 0, 255), (int(character_x_pos+character_width/2), int(character_y_pos+character_height/2)), 50)
        else:
            tanker_skill_active = False
    # 힐러스킬 이펙트
    if healer_skill_active:
        if time.time() - healer_effect_start_time <= healer_effect_duration:
            pygame.draw.circle(screen, (0, 255, 0), (int(character_x_pos+character_width/2), int(character_y_pos+character_height/2)), 50)
        else:
            healer_skill_active = False
    # 부활
    if p.character_health <= 0 and p.revive >= 1:
        p.revive -= 1
        if p.money >= 1000:
            p.money -= 1000
            p.character_health = 30
            revive_skill_active = True
            invincibility_start_time = time.time()
    if revive_skill_active:
        if time.time() - current_time <= revive_effect_duration:
            pygame.draw.circle(screen, (255, 255, 255), (int(character_x_pos+character_width/2), int(character_y_pos+character_height/2)), 50)
        else:
            revive_skill_active = False
    # 스킬 쿨 그리기
    # 쿨타임 텍스트 생성
    current_time = time.time()
    if p.dealer:
        remaining_time = max(0, dealer_cooldown['duration'] - (current_time - dealer_cooldown['last_used']))
        text = f"Cooldown : {remaining_time:.1f} s"
        text_render = font.game_font.render(text, True, (255, 255, 255))
        screen.blit(text_render, (10, 110))
    if p.tanker:
        remaining_time = max(0, tanker_cooldown['duration'] - (current_time - tanker_cooldown['last_used']))
        text = f"Cooldown : {remaining_time:.1f} s"
        text_render = font.game_font.render(text, True, (255, 255, 255))
        screen.blit(text_render, (10, 110))
    if p.healer:
        remaining_time = max(0, healer_cooldown['duration'] - (current_time - healer_cooldown['last_used']))
        text = f"Cooldown : {remaining_time:.1f} s"
        text_render = font.game_font.render(text, True, (255, 255, 255))
        screen.blit(text_render, (10, 110))
    if p.thief:
        text = f"남은 갯수 : {thiefcount}"
        text_render = font.game_font.render(text, True, (255, 255, 255))
        screen.blit(text_render, (10, 110))
    # 스킬아이콘 그리기
    if p.thief and thiefcount == 0:
        remaining_time = 999
    if p.prist and p.revive == 0:
        remaining_time = 999
    if remaining_time == 0:
        screen.blit(skillicon, (20, 40))
    else:
        screen.blit(skillicon_cd, (20, 40))
    
    # 소지자금
    money_text = font.game_font.render(f"Money : {p.money}", True, (255, 255, 255))
    screen.blit(money_text, (screen_width - 180, screen_height - 40))
    screen.blit(gfx.money, (screen_width - 215, screen_height - 40))
    # 스테이지
    stage_text = font.game_font.render(f"Stage : {p.stage}", True, (255, 255, 255))
    screen.blit(stage_text, (screen_width/2-50, screen_height-540))  # 화면 우하단에 표시할 위치 설정
    # 악마방확률
    devil_text = font.game_font.render(f"Chance : {p.devilper}%", True, (255, 255, 255))
    screen.blit(devil_text, (10, 130))  # 화면 우하단에 표시할 위치 설정
    # 미니맵
    mini_map_width = len(mapdata[0]) * mini_map_cell_size
    mini_map_height = len(mapdata) * mini_map_cell_size
    if room_type != 7:
        pygame.draw.rect(screen, (255, 255, 255), (mini_map_x - 2, mini_map_y - 2, mini_map_width + 4, mini_map_height + 4), 2)
    for y in range(len(mapdata)):
        for x in range(len(mapdata[0])):
            room_type_mini = mapdata[y][x]
            if room_type_mini == 1:
                room_color = (255, 255, 255)  # 일반 방
            elif room_type_mini == 2:
                room_color = (255, 0, 0)      # 보스방
            elif room_type_mini == 3:
                room_color = (0, 255, 0)      # 상점 방
            elif room_type_mini == 4:
                room_color = (255, 215, 0)    # 황금 방
            else:
                room_color = (0, 0, 0)        # 빈 방 또는 기타
            if room_type != 7:
                pygame.draw.rect(screen, room_color, (mini_map_x + x * mini_map_cell_size, mini_map_y + y * mini_map_cell_size, mini_map_cell_size, mini_map_cell_size))
    if mapdata[player_y][player_x] != 7:
        pygame.draw.rect(screen, (0, 0, 255), (mini_map_x + player_x * mini_map_cell_size, mini_map_y + player_y * mini_map_cell_size, mini_map_cell_size, mini_map_cell_size))
    # 그리드
    #for y in range(grid_start_y, grid_end_y + 1, grid_step_y):
        #pygame.draw.line(screen, (255, 255, 255), (grid_start_x, y), (grid_end_x, y), 1)
    #for x in range(grid_start_x, grid_end_x + 1, grid_step_x):
        #pygame.draw.line(screen, (255, 255, 255), (x, grid_start_y), (x, grid_end_y), 1)
    # 무적시간
    draw_invincibility_text()       
    # 클리어
    if p.clear:
        screen.blit(gfx.gameclear, (0,0))
        current_sound.stop()
        current_sound = sfx.clearsound
        current_sound.play(-1)
        #pygame.time.delay(2000)
        #running = False
    # 게임오버
    if p.character_health <= 0 and not p.clear and p.revive == 0:
        current_sound.stop()
        current_sound = sfx.endsound
        screen.blit(gfx.gameover, (0,0))
        current_sound.play(-1)
        #pygame.time.delay(2000)
        #running = False
    pygame.display.update()
   

pygame.quit()

# 전역변수 관리
character_health = 100 # 체력
basedamge = 3.5 # 초기뎀
itemdamage = 0 # 아이템 데미지
extradamage = 0 # 추가뎀
realdamage = 3.5 # 최종뎀
damagemultiple = 1 # 데미지배수
shotdelay = 1330 # 최종공속
totaldelay = 10 # 공격속도
itemdelay = 0 # 템공속
delaylimit = 5 # 공속제한
delaymultiple = 1 # 공속배수
shotspeed = 0.5 # 탄속
shotspeedmultiple = 1 # 탄속배수
invincibility_time = 1 # 무적시간
invtimemultiple = 1 # 무적시간배수
invtimeitem = 1 # 무적시간아이템
skilcooltime = 1 # 스킬쿨배수
speed = 1 # 이속배수
collision_distance = 10 # 넉백거리
collision_distance_bullet = 30 # 총알넉백거리
itemprice = 1 # 상점가격배수
money = 0 # 돈
revive = 0
devilper = 100
devilroom = False
##################################
# 적 관련 변수
monsterhp = 1 # 체력배수
monsterdamage = 1 #공격력배수
obstacledamage = 1 #장애물공격력배수
monstershotdelay = 1000 # 공속
monstershotspeed = 0.2 # 탄속
monsterspeed = 1 # 이속 배수
monstermoney = 1 # 돈 배수
###################
dealer = False # 딜러판별
healer = False # 힐러판별
tanker = False # 탱커판별
prist = False
thief = False
monsternum = 0 # 방 안 몬스터 수
clear = False # 스테이지3 클리어 판별
stage = 1 # 현재스테이지
visited_rooms = [(7, 7)] # 방 저장
bossclear = False
timestop = False
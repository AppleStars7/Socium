import wall
import obstacle
import ghost
import bat
import random
import shopitem
import skeleton
from boss import Boss
from box import Box
import grid
import playerdata as p
import devilitem
from portal import Portal
monsternum = 0
class Roommake:
    def __init__(self):
        # 버그 방지용 초기값 세팅
        self.walls = []
        self.obstacles = []
        self.ghosts = []
        self.bats = []
        self.items = []
        self.shopitems = []
        self.skeletons = []
        self.boxes = []
        self.bosses = []
        self.devilitems = []
        self.portals = []
    # 방 디자인 설정
    def roomnumber(self, code, type):
        # 코드에 따른 일반방 디자인
        if code == 1 and type == 1:
            self.walls = [
                wall.Wall(grid.grid_pos_x(0), grid.grid_pos_y(0)),
                wall.Wall(grid.grid_pos_x(0), grid.grid_pos_y(2)),
                wall.Wall(grid.grid_pos_x(1), grid.grid_pos_y(2)),
                wall.Wall(grid.grid_pos_x(2), grid.grid_pos_y(2)),
                wall.Wall(grid.grid_pos_x(3), grid.grid_pos_y(2)),
                wall.Wall(grid.grid_pos_x(4), grid.grid_pos_y(2)),
                wall.Wall(grid.grid_pos_x(8), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(8), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(9), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(10), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(11), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(12), grid.grid_pos_y(4)),
                wall.Wall(grid.grid_pos_x(12), grid.grid_pos_y(6))
                ]
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.shopitems = []
            self.skeletons = [
                skeleton.Skeleton(grid.grid_pos_x(0), grid.grid_pos_y(1)),
                skeleton.Skeleton(grid.grid_pos_x(12), grid.grid_pos_y(5))
                ]
            self.boxes = []
            self.bosses = []
            self.portals = []
            self.devilitems = []
        elif code == 2 and type == 1:
            self.walls = [
                wall.Wall(grid.grid_pos_x(1), grid.grid_pos_y(1)),
                wall.Wall(grid.grid_pos_x(3), grid.grid_pos_y(1)),
                wall.Wall(grid.grid_pos_x(9), grid.grid_pos_y(1)),
                wall.Wall(grid.grid_pos_x(11), grid.grid_pos_y(1)),
                wall.Wall(grid.grid_pos_x(2), grid.grid_pos_y(3)),
                wall.Wall(grid.grid_pos_x(4), grid.grid_pos_y(3)),
                wall.Wall(grid.grid_pos_x(6), grid.grid_pos_y(3)),
                wall.Wall(grid.grid_pos_x(8), grid.grid_pos_y(3)),
                wall.Wall(grid.grid_pos_x(10), grid.grid_pos_y(3)),
                wall.Wall(grid.grid_pos_x(1), grid.grid_pos_y(5)),
                wall.Wall(grid.grid_pos_x(3), grid.grid_pos_y(5)),
                wall.Wall(grid.grid_pos_x(9), grid.grid_pos_y(5)),
                wall.Wall(grid.grid_pos_x(11), grid.grid_pos_y(5))
                ]
            self.obstacles = []
            self.ghosts = []
            self.bats = [
                bat.Bat(grid.grid_pos_x(2), grid.grid_pos_y(2)),
                bat.Bat(grid.grid_pos_x(4), grid.grid_pos_y(2)),
                bat.Bat(grid.grid_pos_x(3), grid.grid_pos_y(3)),
                bat.Bat(grid.grid_pos_x(8), grid.grid_pos_y(4)),
                bat.Bat(grid.grid_pos_x(9), grid.grid_pos_y(3)),
                bat.Bat(grid.grid_pos_x(10), grid.grid_pos_y(4))
                ]
            self.items = []
            self.shopitems = []
            self.skeletons = [
                skeleton.Skeleton(grid.grid_pos_x(3), grid.grid_pos_y(2)),
                skeleton.Skeleton(grid.grid_pos_x(9), grid.grid_pos_y(4))
                ]
            self.boxes = []
            self.bosses = []
            self.devilitems = []
            self.portals = []
        elif code == 3 and type == 1:
            self.walls = [
                wall.Wall(grid.grid_pos_x(6), grid.grid_pos_y(3))
                ]
            self.obstacles = [
                obstacle.Obstacle(grid.grid_pos_x(5), grid.grid_pos_y(3)),
                obstacle.Obstacle(grid.grid_pos_x(7), grid.grid_pos_y(3)),
                obstacle.Obstacle(grid.grid_pos_x(6), grid.grid_pos_y(4)),
                obstacle.Obstacle(grid.grid_pos_x(6), grid.grid_pos_y(2))
            ]
            self.ghosts = []
            self.bats = [
                bat.Bat(grid.grid_pos_x(0), grid.grid_pos_y(0)),
                bat.Bat(grid.grid_pos_x(0), grid.grid_pos_y(12)),
                bat.Bat(grid.grid_pos_x(12), grid.grid_pos_y(6)),
                bat.Bat(grid.grid_pos_x(12), grid.grid_pos_y(0)),
                bat.Bat(grid.grid_pos_x(5), grid.grid_pos_y(2)),
                bat.Bat(grid.grid_pos_x(7), grid.grid_pos_y(2)),
                bat.Bat(grid.grid_pos_x(5), grid.grid_pos_y(4)),
                bat.Bat(grid.grid_pos_x(7), grid.grid_pos_y(4))
                ]
            self.items = []
            self.shopitems = []
            self.skeletons = []
            self.boxes = []
            self.bosses = []
            self.portals = []
            self.devilitems = []
        elif code == 4 and type == 1:
            self.walls = []
            self.obstacles = [
                obstacle.Obstacle(grid.grid_pos_x(1), grid.grid_pos_y(1)),
                obstacle.Obstacle(grid.grid_pos_x(1), grid.grid_pos_y(5)),
                obstacle.Obstacle(grid.grid_pos_x(3), grid.grid_pos_y(2)),
                obstacle.Obstacle(grid.grid_pos_x(3), grid.grid_pos_y(4)),
                obstacle.Obstacle(grid.grid_pos_x(5), grid.grid_pos_y(3)),
                obstacle.Obstacle(grid.grid_pos_x(7), grid.grid_pos_y(3)),
                obstacle.Obstacle(grid.grid_pos_x(9), grid.grid_pos_y(2)),
                obstacle.Obstacle(grid.grid_pos_x(9), grid.grid_pos_y(4)),
                obstacle.Obstacle(grid.grid_pos_x(11), grid.grid_pos_y(1)),
                obstacle.Obstacle(grid.grid_pos_x(11), grid.grid_pos_y(5))
            ]
            self.ghosts = [
                ghost.Ghost(grid.grid_pos_x(1), grid.grid_pos_y(3)),
                ghost.Ghost(grid.grid_pos_x(3), grid.grid_pos_y(3)),
                ghost.Ghost(grid.grid_pos_x(6), grid.grid_pos_y(3)),
                ghost.Ghost(grid.grid_pos_x(8), grid.grid_pos_y(3)),
                ghost.Ghost(grid.grid_pos_x(10), grid.grid_pos_y(3))
                ]
            self.bats = []
            self.items = []
            self.shopitems = []
            self.skeletons = []
            self.boxes = []
            self.bosses = []
            self.portals = []
            self.devilitems = []
        elif code == 5 and type == 1:
            self.walls = []
            self.obstacles = []
            self.ghosts = [
                ghost.Ghost(grid.grid_pos_x(5), grid.grid_pos_y(2)),
                ghost.Ghost(grid.grid_pos_x(7), grid.grid_pos_y(2)),
                ghost.Ghost(grid.grid_pos_x(5), grid.grid_pos_y(4)),
                ghost.Ghost(grid.grid_pos_x(7), grid.grid_pos_y(4))
                ]
            self.bats = [
                bat.Bat(grid.grid_pos_x(6), grid.grid_pos_y(2)),
                bat.Bat(grid.grid_pos_x(5), grid.grid_pos_y(3)),
                bat.Bat(grid.grid_pos_x(7), grid.grid_pos_y(3)),
                bat.Bat(grid.grid_pos_x(8), grid.grid_pos_y(4))
            ]
            self.items = []
            self.shopitems = []
            self.skeletons = [
                skeleton.Skeleton(grid.grid_pos_x(6), grid.grid_pos_y(3))
            ]
            self.boxes = []
            self.bosses = []
            self.devilitems = []
            self.portals = []
        # 보스방
        elif type == 2:
            self.bosses = [
                Boss(grid.grid_pos_x(6)-131, grid.grid_pos_y(1)-119)
                ]
            self.walls = []
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.shopitems = []
            self.skeletons = []
            self.boxes = []
            self.devilitems = []
            self.portals = []
        # 상점방
        elif type == 3:
            self.shopitems = [
                shopitem.Shopitem(grid.grid_pos_x(6), grid.grid_pos_y(3), random.randint(1, 7)),
                shopitem.Shopitem(grid.grid_pos_x(4), grid.grid_pos_y(3), random.randint(1, 7))
                ]
            self.walls = []
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.skeletons = []
            self.boxes = []
            self.bosses = []
            self.devilitems = []
            self.portals = []
        # 보물방
        elif type == 4:
            self.boxes = [
                Box(grid.grid_pos_x(6), grid.grid_pos_y(3), random.randint(1, 7)),
                Box(grid.grid_pos_x(4), grid.grid_pos_y(3), random.randint(1, 7))
                ]
            self.walls = []
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.shopitems = []
            self.skeletons = []
            self.bosses = []
            self.portals = []
            self.devilitems = []
        elif type == 7: #악마방
            self.devilitems = [
                devilitem.Devilitem(grid.grid_pos_x(6), grid.grid_pos_y(3), random.randint(1, 7)),
                devilitem.Devilitem(grid.grid_pos_x(4), grid.grid_pos_y(3), random.randint(1, 7)),
                devilitem.Devilitem(grid.grid_pos_x(8), grid.grid_pos_y(3), random.randint(1, 7))
                ]
            self.walls = []
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.skeletons = []
            self.boxes = []
            self.bosses = []
            self.shopitems = []
            self.portals = []
        else:
            self.walls = []
            self.obstacles = []
            self.ghosts = []
            self.bats = []
            self.items = []
            self.shopitems = []
            self.skeletons = []
            self.boxes = []
            self.bosses = []
    # 방 안 구성 그리기
    def draw(self, character_x_pos, character_y_pos,dt):
        for wall in self.walls:
            wall.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        for box in self.boxes:
            box.draw()
        for shopitem in self.shopitems:
            shopitem.draw()
        for item in self.items:
            item.draw()
        for devilitem in self.devilitems:
            devilitem.draw()
        for boss in self.bosses:
            boss.update(character_x_pos, character_y_pos, dt)
            boss.draw()
            if boss.is_dead():
                self.bosses.remove(boss)
                devilmake = random.randint(1, 100)
                if devilmake <= p.devilper:
                    p.devilroom = True
                p.money += 50 * p.monstermoney
                if p.stage == 3:
                    p.clear = True
                self.portals.append(Portal(grid.grid_pos_x(6), grid.grid_pos_y(3)))
                p.bossclear = True
        for ghost in self.ghosts:
            ghost.draw()
            ghost.update()
            if ghost.is_dead():
                self.ghosts.remove(ghost)
                p.money += 10 * p.monstermoney
        for skeleton in self.skeletons:
            skeleton.update(character_x_pos, character_y_pos, dt)
            skeleton.draw()
            if skeleton.is_dead():
                self.skeletons.remove(skeleton)
                p.money += 10 * p.monstermoney
        for bat in self.bats:
            bat.move_bat(character_x_pos,character_y_pos,dt)
            bat.draw()
            if bat.is_dead():
                self.bats.remove(bat)
                p.money += 20 * p.monstermoney
        for portal in self.portals:
            portal.draw()
    # 상자용 아이템생성 함수
    def item_genetate(self):
        for box in self.boxes:
            item = box.item_generate()
            if item != 0:
                self.items.append(item)
    # 보스용 몬스터생성 함수
    def bat_generate(self):
        for boss in self.bosses:
            bat = boss.bat_generate()
            self.bats.append(bat)
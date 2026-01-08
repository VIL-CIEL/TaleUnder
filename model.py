import pygame
# Enemy DATABASE

class Kopa:

    def __init__(self):
        self.sheet = pygame.image.load("sprites/enemy/Kopa_sheet.png").convert_alpha()
        self.img = pygame.image.load("sprites/enemy/Kopa_model.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
        self.index = [0,0]
        self.info = {
            "name" : "Kopa",
            "desc" : "* Kopa - Royal Guard\nShe will not let you pass",
            "hp" : 100,
            "at" : 10,
            "df" : 10,
            "xp_reward" : 50,
            "gold_reward" : 200,
            "KR" : False
        }
        self.act = {
            0 : "check",
            1 : "compliment",
            2 : "insult",
            3 : "call help"
        }
        self.act_txt = {
            "check" : "* 10 ATK 10 DEF\n* She's looking at you with a hatefull face",
            "compliment" : "* She don't seems to care",
            "insult" : "* She don't seems to care of your words",
            "call help" : "* But nobody came"
        }
        self.mercy = {
            0 : "Spare",
        }
        self.mercy_txt = {
            "Spare" : "* Your Sparing Kopa, Nothing Happend"
        }
        self.Attack_bullet =pygame.image.load("sprites/ui/att1.png").convert_alpha()
        self.Spear = pygame.image.load("sprites/ui/att3.png").convert_alpha()
        self.Spear = pygame.transform.scale_by(self.Spear,4)


    def update(self):
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
    
    def anim_simple(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        self.index[0] += 0.1
        if self.index[0] >= 6:
            self.index[0] = 0

        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,y*0,x,y))

        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y*1,x,y))

        elif self.index[0] < 3:
            img.blit(self.sheet,(0,0),(0,y*2,x,y))

        elif self.index[0] < 4:
            img.blit(self.sheet,(0,0),(0,y*3,x,y))

        elif self.index[0] < 5:
            img.blit(self.sheet,(0,0),(0,y*4,x,y))

        elif self.index[0] < 6:
            img.blit(self.sheet,(0,0),(0,y*5,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect
    
    def anim_eyes(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        self.index[0] += 0.02
        if self.index[0] >= 2:
            self.index[0] = 0

        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,y*7,x,y))

        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y*8,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect

    def looking(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        img.blit(self.sheet,(0,0),(0,y*6,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect
    
    def looking_at_yu(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        img.blit(self.sheet,(0,0),(0,y*9,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect

    def degat(self, att,player,rect,vitesse,sens,rect1,type,hurt,taille=(0,0)):
        rect1[0]=att[0]
        rect1[1]=att[1]

        if rect1.colliderect(player.rect) and player.info["current_hp"] >= self.info["at"]//2:
            if type == 'b':
                player.info["current_hp"]-= int(self.info["at"]*0.2)
            if type == 's':
                player.info["current_hp"]-= int(self.info["at"]*0.5)
            hurt.play()
            return False
        
        if type == "b":
            if sens == 'r' and att[0] > rect.right-10-vitesse:
                return False
            if sens == 'l'and att[0] < rect.left-vitesse:
                return False
            if sens == 't' and att[1] < rect.top-vitesse :
                return False
            if sens == 'd'and att[1] > rect.bottom-15-vitesse :
                return False
            
        if type == "s":
            w,h = taille
            if sens == 'r' and att[0] > w:
                return False
            if sens == 'l'and att[0] < -200:
                return False
            if sens == 't' and att[1] < -200 :
                return False
            if sens == 'd'and att[1] > h :
                return False


        return True
                
def attack1(att,vitesse,sens):
    x,y=att
    if sens == 't':
        att[1]-=vitesse
    if sens == 'd':
        att[1]+=vitesse
    if sens == 'r':
        att[0]+=vitesse
    if sens == 'l':
        att[0]-=vitesse
    (x,y) = att
    return x,y    


# ITEM DATABASE
Bandage = {
    "state" : "armor",
    "name" : "Bandage",
    "desc" : "It has already been used several times.",
    "hp_give" : 10,
    "price" : "Free"
}

Monster_Candy = {
    "state" : "consumable",
    "name" : "Monster Candy",
    "desc" : "Has a distinct, non-licorice flavor.",
    "hp_give" : 10,
    "price" : "Free"
}

Spider_Donut = {
    "state" : "consumable",
    "name" : "Spider Donut",
    "desc" : "A donut made with Spider Cider in the batter.",
    "hp_give" : 12,
    "price" : [7,9999]
}

Spider_Cider = {
    "state" : "consumable",
    "name" : "Spider Cider",
    "desc" : "Made with whole spiders, not just the juice.",
    "hp_give" : 10,
    "price" : [18,9999]
}

Butterscotch_Pie = {
    "state" : "consumable",
    "name" : "Butterscotch Pie",
    "desc" : "Butterscotch-cinnamon pie, one slice. ",
    "hp_give" : "ALL",
    "price" : "Free"
}

Snail_Pie = {
    "state" : "consumable",
    "name" : "Snail Pie",
    "desc" : "Heals Some HP. An acquired taste.",
    "hp_give" : "All-1",
    "price" : "Free"
}

Snowman_Piece = {
    "state" : "consumable",
    "name" : "Snowman Piece",
    "desc" : "Please take this to the ends of the earth. ",
    "hp_give" : 45,
    "price" : "Free"
}

Knife = {
    "state" : "useable",
    "name" : "Knife",
    "desc" : "A Knife",
    "hp_give" : 0,
    "price" : [15,25,"Free",12]
}

Name = {
    "state" : "consumable",
    "name" : "Name",
    "desc" : "Desc",
    "hp_give" : 0,
    "price" : [7,9999]
}

#PLAYER INFO AND OTHER SYSTEM
def sort_inv():
    """
    Sort the player inventory
    """
    player_inventory.sort(key=lambda x:x["name"])

def take_dmg(enemy_hp,enemy_df,player_dmg):
    """
    Return the damage taken by the enemy
    """
    if enemy_hp==0:
        return (0,0)
    
    elif enemy_df == 0 and player_dmg > enemy_hp*0.8:
        return (0,enemy_hp)
    
    elif player_dmg == 0:
        player_dmg = enemy_df + 1

    elif player_dmg < enemy_df:
        player_dmg = enemy_df + 1

    damage = player_dmg - enemy_df

    if damage == 0:
        damage = 1
    if damage < 0:
        damage = -damage

    enemy_hp -= damage

    if enemy_hp in [1,2,3,4,5] and player_dmg < enemy_df:
        return (0,damage+enemy_hp)
    
    elif enemy_hp <= 0:
        return (0,damage)
    
    return enemy_hp, damage

#Health System
hp_system = {}
base = 20
for i in range(1,21):
    hp_system[i] = base
    base += 4
hp_system[20] = 99
#Experience System
xp_system = {}
xp_system[1] = 10
xp_system[2] = 20
xp_system[3] = 40
xp_system[4] = 50
xp_system[5] = 80
xp_system[6] = 100
xp_system[7] = 200
xp_system[8] = 300
xp_system[9] = 400
xp_system[10] = 500
xp_system[11] = 800
xp_system[12] = 1000
xp_system[13] = 1500
xp_system[14] = 2000
xp_system[15] = 3000
xp_system[16] = 5000
xp_system[17] = 10000
xp_system[18] = 25000
xp_system[19] = 49999
#Attack System
at_system = {}
base = 10
for i in range(1,21):
    at_system[i] = base
    base += 2
#Defence System
df_system = {}
base = 10
for i in range(1,21):
    if i < 5:
        df_system[i] = base
    elif i < 9:
        df_system[i] = base + 1
    elif i < 12:
        df_system[i] = base + 2
    elif i < 17:
        df_system[i] = base + 3
    else:
        df_system[i] = base + 4
#Player Inventory
player_inventory = [Bandage,Bandage,Snail_Pie]
sort_inv()

def recover_hp(player,hp):
    if type(hp) == str:
        if hp == 'ALL':
            player.info["current_hp"] = player.info["hp"]
        if hp == 'All-1':
            player.info["current_hp"] = player.info["hp"] -1
    else:

        temp = player.info["current_hp"] + hp
        if temp >= player.info["hp"]:
            player.info["current_hp"] = player.info["hp"]
        else:
            player.info["current_hp"] = temp


red_soul = pygame.image.load("sprites/Souls/new_soul.png").convert_alpha()
blue_soul = pygame.image.load("sprites/Souls/blue_soul.png").convert_alpha()

class Player:

    def __init__(self,info,inventory):
        self.img = pygame.image.load("sprites/Souls/new_soul.png").convert_alpha()
        self.size = self.img.get_size()
        self.rect = self.img.get_rect(x=0,y=0)
        self.info = info
        self.speed = 4.5
        self.velocity = [0,0]
        self.inv = inventory
        
    def __str__(self):
         return f"({self.img}\n{self.rect}\n{self.info})"
    
    def move(self,surface):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        self.rect.clamp_ip(surface)
        
    def swap_img(self,flags):
        if flags == 'red':
            self.img = red_soul
        if flags == 'blue':
            self.img = blue_soul

    def update_stats(self):
        if self.info["level"]<20 and xp_system[self.info["level"]] <= self.info["xp"]:
            ecart = self.info["xp"] - xp_system[self.info["level"]]
            self.info["xp"] = ecart
            if self.info["level"]<20:
                self.info["level"] += 1
                self.info["hp"] = hp_system[self.info["level"]]
                self.info["current_hp"] = self.info["hp"]

        self.info["hp"] = hp_system[self.info["level"]]
        self.info["at"] = at_system[self.info["level"]]
        self.info["df"] = df_system[self.info["level"]]

### OVERWORLD ###

class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("sprites/character/p1.1.png")
        self.speed = 10
        self.velocity = [0,0]
        self.rect = self.img.get_rect(x=0,y=0)
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.frame = 0
        self.sens = "bas"

    def get_position(self):
        return (self.x, self.y)
    
    def get_image(self):
        return self.img

    def set_position(self, pos):
        self.x,self.y = pos
        self.rect.update(self.x,self.y,60,60)

    def deplacer(self):
        self.rect.x += self.velocity[0] * self.speed
        self.rect.y += self.velocity[1] * self.speed

def anim_perso(perso,frame):
    perso.frame +=0.2
    if perso.frame >= 5:
        perso.frame = 0
    if perso.velocity[0] == 0 and perso.velocity[1] == -1:
        perso.sens = "haut"
    if perso.velocity[0] == 0 and perso.velocity[1] == 1:
        perso.sens = "bas"
    if perso.velocity[0] == -1 and perso.velocity[1] == 0:
        perso.sens = "gauche"
    if perso.velocity[0] == 1 and perso.velocity[1] == 0:
        perso.sens = "droite"
    if perso.frame >= 2.5:
        perso.img = frame[perso.sens][2]
    else:
        perso.img = frame[perso.sens][1]
    if perso.velocity[0] == 0 and perso.velocity[1] == 0:
        perso.img = frame[perso.sens][0]
    perso.img = pygame.transform.scale(perso.img, (64, 64))

        
class Map:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("sprites/maps/Fullmap.png")
        self.img = pygame.transform.scale(self.img, (5812, 3070))
        self.rect  = self.img.get_rect(x=0,y=0)
    
    def set_position(self, pos):
        self.x, self.y = pos

class Camera:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 824

    def apply(self, entity_or_surface):
        if hasattr(entity_or_surface, 'rect'):
            return entity_or_surface.rect.move(self.camera.topleft)
        else:
            return entity_or_surface.get_rect(topleft=self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.SCREEN_WIDTH / 2)
        y = -target.rect.y + int(self.SCREEN_HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.SCREEN_WIDTH), x)-50
        y = max(-(self.height - self.SCREEN_HEIGHT), y)-50

        self.camera = pygame.Rect(x, y, self.width, self.height)

class Obstacle:

    def __init__(self,rect):
        self.rect = rect
    
    def collisions(self,perso):
        if self.rect.colliderect(perso.rect):
            if perso.velocity[0] == 1 and perso.velocity[1] == 0:
                perso.rect.right = self.rect.left
            elif perso.velocity[0] == -1 and perso.velocity[1] == 0:
                perso.rect.left = self.rect.right
            if perso.velocity[1] == -1 and perso.velocity[0] == 0:
                perso.rect.top = self.rect.bottom
            elif perso.velocity[1] == 1 and perso.velocity[0] == 0:
                perso.rect.bottom = self.rect.top

class Debutcombat:
    def __init__(self,rect):
        self.rect = rect
        self.pos = (0,0)
    def collisions(self,perso):
        self.x = perso.x
        self.y = perso.y
        if self.rect.colliderect(perso.rect):
            return True
        return False

col11 = Obstacle(pygame.Rect(2470,1875,3340,10))
col12 = Obstacle(pygame.Rect(2510,2500,3300,10))
col13 = Obstacle(pygame.Rect(5802,1875,10,585))
col14 = Obstacle(pygame.Rect(5490,1885,65,50))
col15 = Obstacle(pygame.Rect(5555,1885,65,100))
col16 = Obstacle(pygame.Rect(5620,1885,80,175))
col17 = Obstacle(pygame.Rect(5700,1885,90,250))
col18 = Obstacle(pygame.Rect(2510,2500,10,55))
col19 = Obstacle(pygame.Rect(2020,2555,490,10))
col20 = Obstacle(pygame.Rect(2020,2555,10,300))
col21 = Obstacle(pygame.Rect(1570,2845,450,10))
col22 = Obstacle(pygame.Rect(1570,2845,10,150))
col23 = Obstacle(pygame.Rect(1495,2995,75,10))
col24 = Obstacle(pygame.Rect(1495,2905,10,90))
col25 = Obstacle(pygame.Rect(0,2905,1495,10))
col26 = Obstacle(pygame.Rect(0,2155,720,10))
col27 = Obstacle(pygame.Rect(720,2095,10,60))
col28 = Obstacle(pygame.Rect(720,2095,600,10))
col29 = Obstacle(pygame.Rect(1320,2095,10,60))
col30 = Obstacle(pygame.Rect(1320,2155,600,10))
col31 = Obstacle(pygame.Rect(1920,2035,10,120))
col32 = Obstacle(pygame.Rect(1920,2035,70,10))
col33 = Obstacle(pygame.Rect(1990,1975,10,60))
col34 = Obstacle(pygame.Rect(1990,1975,60,10))
col35 = Obstacle(pygame.Rect(2050,1905,10,70))
col36 = Obstacle(pygame.Rect(2050,1905,150,10)) 
col37 = Obstacle(pygame.Rect(2200,1630,10,275)) 
col38 = Obstacle(pygame.Rect(2070,1630,130,10)) 
col39 = Obstacle(pygame.Rect(2070,1565,10,65)) 
col40 = Obstacle(pygame.Rect(800,1565,1270,10))
col41 = Obstacle(pygame.Rect(800,1505,10,60))
col42 = Obstacle(pygame.Rect(740,1505,60,10))
col43 = Obstacle(pygame.Rect(740,705,10,800))
col44 = Obstacle(pygame.Rect(740,705,110,10))
col45 = Obstacle(pygame.Rect(850,635,10,70))
col46 = Obstacle(pygame.Rect(850,635,670,10))
col47 = Obstacle(pygame.Rect(1520,635,10,65))
col48 = Obstacle(pygame.Rect(1520,700,200,10))
col49 = Obstacle(pygame.Rect(1720,700,10,65))
col50 = Obstacle(pygame.Rect(1720,765,180,10))
col51 = Obstacle(pygame.Rect(1900,765,10,130))
col52 = Obstacle(pygame.Rect(1900,895,450,10))
col53 = Obstacle(pygame.Rect(2350,895,10,130))
col54 = Obstacle(pygame.Rect(2350,1025,120,10))
col55 = Obstacle(pygame.Rect(2470,1025,10,850))
col56 = Obstacle(pygame.Rect(5742,2135,10,365))
col57 = Obstacle(pygame.Rect(700,2155,10,750))

map_collisions = [col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,
                  col31,col32,col33,col34,col35,col36,col37,col38,col39,col40,col41,col42,col43,col44,col45,col46,col47,col48,col49,
                  col50,col51,col52,col53,col54,col55,col56,col57]

frame = {"gauche" :[pygame.image.load("sprites/character/p4.1.png"),pygame.image.load("sprites/character/p4.2.png"),pygame.image.load("sprites/character/p4.3.png")],
          "droite" : [pygame.image.load("sprites/character/p3.1.png"),pygame.image.load("sprites/character/p3.2.png"),pygame.image.load("sprites/character/p3.3.png")],
            "haut" : [pygame.image.load("sprites/character/p2.1.png"),pygame.image.load("sprites/character/p2.2.png"),pygame.image.load("sprites/character/p2.3.png")],
              "bas" : [pygame.image.load("sprites/character/p1.1.png"),pygame.image.load("sprites/character/p1.2.png"),pygame.image.load("sprites/character/p1.3.png")]}
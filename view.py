import pygame
from controller import blue_lock

fontsize = 30
font = pygame.font.Font("8bitoperator_jve.ttf",fontsize)

def display_StartScreen(screen):
    x,y = screen.get_size()
    logo = pygame.image.load("sprites/Cover.png").convert_alpha()
    logorect = logo.get_rect(center=(x//2,y//2))
    screen.blit(logo,logorect)
    xl,yl = logorect.bottomleft
    display(screen,"Press z to begin your journey",font,(xl+105,yl+20), "white",500)

def display_EndScreen(screen):
    x,y = screen.get_size()
    display(screen,"Here The Beta Take An End, Thanks for playing !",font,(x*0.3,y//2), "white")

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
txt = ''
def name_pad(screen,spec,cursor,select):
    global txt
    letter = ''
    w,h = spec

    font = pygame.font.Font("8bitoperator_jve.ttf",40)
    display(screen,"Name the fallen human.",font,(w*0.37,h*0.2), "white",500)
    for i in range(len(Alphabet)):
        if i % 7 == 0:
            w,h = spec
            w,h = w*0.27,(h*0.4) +100*(i//7)
        if txt == '':
            if i == cursor:
                display_letter(screen,chr(ord(Alphabet[i])-32),'blue',(w,h))
                letter = chr(ord(Alphabet[i])-32)
            else:
                display_letter(screen,chr(ord(Alphabet[i])-32),'white',(w,h))
        else:
            if i == cursor:
                display_letter(screen,Alphabet[i],'blue',(w,h))
                letter = Alphabet[i]
            else:
                display_letter(screen,Alphabet[i],'white',(w,h))
        w += 100

    w,h = spec
    if select:
        if cursor == 'Erase':
            txt = txt[:-1]
        elif type(cursor) == int:
            txt += letter

    display(screen,txt,font,(w*0.37,h*0.3), "white",500)
    return txt

def selection_name(screen,spec,txt,i):
    if txt == 'Gaster':
        return True
    w,h = spec
    font = pygame.font.Font("8bitoperator_jve.ttf",60)
    if i > 80:
        display(screen,"However, YOU CAN'T CHOOSE YOUR NAME",font,(w*0.21,h*0.45), "white",500)
    else:
        display(screen,f"Your Name is {txt}",font,(w*0.37,h*0.45), "white",500)

    return False

def draw_player(screen,player):
    screen.blit(player.img,player.rect)

font_namepad = pygame.font.Font("8bitoperator_jve.ttf",40)

def display_letter(screen,txt,color,pos):
    render = font_namepad.render(txt,True,color)
    rect = render.get_rect(topleft = pos)
    screen.blit(render,rect)

def display(surface,text,font,pos,color,limit=500):
    """
    Display Text on a Surface
    """
    line = ""
    x,y = pos
    size = font.__sizeof__()
    
    if len(text) > limit:
        for el in text:
            if len(line) > limit and el == " ":
                render = font.render(line,True,color)
                surface.blit(render,(x,y))
                y +=size* 1.1
                line = ""
            if el == "\n":
                render = font.render(line,True,color)
                surface.blit(render,(x,y))
                y +=size* 1.1
                line = ""
            else:
                line += el
    else:
        line = text

    render = font.render(line,True,color)
    rect = render.get_rect(topleft = (x,y))
    surface.blit(render,rect)
    return render, rect

def debug(screen,info):
    """
    Display Debug Text

    info - list - Tableau de variable à afficher sur l'ecran
    """
    display(screen,f"{info}",font,(0,0), "orange")

background1 = pygame.image.load("sprites/ui/battle_back/Background.png").convert_alpha()
background1 = pygame.transform.scale_by(background1,2.2)


def display_background(screen):
    backrect = background1.get_rect()
    x,y = screen.get_size()
    backrect.midbottom = (x*0.52,y*.6)
    screen.blit(background1,backrect)

def display_line(screen,box,nb_line):
    L,l = box.size
    larg = l//3
    line = pygame.Surface((L,2))
    line.fill("white")
    x,y = box.topleft
    y += larg
    for i in range(nb_line):
        screen.blit(line,(x,y))
        y+= larg

def display_side_line(screen,box):
    L,l = box.size
    long = 2*L//3
    line = pygame.Surface((2,l))
    line.fill("white")
    x,y = box.topleft
    x += long
    screen.blit(line,(x,y))
        

def boxfight(screen,longueur,largeur,coord,colors="black"):
    x,y = coord  
    boxsurf = pygame.Surface((longueur, largeur))
    boxsurf.fill(colors)
    pygame.draw.rect(boxsurf, "white", (0, 0, longueur,  largeur), 3)
    moving_space = pygame.Surface((longueur-6, largeur-6))
    box = moving_space.get_rect(center=(x,y))
    screen.blit(boxsurf,(x-longueur//2,y-largeur//2))
    return boxsurf,box

fight = pygame.image.load("sprites/Buttons/b_f.png").convert_alpha()
fight_s = pygame.image.load("sprites/Buttons/b_f_s.png").convert_alpha()
act = pygame.image.load("sprites/Buttons/b_a.png").convert_alpha()
act_s = pygame.image.load("sprites/Buttons/b_a_s.png").convert_alpha()
items = pygame.image.load("sprites/Buttons/b_i.png").convert_alpha()
items_s = pygame.image.load("sprites/Buttons/b_i_s.png").convert_alpha()
mercy = pygame.image.load("sprites/Buttons/b_m.png").convert_alpha()
mercy_s = pygame.image.load("sprites/Buttons/b_m_s.png").convert_alpha()


def buttons(screen,boxrect,selected=[0,0,0,0]):
    x,y = boxrect.midbottom
    l,L = boxrect.size
    x -= L*2
    y += 100
    larg,long = fight.get_size()
    if selected == [0,0,0,0]:
        screen.blit(fight,(x,y))
        x+=250
        screen.blit(act,(x,y))
        x+=250
        screen.blit(items,(x,y))
        x+=250
        screen.blit(mercy,(x,y))
    else:
        if selected[0]:
            screen.blit(fight_s,(x,y))
        else:
            screen.blit(fight,(x,y))
        x+=250
        if selected[1]:
            screen.blit(act_s,(x,y))
        else:
            screen.blit(act,(x,y))
        x +=250
        if selected[2]:
            screen.blit(items_s,(x,y))
        else:
            screen.blit(items,(x,y))
        x+=250
        if selected[3]:
            screen.blit(mercy_s,(x,y))
        else:
            screen.blit(mercy,(x,y))

def fight_elements(screen,player,boxrect,KR_mode=False):
    x,y = boxrect.midbottom
    font_gros = pygame.font.Font("8bitoperator_jve.ttf",50)

    #Health bar
    health = pygame.Surface((player.info["hp"]*2.5,50))
    health.fill("lightgrey")
    healthrect = screen.blit(health,(x-100,y+25))
    #Current Health Bar
    pv = pygame.Surface((player.info["current_hp"]*2.5,50))
    pv.fill("lightblue")
    pvrect = screen.blit(pv,healthrect.topleft)

    xh,yh = healthrect.topleft
    #Name + Level + HP
    display(screen,player.info["name"], font_gros,(xh-350,yh),"white")
    display(screen,f"LV {player.info['level']}", font_gros,(xh-200,yh),"white")
    display(screen,"HP",font,(xh-40,yh+9),"white")
    
    #KR + Life
    x,y = healthrect.topright
    if KR_mode:
         display(screen,"KR",font,(x+15,y+9),"white")
         display(screen,f"{player.info['current_hp']}/{player.info['hp']}", font_gros,(x+60,y-2),"white")
    else:
        display(screen,f"{player.info['current_hp']}/{player.info['hp']}",font_gros,(x+20,y-2),"white")

def display_enemy(screen,enemy,boxrect):
    sizex,sizey = enemy.size
    surf,rect = enemy.anim_simple(boxrect)
    rect.bottom = boxrect.top - 10
    rect.x -= 10
    screen.blit(surf,rect)

def display_enemy_frame(screen,enemy,boxrect,frame):
    sizex,sizey = enemy.size
    if frame == 'eyes':
        surf,rect = enemy.anim_eyes(boxrect)
    if frame == 'looking':
        surf,rect = enemy.looking(boxrect)
    if frame == 'look_yu':
        surf,rect = enemy.looking_at_yu(boxrect)
    rect.bottom = boxrect.top - 10
    rect.x -= 10
    screen.blit(surf,rect)

kris_model = pygame.image.load("sprites/enemy/Kris_model.png").convert_alpha()
kris_sheet = pygame.image.load("sprites/enemy/Kris_sheet.png").convert_alpha()
ind = 0

def display_kris(screen,boxrect):
    global ind
    x,y = kris_model.get_size()
    img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

    ind += 0.1
    if ind >= 6:
        ind = 0

    if ind < 1:
        img.blit(kris_sheet,(0,0),(0,y*0,x,y))

    elif ind < 2:
        img.blit(kris_sheet,(0,0),(0,y*1,x,y))

    elif ind < 3:
        img.blit(kris_sheet,(0,0),(0,y*2,x,y))

    elif ind < 4:
        img.blit(kris_sheet,(0,0),(0,y*3,x,y))

    elif ind < 5:
        img.blit(kris_sheet,(0,0),(0,y*4,x,y))

    elif ind < 6:
        img.blit(kris_sheet,(0,0),(0,y*5,x,y))

    img = pygame.transform.scale_by(img,6)

    x,y = boxrect.topleft
    rect = img.get_rect(center = (x+20,y-80))
    screen.blit(img,rect)

font35 = pygame.font.Font("8bitoperator_jve.ttf",35)

def display_info(screen,box,enemy):
    x,y = box.topleft
    display(screen,f"{enemy.info['desc']}\n- {enemy.info['hp']} HP -",font35,(x+30,y+20), "white",40)

kopa_face = pygame.image.load("sprites/enemy/Kopa_Face.png").convert_alpha()
kopa_face = pygame.transform.scale_by(kopa_face,5)
kopa_face_look = pygame.image.load("sprites/enemy/Kopa_Face_looking.png").convert_alpha()
kopa_face_look = pygame.transform.scale_by(kopa_face_look,5)
kopa_face_look_up = pygame.image.load("sprites/enemy/Kopa_Face_looking2.png").convert_alpha()
kopa_face_look_up = pygame.transform.scale_by(kopa_face_look_up,5)
kopa_face_look_yu = pygame.image.load("sprites/enemy/Kopa_Face_looking3.png").convert_alpha()
kopa_face_look_yu = pygame.transform.scale_by(kopa_face_look_yu,5)
kris_face = pygame.image.load("sprites/enemy/Kris_Face.png").convert_alpha()
kris_face = pygame.transform.scale_by(kris_face,8)

def Speaking(screen,box,txt,perso,type="n"):
    x,y = box.topleft
    if perso == 'Kopa':
        if type == "n":
            screen.blit(kopa_face,(x+30,y+25))
        if type == 'looking':
            screen.blit(kopa_face_look,(x+30,y+25))
        if type == 'look_yu':
            screen.blit(kopa_face_look_yu,(x+30,y+25))
        if type == 'eyes':
            screen.blit(kopa_face_look_up,(x+30,y+25))
        display(screen,txt,font_namepad,(x+160,y+70), "white",30)
    if perso == 'Kris':
        screen.blit(kris_face,(x+20,y+50))
        display(screen,txt,font_namepad,(x+190,y+70), "white",30)

selection_arrow = pygame.image.load("sprites/ui/arrows/arrows_2.png").convert_alpha()
selection_arrow = pygame.transform.scale_by(selection_arrow,3)
sa_rect = selection_arrow.get_rect()
index = 0
def display_arrow(screen,coord):
    global index
    sa_rect.center = coord
    screen.blit(selection_arrow,sa_rect)

arrow_up = pygame.image.load("sprites/ui/arrows/arrows_0.png").convert_alpha()
arrow_up = pygame.transform.scale_by(arrow_up,3)
arrow_down = pygame.image.load("sprites/ui/arrows/arrows_1.png").convert_alpha()
arrow_down = pygame.transform.scale_by(arrow_down,3)

def display_menu_arrows(screen,box,up,down):
    global i
    i = 0
    L,l = box.size
    x,y = box.topleft
    x += L*0.92
    if up:
        screen.blit(arrow_up,(x,y))
    if down:
        screen.blit(arrow_down,(x,y+l*0.82))

def display_fight(screen,box,player):
    x,y = box.topleft
    display(screen,"* Fight",font35,(x+75,y+20), "white")

def display_act(screen,box,enemy,elem):
    x,y = box.topleft
    i = 0
    y+= 20
    for el in enemy.act.values():
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el}",font35,(x+75,y), "white")
            y += 80
        if elem != 3:
            display_menu_arrows(screen,box,True,False)
        if elem != len(enemy.act):
            display_menu_arrows(screen,box,False,True)

def display_item(screen,box,player,elem):
    x,y = box.topleft
    i = 0
    y+=20
    for el in player.inv:
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el['name']}",font35,(x+75,y), "white")
            display(screen,f"+ {el['hp_give']} HP",font35,(x+550,y), "white")
            y += 80
        if elem != 3:
            display_menu_arrows(screen,box,True,False)
        if elem != len(player.inv):
            display_menu_arrows(screen,box,False,True)

def display_mercy(screen,box,enemy,elem):
    x,y = box.topleft
    i = 0
    y += 20
    for el in enemy.mercy.values():
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el}",font35,(x+75,y), "white")
            y += 80

glove_sheet = pygame.image.load("sprites/ui/Glove_Attack_spritesheet.png").convert_alpha()
glove_sheet = pygame.transform.scale_by(glove_sheet,2)
glove_tab = [0,0,0,0,0]
def display_glove(screen,enemy,nmb,i):
    xg,yg = 47*2,40*2
    img = pygame.Surface((xg,yg),pygame.SRCALPHA).convert_alpha()

    if i > 14 :
        img.blit(glove_sheet,(0,0),(0,yg*7,xg,yg))
    elif i > 12:
        img.blit(glove_sheet,(0,0),(0,yg*6,xg,yg))
    elif i > 10 :
        img.blit(glove_sheet,(0,0),(0,yg*5,xg,yg))
    elif i > 8 :
        img.blit(glove_sheet,(0,0),(0,yg*4,xg,yg))
    elif i > 6:
        img.blit(glove_sheet,(0,0),(0,yg*3,xg,yg))
    elif i > 4:
        img.blit(glove_sheet,(0,0),(0,yg*2,xg,yg))
    elif i > 2:
        img.blit(glove_sheet,(0,0),(0,yg,xg,yg))
    elif i > 0:
        img.blit(glove_sheet,(0,0),(0,0,xg,yg))
    i += 1

    x,y = enemy.rect.center
    if type(img) == pygame.Surface:
        if nmb == 1:
            screen.blit(img,(x-50,y))
        elif nmb == 2:
            screen.blit(img,(x,y-100))
        elif nmb == 3:
            screen.blit(img,(x-100,y-150))
        elif nmb == 4:
            screen.blit(img,(x-70,y+50))
        elif nmb == 5:
            screen.blit(img,(x-100,y-50))
    
    return i

def display_attack(screen,box):
    x,y = box.topleft
    display(screen,"5 x Press Z ! ",font35,(x+30,y+20), "white",40)

def display_attack_damage(screen,box,dmg):
    x,y = box.topleft
    display(screen,f"You dealt {dmg} damages !",font35,(x+30,y+20), "white",40)

def display_act_txt(screen,box,enemy,cursor):
    x,y = box.topleft
    display(screen,f"{enemy.act_txt[cursor]}",font35,(x+30,y+20), "white",40)

def display_item_txt(screen,box,player,cursor):
    x,y = box.topleft
    display(screen,f"You hate the {player.inv[cursor]['name']}, you recover {player.inv[cursor]['hp_give']} HP",font35,(x+30,y+20), "white",50)

def display_mercy_txt(screen,box,enemy,cursor):
    x,y = box.topleft
    display(screen,f"{enemy.mercy_txt[cursor]}",font35,(x+30,y+20), "white",40)

Attack_bullet = pygame.image.load("sprites/ui/att1.png").convert_alpha()

def enemy_attack(screen,type,coo,img=Attack_bullet):
    x,y=coo
    if type == "bullet":
        screen.blit(Attack_bullet,(x,y))
    if type == "spear":
        screen.blit(img,(x,y))
        
    
font35 = pygame.font.Font("8bitoperator_jve.ttf",35)

### OVERWORLD ### 

def draw_player_o(screen, perso, camera):
    screen.blit(perso.img, camera.apply(perso))

def draw(screen,map):
    screen.blit(map.img,(0,0))

def draw_map(screen, map_image, camera):
    screen.blit(map_image, camera.camera.topleft)

def draw_item(screen, item):
    screen.blit(item.img,item.rect)

def display_text_item_o(screen,item):
    w,h = screen.get_size()
    display(screen,f"You picked up the {item["name"]}",font35,(w-500,h-50), "white")
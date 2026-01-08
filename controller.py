import pygame
blue_lock = True

def window_quit():
    for event in pygame.event.get():
        # Window Close
        if event.type == pygame.QUIT :
            return True
    return False

def waiting_room():
    for event in pygame.event.get(eventtype=[pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT :
            return False,True
        if event.key == pygame.K_z:
            return False,False
    return True,False

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stock_ancient = ""
def name_ev(cursor,enter,move):
    move.set_volume(0.8)
    global stock_ancient
    if cursor == 'Erase':
        cursor = stock_ancient
    for event in pygame.event.get(eventtype=[pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT :
            return True, False, cursor,False,enter
        
        if event.key == pygame.K_LEFT and cursor -1 >= 0:
            cursor -= 1
            move.play()
        elif event.key == pygame.K_RIGHT and cursor +1 < len(Alphabet):
            cursor += 1
            move.play()
        elif event.key == pygame.K_UP and cursor - 7 >= 0:
            cursor -= 7
            move.play()
        elif event.key == pygame.K_DOWN and cursor +7 < len(Alphabet):
            cursor += 7
            move.play()
        if event.key == pygame.K_z:
            move.play()
            return False,True,cursor,True,enter
        elif event.key == pygame.K_BACKSPACE:
            stock_ancient = cursor
            move.play()
            return False,True,'Erase',True,enter

        if event.key == pygame.K_RETURN:
            move.play()
            return False,True,cursor,False,True

    return False,True,cursor,False,enter
        

def modif_soul(state):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_F1]:
        return "blue"
    if pressed[pygame.K_F2]:
        return "red"
    return state

def eturn_events(soul_mode,player,fightbox):

    pressed =  pygame.key.get_pressed()

    if soul_mode == "red":
        if pressed[pygame.K_LEFT]:
            player.velocity[0] = -1
        elif pressed[pygame.K_RIGHT]:
            player.velocity[0] = 1
        else:
            player.velocity[0] = 0

        if pressed[pygame.K_UP]:
            player.velocity[1] = -1
        elif pressed[pygame.K_DOWN]:
            player.velocity[1] = 1
        else:
            player.velocity[1] = 0
    
    if soul_mode == "blue":
        global blue_lock
        ytop = player.rect.top
        ybottom = player.rect.bottom
        # Bouge a droite a gauche
        if pressed[pygame.K_LEFT]:
            player.velocity[0] = -1
        elif pressed[pygame.K_RIGHT]:
            player.velocity[0] = 1
        else:
            player.velocity[0] = 0
        # Coeur touche bas
        if ybottom >= fightbox.bottom-5:
            blue_lock = True
        # Coeur limite haut
        if ytop <= fightbox.top+(fightbox.bottom - fightbox.top)*0.01:
            blue_lock = False
        # Saut
        if pressed[pygame.K_UP] and blue_lock:
            player.velocity[1]=-1
        else:
            player.velocity[1]=1
            blue_lock = False

    player.swap_img(soul_mode)
    player.move(fightbox)
    
    return True

def pturn_events(tab,player,enemy,sound):
    global menu_pos,cursor, elements
    sound.set_volume(0.5)
    menu_pos = 0
    cursor = 0
    elements = 3

    selected = None
    for event in pygame.event.get(eventtype=[pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT :
            return False,tab,None
        if tab == [0,0,0,0]:
            return True,tab,selected
        if tab[0]:
            if event.key == pygame.K_z:
                selected = 'f'
            elif event.key == pygame.K_RIGHT:
                sound.play()
                tab = [0,1,0,0]
        elif tab[1]:
            if event.key == pygame.K_z:
                selected = 'a'
            elif event.key == pygame.K_RIGHT:
                sound.play()
                tab = [0,0,1,0]
            elif event.key == pygame.K_LEFT:
                sound.play()
                tab = [1,0,0,0]
        elif tab[2]:
            if event.key == pygame.K_z:
                selected = 'i'
            elif event.key == pygame.K_RIGHT:
                sound.play()
                tab = [0,0,0,1]
            elif event.key == pygame.K_LEFT:
                sound.play()
                tab = [0,1,0,0]
        elif tab[3]:
            if event.key == pygame.K_z:
                selected = 'm'
            elif event.key == pygame.K_LEFT:
                sound.play()
                tab = [0,0,1,0]

    if selected != 'f':
        if selected == 'a':
            lan = len(enemy.act)
            if elements - lan > 3:
                elements = 3 -(elements - lan)
                
        if selected == 'i':
            lan = len(player.inv)
            if elements - lan > 3:
                elements = 3 -(elements - lan)
                
        if selected == 'm':
            lan = len(enemy.mercy)
            if elements - lan > 3:
                elements = 3 -(elements - lan)
    else:
        elements = 1
    
    return True, tab, selected


menu_pos = 0
elements = 0
cursor = 0
def in_menu(tab,selected,box,player,enemy,sound,Item_use):
    global cursor,menu_pos,elements
    sound.set_volume(0.5)
    x,y = box.topleft
    x+= 50
    y+= 38
    coord = (x,y)
    lan = 0
    fonc = ["fight"]
    if selected == 'a':
        lan = len(enemy.act)
        fonc = enemy.act
    if selected == 'i':
        lan = len(player.inv)
        fonc = player.inv
    if selected == 'm':
        lan = len(enemy.mercy)
        fonc = enemy.mercy

    for event in pygame.event.get(eventtype=[pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT :
            return False,tab,selected,coord,elements,False,fonc[cursor]
        if event.key == pygame.K_ESCAPE:
            return True,[1,0,0,0],None,coord,elements,False,fonc[cursor]
        
        if event.key == pygame.K_UP :
            sound.play()
            if menu_pos > 0:
                menu_pos -= 1
                cursor -= 1
            elif elements>3:
                coord = (x,y+(80*menu_pos))
                elements-=1
                cursor -= 1
                return True,tab,selected,coord,elements,False,fonc[cursor]
            
        if event.key == pygame.K_DOWN:
            sound.play()
            if menu_pos < elements-1 and menu_pos <2:
                menu_pos += 1
                cursor += 1
            elif elements < lan:
                coord = (x,y+(80*menu_pos))
                elements+=1
                cursor += 1
                return True,tab,selected,coord,elements,False,fonc[cursor]
            
        if event.key == pygame.K_z:
            Item_use.play()
            if selected == 'i':
                return True,tab,selected,coord,elements,True,cursor
            return True,tab,selected,coord,elements,True,fonc[cursor]
    if selected == 'm':
        cursor = 0
        return True,tab,selected,coord,elements,False,fonc[0]
    coord = (x,y+(80*menu_pos))
    return True,tab,selected,coord,elements,False,fonc[cursor]

def fight_button_pressed():
    for event in pygame.event.get(eventtype=[pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT :
            return False,False
        if event.key == pygame.K_z:
            return True,True
    
    return True,False

### OVERWORLD ###

class Item:
    def __init__(self,item):
        self.img = pygame.image.load("sprites/ui/pie.png")
        self.img = pygame.transform.scale_by(self.img,2)
        self.rect = self.img.get_rect(center = (1100,800))
        self.item = item

    def collisions(self,perso):
        if self.rect.colliderect(perso.rect):
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_z]:
                    return True
        return False

def deplacement(personnage):
    pressed =  pygame.key.get_pressed()
    if personnage.velocity[0] == 0:
        if pressed[pygame.K_UP]:
            personnage.velocity[1] = -1
        elif pressed[pygame.K_DOWN]:
            personnage.velocity[1] = 1
        else:
            personnage.velocity[1] = 0

    if personnage.velocity[1] == 0:
        if pressed[pygame.K_RIGHT]:
            personnage.velocity[0] = 1
        elif pressed[pygame.K_LEFT]:
            personnage.velocity[0] = -1
        else:
            personnage.velocity[0] = 0
    personnage.deplacer()
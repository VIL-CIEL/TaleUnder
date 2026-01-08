#########################################
#                                       #
#                                       #
#              TaleUnder                #
#       Par Fabien, Noa et Theault      #
#                                       #
#                                       #
#########################################

# Commandes :

# - Flêches haut/bas/gauche/droite : aller dans une direction
# - Z : Selectionner/interagir

# Systèmes des Ames (coeurs):

# - Bleu clair : Peut bouger librement dans tous les sens
# - Bleu : Peut bouger librement de gauche a droite, mais est sous emprise d'une gravité

# Musiques et FX par TobyFox et Mugger

# Les lignes en # sont soit des lignes de description ou des lignes de débug
# Vous avez aussi a votre disposition la fonction debug() qui vous permet de
# voir le comportement d'une variable en temps réel, vous n'avez qu'a mettre
# les variables voulus dans le tableau en argument

import pygame
pygame.init()

height = 824
width = 1280

screen = pygame.display.set_mode((width,height))
fps = 60
from view import *
from controller import *
from model import *

class attack_G_D:

    def __init__(self,sens,rect,modif,speed=2):
        self.att_touch = True
        self.vitesse = speed
        self.sens = sens
        self.att = [0,0]
        if sens == 'r':
            self.att = [rect.top,rect.top+modif]
        if sens == 'l':
            self.att = [rect.right,rect.top+modif]
        if sens == 't':
            self.att = [rect.left+modif,rect.bottom]
        if sens == 'd':
            self.att = [rect.left+modif,rect.top]
        
        self.img =pygame.image.load("sprites/ui/att1.png").convert_alpha()
        self.rect = self.img.get_rect()


    def begin(self,enemy,rect):
        if self.att_touch :
            # attack
            enemy_attack(screen,"spear",attack1(self.att,self.vitesse,self.sens),self.img)
            # damage on soul
            self.att_touch = enemy.degat(self.att,player,rect,self.vitesse,self.sens,self.rect,"b",hurt)

class spear:
    def __init__(self,sens,rect,modif,speed=10):
        self.att_touch = True
        self.vitesse = speed
        self.sens = sens
        self.att = [0,0]
        self.img = pygame.image.load("sprites/ui/att3.png").convert_alpha()
        self.img = pygame.transform.scale_by(self.img,4)

        if sens == 'r':
            self.att = [0,rect.top+modif]
            self.img = pygame.transform.rotate(self.img,270)
        if sens == 'l':
            self.att = [width,rect.top+modif]
            self.img = pygame.transform.rotate(self.img,90)
        if sens == 't':
            self.att = [rect.left+modif,height]
        if sens == 'd':
            self.att = [rect.left+modif,0]
            self.img = pygame.transform.rotate(self.img,180)

        self.rect = self.img.get_rect()

    def passing(self,enemy,rect):
        if self.att_touch :
            # attack
            enemy_attack(screen,"spear",attack1(self.att,self.vitesse,self.sens),self.img)
            # damage on soul
            self.att_touch = enemy.degat(self.att,player,rect,self.vitesse,self.sens,self.rect,"s",hurt,(width,height))         

def fin_combat():
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Display the green boxes
    display_background(img)
    # Init boxfight
    surf,rect = boxfight(img,width*0.6,height*0.3,(width*0.5,height*0.6))
    surfrect = surf.get_rect(center = rect.center)
    # Init buttons
    buttons(img,rect,[0,0,0,0])
    player.rect.center = rect.center

    # Begin the loop
    combat_lock = True
    i = 0
    while combat_lock:
        # If window closed
        if window_quit():
            combat_lock = False
            return True,False
        else:
            # Print on the screen the static background
            screen.blit(img,(0,0))
            i += 0.08
            if i <= 20:
                Speaking(screen,rect,"* Enough. Now, its time to die, human",'Kopa')
                # Enemy anim
                display_enemy(screen,enemy,rect)
            elif i <= 40:
                Divided_solitude.stop()
                piano.play(99)
                Speaking(screen,rect,"* What are you doing Kopa ?",'Kris')
                display_enemy_frame(screen,enemy,rect,'look_yu')
            elif i <= 60:
                Speaking(screen,rect,"* Kris ? Wait it's dangerous, don't come, a human is here !",'Kopa','looking')
                display_enemy_frame(screen,enemy,rect,'looking')
            elif i <= 80:
                Speaking(screen,rect,"* Oh its okayyy, he can't be that bad",'Kris')
                display_enemy_frame(screen,enemy,rect,'looking')
            elif i <= 120:
                Speaking(screen,rect,"* You see ? He's not doing anything to me, don't be so mad to humans, they are not all bad",'Kris')
                display_enemy_frame(screen,enemy,rect,'looking')
                display_kris(screen,rect)
            elif i <= 140:
                Speaking(screen,rect,"* You pass too much time with Susie, i see...",'Kopa','look_yu')
                display_enemy_frame(screen,enemy,rect,'look_yu')
                display_kris(screen,rect)
            elif i <= 160:
                Speaking(screen,rect,"* Yes i know, but she's so cool! And i know you like her too",'Kris')
                display_enemy_frame(screen,enemy,rect,'looking')
                display_kris(screen,rect)
            elif i <= 180:
                Speaking(screen,rect,"* Mhh no, no, i don't really like this type of person",'Kopa','eyes')
                display_enemy_frame(screen,enemy,rect,'eyes')
                display_kris(screen,rect)
            elif i <= 200:
                Speaking(screen,rect,"* Mhh i see",'Kris')
                display_enemy_frame(screen,enemy,rect,'eyes')
                display_kris(screen,rect)
            elif i <= 230:
                Speaking(screen,rect,"* Nevermind, you can't be so mean to newcomers, even if they are human.",'Kris')
                display_enemy_frame(screen,enemy,rect,'looking')
                display_kris(screen,rect)
            elif i <= 260:
                Speaking(screen,rect,"* Everyone is different and i'd like it if you gave him a chance.",'Kris')
                display_enemy_frame(screen,enemy,rect,'looking')
                display_kris(screen,rect)
            elif i <= 280:
                Speaking(screen,rect,"* Okay... I'll let him go",'Kopa','look_yu')
                display_enemy_frame(screen,enemy,rect,'look_yu')
                display_kris(screen,rect)
            elif i > 279:
                vaporised.stop()
                piano.stop()
                combat_lock = False
                return False,True

            # Hp bar, name...
            fight_elements(screen,player,rect)
            
            # debug
            # debug(screen,[clock])
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(fps)
            pygame.display.update()

def transition(txt):
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Display the green boxes
    display_background(img)
    # Init boxfight
    surf,rect = boxfight(img,width*0.6,height*0.3,(width*0.5,height*0.6))
    surfrect = surf.get_rect(center = rect.center)
    # Init buttons
    buttons(img,rect,[0,0,0,0])
    player.rect.center = rect.center

    # Begin the loop
    combat_lock = True
    i = 0
    while combat_lock:
        # If window closed
        if window_quit():
            combat_lock = False
            return True,False
        else:
            # Print on the screen the static background
            screen.blit(img,(0,0))
            i += 0.1
            if i <= 15:
                Speaking(screen,rect,txt,'Kopa')
                # Enemy anim
                display_enemy(screen,enemy,rect)
            if i > 15:
                combat_lock = False
                return False,True

            # Hp bar, name...
            fight_elements(screen,player,rect)
            
            # debug
            # debug(screen,[clock])
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(fps)
            pygame.display.update()

def player_turn():
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Background
    display_background(img)
    # TextBox
    surf,rect = boxfight(img,width*0.6,height*0.3,(width*0.5,height*0.6),colors= (15,15,15))
    line_all = pygame.Surface((width,height))
    line_all.blit(img,(0,0))
    display_line(line_all,rect,2)
    # display_side_line(line_all,rect)
    line_mercy = pygame.Surface((width,height))
    line_mercy.blit(img,(0,0))
    display_line(line_mercy,rect,1)
    # Begin the loop
    combat_lock = True
    stop = False
    buttonstab = [1,0,0,0]
    selected = None
    last_tab = [0,0,0,0]
    action_pressed = False
    nmb_hit = 0
    cursor = 0
    damage = 0
    glove_t = [0,0,0,0,0]
    i,t,g,k,p = 0,0,0,0,0
    while combat_lock:
            # Print on the screen the static background
            if not action_pressed and selected != None and selected not in ['f','m']:
                screen.blit(line_all,(0,0))
            elif not action_pressed and selected == 'm':
                screen.blit(line_mercy,(0,0))
            else:
                screen.blit(img,(0,0))
            
            if selected == None:
                # Selection of the menu
                stop, buttonstab,selected = pturn_events(buttonstab,player,enemy,move)
                display_info(screen,rect,enemy)
            else:
                # In a menu
                if buttonstab != [0,0,0,0]:
                    last_tab = buttonstab
                    buttonstab = [0,0,0,0]
                
                if action_pressed:
                    
                    if selected == 'f':
                        stop, when_att = fight_button_pressed()
                        
                        if nmb_hit <= 5:
                            display_attack(screen,rect)
                        if when_att:
                            if nmb_hit <= 6:
                                p_weak.play()
                            elif nmb_hit <= 8:
                                p_strong.play()
                            nmb_hit += 1

                    if selected == 'a':
                        stop = not window_quit()
                        display_act_txt(screen,rect,enemy,cursor)
                        if nmb_hit > 10:
                            return False,True,[selected,cursor]
                        nmb_hit += 0.1
                    
                    if selected == 'i':
                        
                        stop = not window_quit()
                        display_item_txt(screen,rect,player,cursor)
                        if nmb_hit == 0:
                            recover_hp(player,player.inv[cursor]['hp_give'])
                        if nmb_hit > 10:
                            return False,True,[selected]
                        nmb_hit += 0.1

                    if selected == 'm':
                        stop = not window_quit()
                        display_mercy_txt(screen,rect,enemy,cursor)
                        if nmb_hit > 10:
                            return False,True, [selected,cursor]
                        nmb_hit += 0.1
                else:
                    stop,buttonstab,selected,arrow_coord,elem,action_pressed,cursor = in_menu(buttonstab,selected,rect,player,enemy,move,Item_use)
                    
                    if selected == None:
                        buttonstab = last_tab
                        last_tab = [0,0,0,0]

                    elif selected == 'f':
                        display_fight(screen,rect,player)

                    elif selected == 'a':
                        display_act(screen,rect,enemy,elem)

                    elif selected == 'i':
                        display_item(screen,rect,player,elem)

                    elif selected == 'm':
                        display_mercy(screen,rect,enemy,elem)
                    
                    display_arrow(screen,arrow_coord)

            
            # Buttons
            buttons(screen,rect,buttonstab)
            # Hp bar, name...
            fight_elements(screen,player,rect)
            # Enemy anim
            display_enemy(screen,enemy,rect)
            if selected == 'f':
                diff = clock.tick_busy_loop()
                if nmb_hit == 1:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[0] = 1
                if nmb_hit == 3:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[1] = 1

                if nmb_hit == 5:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[2] = 1

                if nmb_hit == 7:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[3] = 1

                if nmb_hit == 9:
                    damage += diff * player.info["at"]
                    damage = damage // (enemy.info["df"]*2)
                    nmb_hit += 1
                    glove_t[4] = 1

                if nmb_hit > 9:
                    nmb_hit += 1
                    display_attack_damage(screen,rect,damage)
                    
                    if nmb_hit >= 100:
                        enemy.info['hp'] -= damage
                        return False,True,['f']
                
                if glove_t[0]:
                    i = display_glove(screen,enemy,1,i)
                    if i > 16 :
                        glove_t[0] = 0
                if glove_t[1]:
                    t = display_glove(screen,enemy,2,t)
                    if t > 16 :
                        glove_t[1] = 0
                if glove_t[2]:
                    g = display_glove(screen,enemy,3,g)
                    if g > 16 :
                        glove_t[2] = 0
                if glove_t[3]:
                    k = display_glove(screen,enemy,4,k)
                    if k > 16 :
                        glove_t[3] = 0
                if glove_t[4]:
                    p = display_glove(screen,enemy,5,p)
                    if p > 16 :
                        glove_t[4] = 0
            # Misc
            # debug(screen,[clock])
            player.update_stats()
            sort_inv()
            clock.tick(fps)
            
            pygame.display.update()
            if not stop:
                return True,False,[]

def enemy_turn(soul,state):
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Display the green boxes
    display_background(img)
    # Init boxfight
    surf,rect = boxfight(img,width*0.4,height*0.3,(width*0.5,height*0.6))
    surfrect = surf.get_rect(center = rect.center)
    # Init buttons
    buttons(img,rect,[0,0,0,0])
    player.rect.center = rect.center

    if state == 1:
        ATT_First = [attack_G_D('r',rect,10),attack_G_D('r',rect,1*100+10),attack_G_D('r',rect,2*100+10)]
        ATT_Second = [attack_G_D('l',rect,60,10),attack_G_D('l',rect,160,10)]
        ATT_Third = [attack_G_D('t',rect,0),attack_G_D('t',rect,80),attack_G_D('t',rect,80*2),attack_G_D('t',rect,80*3),attack_G_D('t',rect,80*4),attack_G_D('t',rect,80*5),attack_G_D('t',rect,80*6)]
        ATT_Fourth = [attack_G_D('d',rect,40,4),attack_G_D('d',rect,40*3,4),attack_G_D('d',rect,40*5,4),attack_G_D('d',rect,40*7,4),attack_G_D('d',rect,40*9,4),attack_G_D('d',rect,40*9,4),attack_G_D('d',rect,40*11,4)]
    if state == 2:
        ATT_First = [spear('l',rect,100,9),spear('r',rect,20),spear('r',rect,180)]
        ATT_Second = [spear('l',rect,20,12),spear('l',rect,100,15),spear('l',rect,180)]
        ATT_Third = [spear('t',rect,20,12),spear('t',rect,100,12),spear('t',rect,180,12),spear('t',rect,340,12),spear('t',rect,440,12)]

    if state == 3:
        ATT_First = [spear('r',rect,200),spear('r',rect,150)]
        ATT_Second = [spear('l',rect,0,15),spear('l',rect,50,15),spear('l',rect,100,15)]
        ATT_Third = [spear('r',rect,200),spear('l',rect,150,20)]
        ATT_Fourth = [spear('r',rect,200,15),spear('l',rect,200),spear('l',rect,150)]
        ATT_Fifth = [spear('l',rect,50,15),spear('l',rect,100,15),attack_G_D('t',rect,0,5),attack_G_D('t',rect,150,5),attack_G_D('t',rect,350,5),attack_G_D('t',rect,480,5)]

    ATT = 0
    # Begin the loop
    combat_lock = True
    while combat_lock:
        # If window closed
        if window_quit():
            combat_lock = False
            return True,False
        else:
            # Print on the screen the static background
            screen.blit(img,(0,0))

            ATT += 1
            
            if state == 1:
                for el in ATT_First:
                    if not el.att_touch:
                        ATT_First.pop(ATT_First.index(el))
                    el.begin(enemy,rect)

                if ATT > 100:
                    for el in ATT_Second:
                        if not el.att_touch:
                            ATT_Second.pop(ATT_Second.index(el))
                        el.begin(enemy,rect)
                
                if ATT > 150:
                    for el in ATT_Third:
                        if not el.att_touch:
                            ATT_Third.pop(ATT_Third.index(el))
                        el.begin(enemy,rect)
                
                if ATT > 200:
                    for el in ATT_Fourth:
                        if not el.att_touch:
                            ATT_Fourth.pop(ATT_Fourth.index(el))
                        el.begin(enemy,rect)
                
                if ATT > 280:
                    return False,True
           
            if state == 2:
                for el in ATT_First:
                    if not el.att_touch:
                        ATT_First.pop(ATT_First.index(el))
                    el.passing(enemy,rect)

                if ATT > 100:
                    for el in ATT_Second:
                        if not el.att_touch:
                            ATT_Second.pop(ATT_Second.index(el))
                        el.passing(enemy,rect)

                if ATT > 120:
                    for el in ATT_Third:
                        if not el.att_touch:
                            ATT_Third.pop(ATT_Third.index(el))
                        el.passing(enemy,rect)

                if ATT > 220:
                    return False,True
                    
            if state == 3:
                for el in ATT_First:
                    if not el.att_touch:
                        ATT_First.pop(ATT_First.index(el))
                    el.passing(enemy,rect)

                if ATT > 80:
                    for el in ATT_Second:
                        if not el.att_touch:
                            ATT_Second.pop(ATT_Second.index(el))
                        el.passing(enemy,rect)

                if ATT > 160:
                    for el in ATT_Third:
                        if not el.att_touch:
                            ATT_Third.pop(ATT_Third.index(el))
                        el.passing(enemy,rect)
                
                if ATT > 240:
                    for el in ATT_Fourth:
                        if not el.att_touch:
                            ATT_Fourth.pop(ATT_Fourth.index(el))
                        el.passing(enemy,rect)
                
                if ATT > 280:
                    for el in ATT_Fifth:
                        if type(el) == attack_G_D:
                            el.begin(enemy,rect)
                        elif type(el) == spear:
                            el.passing(enemy,rect)
                        if not el.att_touch:
                            ATT_Fifth.pop(ATT_Fifth.index(el))
                
                if ATT > 380:
                    return False,True
            
            if player.info['current_hp'] <= 5 or enemy.info['hp'] <= 5:
                if not enemy.info['hp'] <= 5:
                    player.info['current_hp'] = 1
                return True,True


            # Hp bar, name...
            fight_elements(screen,player,rect)
            # Enemy anim
            display_enemy(screen,enemy,rect)
            # draw the soul
            draw_player(screen,player)
            # debug
            # debug(screen,[clock,player.rect,ATT])
            # blue/red soul
            soul = modif_soul(soul)
            # Stop condition
            combat_lock = eturn_events(soul_mode=soul,player=player,fightbox=rect)
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(fps)
            pygame.display.update()

def debut_combat(Emergency_Stop,overworld_lock):
    soul = 'red'
    Divided_solitude.play(99)
    Emergency_Stop,overworld_lock,info = player_turn()

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = transition("* Do you think you're special or something ?")

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = enemy_turn(soul,1)

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock,info = player_turn()

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = transition("* Not bad, kid, prepare yourself")

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = enemy_turn(soul,2)

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock,info = player_turn()

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = transition("* Gosh human, you're hard to kill isn't it ?\nNow die.")

    if overworld_lock and not Emergency_Stop:
        soul = 'blue'
        Emergency_Stop,overworld_lock = enemy_turn(soul,3)

    if overworld_lock and not Emergency_Stop:
        Emergency_Stop,overworld_lock = fin_combat()
    
    if Emergency_Stop and overworld_lock:
        Emergency_Stop = False
        Emergency_Stop,overworld_lock = fin_combat()

    return Emergency_Stop,overworld_lock

# Stop Condition -> pygame.QUIT
Emergency_Stop = False

# ALL the FX
Entry = pygame.mixer.Sound("FX/mus_sfx_cinematiccut.wav")
Name_pad = pygame.mixer.Sound("FX/mus_disturbing.ogg")
move = pygame.mixer.Sound("FX/snd_squeak.wav")
Item_use = pygame.mixer.Sound("FX/snd_item.wav")
p_weak = pygame.mixer.Sound("FX/snd_punchweak.wav")
p_strong = pygame.mixer.Sound("FX/snd_punchstrong.wav")
p_giga = pygame.mixer.Sound("FX/mus_sfx_gigapunch.wav")
hurt = pygame.mixer.Sound("FX/snd_hurt1.wav")
battle_fall = pygame.mixer.Sound("FX/snd_battlefall.wav")
noise = pygame.mixer.Sound("FX/snd_noise.wav")
equip = pygame.mixer.Sound("FX/snd_buyitem.wav")
vaporised = pygame.mixer.Sound("FX/snd_vaporized.wav")
# ALL the Songs
Divided_solitude = pygame.mixer.Sound("song/final_archon.mp3")
Divided_solitude.set_volume(0.5)
cave = pygame.mixer.Sound("song/papyrus-overworld.mp3")
Divided_solitude.set_volume(0.7)
piano = pygame.mixer.Sound("song/piano_overworld_section_v2.mp3")
piano.set_volume(0.8)

# Window Name and Icon
ico = pygame.image.load("sprites/Souls/new_soul.png")
pygame.display.set_caption("TaleUnder_BETA")
pygame.display.set_icon(ico)

# Note # Si vous avez du mal avec le combat, changez la valeur du niveau du personnage
#      # cependant le niveau doit être compris entre 1 et 20 inclus, les stats seront
#      # proportionnel au niveau
#      # L'exp est aussi fonctionnel, mais cela n'est pas très précis si vous voulez
#      # un niveau précis

# Note # Il faut savoir que normalement l'enemy ne peut pas être tué car le jeu commence
#      # au niveau 1 donc un ajout trop important de niveau peut donner un résultat illogique

info = {}
info["name"] = "Niko"
info["xp"] = 0
info["level"] = 1
info["hp"] = hp_system[info["level"]]
info["current_hp"] = info["hp"]
info["at"] = at_system[info["level"]]
info["df"] = df_system[info["level"]]


player = Player(info,player_inventory)

clock = pygame.time.Clock()
screenrect = screen.get_rect()

Entry.play()
Entry.set_volume(0.4)
# Start of the Game
start_lock = True
while start_lock:
    screen.fill((0,0,20))
    display_StartScreen(screen)
    start_lock,Emergency_Stop = waiting_room()
    clock.tick(fps)
    pygame.display.update()
 
name_lock = not Emergency_Stop
cursor = 0
txt = ''
ind = 0
enter = False
Name_pad.set_volume(0.4)
Name_pad.play(99)
while name_lock:
    
    screen.fill((0,0,20))
    Emergency_Stop,name_lock,cursor,select,enter = name_ev(cursor,enter,move)
    if txt == '':
        enter = False
    if enter:
        if not Emergency_Stop:
            Emergency_Stop = selection_name(screen,(width,height),txt,ind)
        ind += 1
        if ind > 160:
            name_lock = False
    else:
        txt = name_pad(screen,(width,height),cursor,select)
    
    clock.tick(fps)
    pygame.display.update()
Name_pad.stop()

# Pense bête pour les tailles de boites différentes
# cube_box = boxfight(screen,width*0.2,height*0.3,(width*0.5,height*0.6))
# large_box = boxfight(screen,width*0.4,height*0.3,(width*0.5,height*0.6))
# dialogue_box = boxfight(screen,width*0.6,height*0.3,(width*0.5,height*0.6))

overworld_lock = not Emergency_Stop
enemy = Kopa()

### OVERWORLD ###
map = Map()

combat1 = Debutcombat(pygame.Rect(5000,1885,10,600))
combats = [combat1]

item1 = Item(Butterscotch_Pie)
items = [item1]

perso = Personnage()
map.set_position((0,0))
camera = Camera(5700,2975)
perso.set_position((900,2350))

new_item = False
txt = []
t = 0

stop = False

### ###
cave.play(99)
while overworld_lock:
    screen.fill((0,0,20))
    if window_quit():
        overworld_lock = False
        Emergency_Stop = True
    else:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                overworld = False
                Emergency_Stop = False
        if not stop :
            deplacement(perso)
            anim_perso(perso,frame)
        camera.update(perso)

        draw_map(screen, map.img, camera)

        for elt in map_collisions:
            elt.collisions(perso)
            # pygame.draw.rect(map.img,(255,0,0),elt.rect)

        if items != []:
            for item in items:
                if item.collisions(perso):
                    equip.play()
                    player_inventory.append(item.item)
                    txt = [item.item]
                    items.pop(0)
                    map.img = pygame.image.load("sprites/maps/Fullmap.png")
                    map.img = pygame.transform.scale(map.img, (5812, 3070))
                    new_item = True
                else:
                    draw_item(map.img,item)

        if new_item:
            display_text_item_o(screen,txt[0])
            t += 1
            if t > 80:
                new_item = 0
                t = 0

        draw_player_o(screen, perso,camera)
        
        
        for combat in combats:
            if combat.collisions(perso):
                cave.stop()
                stop = True
                t += 1
                if t < 10:
                    screen.fill("black")
                elif t < 20:
                    screen.fill((0,0,50))
                    if t == 10:
                        noise.play()
                elif t < 30:
                    screen.fill("black")
                    if t == 20:
                        noise.play()
                elif t < 40:
                    screen.fill((0,0,50))
                    if t == 30:
                        noise.play()
                elif t < 50:
                    battle_fall.play()
                    Emergency_Stop,overworld_lock = debut_combat(Emergency_Stop,overworld_lock)
                    overworld_lock = False
            # pygame.draw.rect(map.img,(0,0,255),combat.rect)

        # debug(screen,[clock,perso.rect,item.rect])    
        pygame.display.update()
        clock.tick(60)
        
end_lock = not Emergency_Stop
slt = 0
Name_pad.play()
while end_lock:
    
    screen.fill((0,0,20))
    if window_quit():
        end_lock = False
        Emergency_Stop = True
    slt += 1
    display_EndScreen(screen)

    if slt > 250:
        end_lock = False

    clock.tick(fps)
    pygame.display.update()


pygame.quit()
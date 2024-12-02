import pygame
import random
import numpy as np
from pygame.locals import *
import sys



maxplayer = 0
turn = 0
animestat = 0 #アニメーションを入れるとき値を保管したいでしょ？使ってね。
animemem = 0 #変化の起点だから前の情報入れたいね。
prog = 1

player = []
statlk = -1
turn_control = 0
turn = 0
selectc = []  #reforce attack altimateの順番。
selectc.append(-1)
selectc.append(-1)
selectc.append(-1)
target = -1


sum = []
sum.append(1)
sum.append(1)
sum.append(1)

summp = []
summp.append(0)
summp.append(0)
summp.append(0)

class Player:
    def __init__(self):
        self.job = -1
        self.name = " "
        self.jobname = " "
        self.hp = 0
        self.atstat = 0
        self.magicstat = 0
        self.magicdefstat = 0
        self.defstat = 0
        self.altimate = 0
        self.altpoint = 0
        self.atcard = np.zeros((3,3))  #1は物理、２は魔法,3は回復、4は全体攻撃。
        self.reforce = np.zeros((2,3)) #0 ~ 3でプラス強化するステータス値を選択する。アルティメットポイント+1をするやつとluckを上げるやつを追加する。
        self.atpower = [0,0]
        self.alivestat = 1 #0: dead 1: alive 生きている。
        self.luck = 1
        self.mpshow = 0


    def jobselect(self,jobs):
        if jobs == 0:
            self.job = 0
            self.attacker()
        elif jobs == 1:
            self.job = 1
            self.healer()
        elif jobs == 2:
            self.job = 2
            self.sorcerer()
        elif jobs == 3:
            self.job = 3
            self.defender()
        elif jobs == 4:
            self.luckman()
            
    def attacker(self):
        self.jobname = "attacker"
        self.job = 0
        self.hp = 800
        self.atstat = 120
        self.magicstat = 60
        self.magicdefstat = 30
        self.defstat = 40
        self.mp = 100
        self.altimate = 2

    def healer(self):
        self.jobname = "healer"
        self.job = 1
        self.hp = 700
        self.atstat = 50
        self.magicstat = 100
        self.magicdefstat = 60
        self.defstat = 40
        self.mp = 300
        self.altimate = 4


    def sorcerer(self):
        self.jobname = "sorcerer"
        self.job = 2
        self.hp = 500
        self.atstat = 30
        self.magicstat = 140
        self.magicdefstat = 50 
        self.defstat = 30
        self.mp = 500
        self.altimate = 5

    def defender(self):
        self.jobname = "defender"
        self.job = 3
        self.hp = 850
        self.atstat = 100
        self.magicstat = 40
        self.magicdefstat = 50
        self.defstat = 60
        self.mp = 100
        self.altimate = 4

    def luckman(self):
        self.jobname = "luckman"
        self.job = 4
        self.hp = int(random.normalvariate(500,250))
        self.atstat = int(random.normalvariate(70,15))
        self.magicstat = int(random.normalvariate(70,15))
        self.magicdefstat = int(random.normalvariate(50,15))
        self.defstat = int(random.normalvariate(50,15))
        self.mp = int(random.normalvariate(300,150))
        self.luck = (random.normalvariate(1,0.5))

        self.altimate = 3
        if self.hp < 0 or self.atstat < 0 or self.magicstat < 0 or self.magicdefstat < 0 or self.defstat < 0 :
            self.luckman()

    def angel(self):
        self.name = "angel"
    
    def fallen_angel(self):
        self.name = "fallen_angel"
    
    def vampire(self):
        self.name = "vampire"
        

    def showstates(self):
        print("hp",self.hp,"attack",self.atstat,"magic",self.magicstat,"defence",self.defstat,"magicdef",self.magicdefstat)

    def states_up(self,plus,plustat,level):
        if plustat == 0:
            self.atstat = self.atstat + plus

        elif plustat == 1:
            self.magicstat = self.magicstat + plus

        elif plustat == 2:
            self.magicdefstat = self.magicdefstat + plus

        elif plustat == 3:
            self.defstat = self.defstat + plus

        self.atstat = int(self.atstat*level)
        self.magicstat = int(self.magicstat*level)
        self.magicdefstat = int(self.magicdefstat*level)
        self.defstat = int(self.defstat *level)
    
    def card_draw(self):
        for stat in range(3):
            self.atcard[0][stat] = random.randint(1,8)
            if self.atcard[0][stat] == 1:
                self.atcard[1][stat] = random.normalvariate(0.8*self.luck,0.3*self.luck)

            elif self.atcard[0][stat] == 2:
                self.atcard[1][stat] = random.normalvariate(1.3*self.luck,0.3*self.luck)

            elif self.atcard[0][stat] ==3:
                healamo = random.randint(1,3)
                self.atcard[1][stat] = int(50*healamo)

            elif self.atcard[0][stat] == 4:
                self.atcard[1][stat] = random.normalvariate(0.65*self.luck,0.4*self.luck)

            elif self.atcard[0][stat] == 5:
                self.atcard[1][stat] = 1

            elif self.atcard[0][stat] == 6:
                self.atcard[1][stat] = 1
            
            elif self.atcard[0][stat] == 7:
                self.atcard[1][stat]
                self.atcard[1][stat] = random.normalvariate(1.1*self.luck,0.4*self.luck)
            
            elif self.atcard[0][stat] == 8:
                self.atcard[1][stat]
                self.atcard[1][stat] = random.normalvariate(0.5*self.luck,0.3*self.luck)


            self.reforce[0][stat] = random.randint(0,6)
            if self.reforce[0][stat] == 4:
                lk = random.randint(0,100)
                if lk < 5:
                    self.reforce[1][stat] = 1
                elif lk <10:
                    self.reforce[1][stat] = 0.4
                elif lk < 20:
                    self.reforce[1][stat] = 0.2
                else:
                    self.reforce[1][stat] = 0.1
            
            elif self.reforce[0][stat] == 5:
                mp = random.randint(0,100)
                if mp < 5:
                    self.reforce[1][stat] = 500
                elif mp < 10:
                    self.reforce[1][stat] = 300
                elif mp < 30:
                    self.reforce[1][stat] = 200
                else:
                    self.reforce[1][stat] = 100
            
            elif self.reforce[0][stat] == 6:
                self.reforce[1][stat] = 1

            else:
                self.reforce[1][stat] = random.normalvariate(40*self.luck,20*self.luck)
        #print("attack_card ",self.atcard[0],self.atcard[1])
        #print("reforce_card",self.reforce[0],self.reforce[1])

    def select_stcard_draw(self,select):
        if self.reforce[0][select] == 4:
            self.luck = self.luck + self.reforce[1][select]
        
        elif self.reforce[0][select] == 5:
            self.mp = int(self.mp + self.reforce[1][select])
        
        elif self.reforce[0][select] == 6:
            self.altpoint = int(self.altpoint + self.reforce[1][select])

        else:
            self.states_up(self.reforce[1][select],self.reforce[0][select],1)
            

    def select_attack_card(self,attack):
        if self.atcard[0][attack] == 1:
            self.atpower[0] = 1
            self.atpower[1] = int(self.atstat * self.atcard[1][attack])
        
        elif self.atcard[0][attack] == 2:
            self.atpower[0] = 2
            self.atpower[1] = int(self.magicstat * self.atcard[1][attack])
            self.mpshow = int(self.atpower[1]*0.5)

        elif self.atcard[0][attack] == 3:
            self.atpower[0] = 3
            self.atpower[1] = self.atcard[1][attack]

        elif self.atcard[0][attack] == 4:
            self.atpower[0] = 4
            self.atpower[1] = int(self.atstat * self.atcard[1][attack])
        
        elif self.atcard[0][attack] == 5:
            self.atpower[0] = 5
            value = random.randint(0,100)
            if value < 10:
                self.atpower[1] = 100

            elif value <40:
                self.atpower[1] = 70

            elif value <50:
                self.atpower[1] = 50
                   
            else:
                self.atpower[1] = 30
        
        elif self.atcard[0][attack] == 6:
            self.atpower[0] = 6
            value = random.randint(0,100)
            if value < 10:
                self.atpower[1] = 100
                self.mpshow = 50

            elif value <40:
                self.atpower[1] = 70
                self.mpshow = 40

            elif value <50:
                self.atpower[1] = 60
                self.mpshow = 30

            else:
                self.atpower[1] = 40
                self.mpshow = 20
        
        elif self.atcard[0][attack] == 7:
            self.atpower[0] = 7
            self.atpower[1] = int(self.magicstat * self.atcard[1][attack])
            self.mpshow = int(self.atpower[1]*0.5)

        elif self.atcard[0][attack] == 8:
            self.atpower[0] = 8
            self.atpower[1] = int(self.magicstat * self.atcard[1][attack])
            self.mpshow = int(self.atpower[1]*0.5)

    def passive(self):
        if self.job == 0:
            self.atstat = self.atstat + 20
        if self.job == 1:
            self.hp = self.hp + 50
        if self.job == 2:
            self.magicstat = self.magicstat + 20
        if self.job == 3:
            self.atstat = self.atstat + 10
            self.defstat = self.defstat + 10
        if self.job == 4:
            self.luck = random.normalvariate(1,0.5)


    def attack(self,defender,maxplayer,player):
        if self.atpower[0] == 1:
            if self.atpower[1] - int(defender.defstat) > 0:
                defender.hp = defender.hp - self.atpower[1] + int(defender.defstat)
                defender.defstat = int(defender.defstat - self.atpower[1]*0.4)
                if defender.defstat < 0:
                    defender.defstat = 0


        elif self.atpower[0] == 2:
            if self.mpshow > self.mp:
                self.hp = self.hp+self.mp - self.mpshow
                self.mp = 0
                if self.hp < 0:
                    self.hp = 0
            else:
                self.mp = self.mp - self.mpshow

            if self.atpower[1] - int(defender.magicdefstat) > 0:
                defender.hp = defender.hp - self.atpower[1] + int(defender.magicdefstat)
                defender.magicdefstat = int(defender.magicdefstat - self.atpower[1]*0.4)
                if defender.magicdefstat < 0:
                    defender.magicdefstat = 0
        
        elif self.atpower[0] == 3:
            self.hp = int(self.hp + self.atpower[1])

        elif self.atpower[0] == 4:
            for i in range(maxplayer):
                if player[i] != self:
                    if self.atpower[1] - int(player[i].defstat) > 0:
                        player[i].hp = player[i].hp - self.atpower[1] + int(player[i].defstat)
                        if player[i].hp < 0:
                            player[i].hp = 0

        elif self.atpower[0] == 5:
            defender.defstat = defender.defstat - self.atpower[1]
            if defender.defstat < 0:
                defender.defstat = 0
        
        elif self.atpower[0] == 6:
            if self.mpshow > self.mp:
                self.hp = self.hp+self.mp - self.mpshow
                self.mp = 0
                if self.hp < 0:
                    self.hp = 0
            else:
                self.mp = self.mp - self.mpshow

            defender.magicdefstat = defender.magicdefstat - self.atpower[1]
            if defender.magicdefstat < 0:
                defender.magicdefstat = 0
        
        elif self.atpower[0] == 7:
            if self.mpshow > self.mp:
                self.hp = self.hp+self.mp - self.mpshow
                self.mp = 0
                if self.hp < 0:
                    self.hp = 0
            else:
                self.mp = self.mp - self.mpshow
            
            for i in range(maxplayer):
                if player[i] != self:
                    if self.atpower[1] - int(player[i].defstat) > 0:
                        player[i].hp = player[i].hp - self.atpower[1] + int(player[i].defstat)
                        if player[i].hp < 0:
                            player[i].hp = 0
        
        elif self.atpower[0] == 8:
            if self.mpshow > self.mp:
                self.hp = self.hp+self.mp - self.mpshow
                self.mp = 0
                if self.hp < 0:
                    self.hp = 0
            else:
                self.mp = self.mp - self.mpshow
                if self.atpower[1] - int(defender.magicdefstat) > 0:
                    defender.hp = defender.hp - self.atpower[1] + int(defender.magicdefstat)
                    if self.hp > 0:
                        self.hp = self.hp + self.atpower[1] - int(defender.magicdefstat)
                    if defender.magicdefstat < 0:
                        defender.magicdefstat = 0
            
        
        if defender.hp < 0:
            defender.hp = 0
            if self.hp == 0:
                defender.hp = 1
    
    def alt_attacker(self,mode,enemy):
        if mode == 0 and self.altimate <= self.altpoint:
            self.atstat = self.atstat*1.5
            self.magicstat = self.magicstat + self.atstat * 0.5
            self.altpoint = self.altpoint - self.altimate

        if mode == 1 and self.altimate <= self.altpoint:
            enemy.hp = enemy.hp + int(enemy.defstat) - int(self.atstat*2)
            self.altpoint = self.altpoint - self.altimate
            if enemy.hp < 0:
                enemy.hp = 0

    def alt_healer(self):
        if self.altimate <= self.altpoint:
            self.magicstat = self.magicstat + int(self.hp*0.1)
            self.magicdefstat = int(self.magicdefstat*1.2) 
            self.altpoint = self.altpoint - self.altimate

    def alt_sorcerer(self,maxplayer,player):
        if self.altpoint >= self.altimate:
            for i in range(maxplayer):
                if player[i] != self:
                    player[i].atstat = int(player[i].atstat*0.6)
                    player[i].magicstat = int(player[i].magicstat*0.6)
                    player[i].defstat = int(player[i].defstat*0.6)
                    player[i].magicdefstat = int(player[i].magicdefstat*0.6)
                    self.altpoint = self.altpoint - self.altimate
    
    def alt_defender(self):
        if self.altpoint >= self.altimate:
            self.atstat = int(self.defstat*1.5)
            self.magicstat = int(self.magicdefstat*1.5)
            self.altpoint = self.altpoint - self.altimate

    def alt_luckman(self,enemy):
        enemy.luck = enemy.luck * 0.7
        self.altpoint = self.altpoint - self.altimate
        

    def dead(self):
        if self.hp == 0:
            self.alivestat = 0



screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Button Example")

# ボタン描画関数



def progress(sign):
    global prog,animestat,animemem

    prog = prog + sign
    animestat = 0
    animemem = 0
    if prog == 2:
        playercreate()
    

def playercreate():
    global player
    global maxplayer

    for i in range(maxplayer):
        player.append(" ")
        player[i] = Player()

def draw_text(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = -2

    # テキストを単語ごとに分割
    words = [word.split(' ') for word in text.splitlines()]
    space_width, space_height = font.size(' ')
    
    # 各行ごとに描画処理
    for line in words:
        x = rect.left
        for word in line:
            word_surface = font.render(word, aa, color, bkg)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= rect.right:
                x = rect.left  # 次の行に移動
                y += word_height + line_spacing
            surface.blit(word_surface, (x, y))
            x += word_width + space_width
        y += word_height + line_spacing
        if y >= rect.bottom:
            break  # テキストが枠を超えた場合終了

def draw_button(screen, x, y, width, height, text, text_color, button_color, action=None, image=None):
    # ボタンの長方形
    button_rect = pygame.Rect(x, y, width, height)

    if image:
        # 画像が指定されている場合、画像をボタンとして使用
        image = pygame.transform.scale(image, (width, height))
        screen.blit(image, button_rect)
    else:
        # 画像がない場合は、色でボタンを描画
        pygame.draw.rect(screen, button_color, button_rect)

    # フォント設定
    font = pygame.font.SysFont(None, 24)

    # テキストを描画
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # マウスのクリックイベントを取得
    mouse_pos = pygame.mouse.get_pos()

    if button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] and action:
            action()


# ボタンをクリックした時に実行される関数
def maxplay(num):
    global maxplayer
    maxplayer = num

def chstat(num):
    global statlk
    if num == 0:
        #animemem = Player()
        #animemem.jobselect(0)
        #draw_button(screen,0,200,300,300,"","blue","black",image=pygame.image.load("at_ba.png"))
        statlk = 0

    if num == 1:
        statlk = 1
    if num == 2:
        statlk = 2
    if num == 3:
        statlk = 3
    if num == 4:
        statlk = 4

def ch_confirm(num):
    global animemem,statlk
    player[animemem].jobselect(num)
    animemem = animemem + 1
    statlk = -1
    if animemem == maxplayer:
        progress(1)
    #print(statlk.hp)

def skip_turn():
    global turn,maxplayer
    turn = turn + 1
    if turn == maxplayer:
        turn = 0


def turn_prepare():
    global player,turn_control,target,sum,maxplayer,summp

    for i in range(maxplayer):
        player[i].dead()
        
    if player[turn].alivestat == 0:
        skip_turn()
        turn_prepare()
        return 0
    
    player[turn].altpoint = player[turn].altpoint + 1
    target = -1
    player[turn].passive()
    player[turn].card_draw()
    turn_control = 1
    print(player[1].hp)
    player[turn].showstates()
    


    for i in range(3):
        player[turn].select_attack_card(i)
        sum[i] = player[turn].atpower[1]
        summp[i] = player[turn].mpshow
        #print(sum[i])
        #print(i)


def reload_card():
    global sum,summp,player,turn
    player[turn].hp = player[turn].hp - 50
    player[turn].card_draw()
    for i in range(3):
        player[turn].select_attack_card(i)
        sum[i] = player[turn].atpower[1]
        summp[i] = player[turn].mpshow
    



def attack_action(card):
    global player
    global turn
    global selectc
    player[turn].select_attack_card(card)
    selectc[1] = card
    print(turn,player[turn].atpower[1])

def select_upcard(i):
    global selectc
    selectc[0] = i
 
def select_alt():
    global selectc
    if selectc[2]==1:
        selectc[2] = -1
    else:
        selectc[2] = 1

def display_draw_card():
    global selectc
    global player
    global turn
    global animestat
    global sum
    

    pat = pygame.image.load("./atcard/pat.png")
    mat = pygame.image.load("./atcard/mat.png")
    heal = pygame.image.load("./atcard/heal.png")
    allatk = pygame.image.load("./atcard/allatk.png")
    shbre = pygame.image.load("./atcard/shield_brake.png")
    mshbre = pygame.image.load("./atcard/mgshield_brake.png")
    allmg = pygame.image.load("./atcard/allmg.png")
    drain = pygame.image.load("./atcard/drain.png")

    patpl = pygame.image.load("./refcard/patpl.png")
    matpl = pygame.image.load("./refcard/matpl.png")
    patdef = pygame.image.load("./refcard/patdef.png")
    matdef = pygame.image.load("./refcard/matdef.png")
    luckst = pygame.image.load("./refcard/luck.png")
    mpup = pygame.image.load("./refcard/mpup.png")
    ultplus = pygame.image.load("./refcard/ultplus.png")

    for i in range(3):
        if player[turn].atcard[0][i] == 1:
            draw_button(screen,20+i*140,240,120,165,"      "+str(sum[i]),"red","green",lambda:attack_action(i),image=pat)
        elif player[turn].atcard[0][i] == 2:
            draw_button(screen,20+i*140,240,120,165,"  "+str(sum[i])+"  MP-"+str(summp[i]),"white","green",lambda:attack_action(i),image=mat)
        elif player[turn].atcard[0][i] == 3:
            draw_button(screen,20+i*140,240,120,165,"      "+str(sum[i]),"black","green",lambda:attack_action(i),image=heal)
        elif player[turn].atcard[0][i] == 4:
            draw_button(screen,20+i*140,240,120,165,"      "+str(sum[i]),"black","green",lambda:attack_action(i),image=allatk)
        elif player[turn].atcard[0][i] == 5:
            draw_button(screen,20+i*140,240,120,165,"      -"+str(sum[i]),"white","green",lambda:attack_action(i),image=shbre)
        elif player[turn].atcard[0][i] == 6:
            draw_button(screen,20+i*140,240,120,165,"      -"+str(sum[i])+"  MP-"+str(summp[i]),"white","green",lambda:attack_action(i),image=mshbre)
        elif player[turn].atcard[0][i] == 7:
            draw_button(screen,20+i*140,240,120,165,"      "+str(sum[i])+"  MP-"+str(summp[i]),"black","green",lambda:attack_action(i),image=allmg)
        elif player[turn].atcard[0][i] == 8:
            draw_button(screen,20+i*140,240,120,165,"   HP+"+str(sum[i])+"  MP-"+str(summp[i]),"white","green",lambda:attack_action(i),image=drain)

        if player[turn].reforce[0][i] == 0:
            draw_button(screen,20+i*140,410,120,165,"      +"+str(int((player[turn].reforce[1][i]))),"red","green",lambda:select_upcard(i+1),image=patpl)
            #draw_button(screen,20+i*140,410,120,165"      +"+str(int(player[turn].reforce[1][i]*turn)),"red","green",)

        elif player[turn].reforce[0][i] == 1:
            draw_button(screen,20+i*140,410,120,165,"      +"+str(int((player[turn].reforce[1][i]))),"blue","green",lambda:select_upcard(i+1),image=matpl)

        elif player[turn].reforce[0][i] == 2:
            draw_button(screen,20+i*140,410,120,165,"      +"+str(int((player[turn].reforce[1][i]))),"blue","green",lambda:select_upcard(i+1),image=matdef)

        elif player[turn].reforce[0][i] == 3:
            draw_button(screen,20+i*140,410,120,165,"      +"+str(int((player[turn].reforce[1][i]))),"red","green",lambda:select_upcard(i+1),image=patdef)

        elif player[turn].reforce[0][i] == 4:
            draw_button(screen,20+i*140,410,120,165,"             +"+str(float((player[turn].reforce[1][i]))),"black","green",lambda:select_upcard(i+1),image=luckst)

        elif player[turn].reforce[0][i] == 5:
            draw_button(screen,20+i*140,410,120,165,"           MP+"+str(float((player[turn].reforce[1][i]))),"black","green",lambda:select_upcard(i+1),image=mpup)

        elif player[turn].reforce[0][i] == 6:
            draw_button(screen,20+i*140,410,120,165,"             +"+str(float((player[turn].reforce[1][i]))),"black","green",lambda:select_upcard(i+1),image=ultplus)
        #print(player[turn].reforce[1][i])
    
    #player[turn].showstates()

def target_done(t):
    global target
    target = t


def turn_end(target):
    global turn_control
    global turn
    global selectc
    global maxplayer,player

    turn_control = 0
    
    if selectc[0] != -1 and selectc[1] != -1:
        player[turn].select_stcard_draw(selectc[0]-1)
        player[turn].attack(player[target],maxplayer,player)
        selectc[0] = -1
        selectc[1] = -1
    
    elif selectc[2] != -1:
        if player[turn].job == 0:
            player[turn].alt_attacker(1,player[target])
            #player[turn].altpoint = player[turn].altpoint - player[turn].altimate
            selectc[2] = -1

        elif player[turn].job == 1:
            player[turn].alt_healer()
            #player[turn].altpoint = player[turn].altpoint - player[turn].altimate
            selectc[2] -1
        
        elif player[turn].job == 2:
            player[turn].alt_sorcerer(maxplayer,player)
            #player[turn].altpoint = player[turn].altpoint - player[turn].altimate
            selectc[2] = -1

        elif player[turn].job == 3:
            player[turn].alt_defender()
            #player[turn].altpoint = player[turn].altpoint - player[turn].altimate
            selectc[2] = -1
        
        elif player[turn].job == 4:
            player[turn].alt_luckman(player[target])
            #player[turn].altpoint = player[turn].altpoint - player[turn].altimate
            selectc[2] = -1
    
    for i in range(3):
        summp[i] = 0
        

    turn = turn + 1 
    if turn == maxplayer:
        turn = 0
    
    player[target].states_up(0,-1,1)
    return turn


def tbox(screen, font, x, y, w, h, n):
    txt = ""
    isEnd = False  # 終了フラグ

    while True:
        pygame.draw.rect(screen, (200, 200, 240), Rect(x, y, w, h))  # ボックス内を塗潰す
        txtg = font.render(txt, True, (55, 55, 55))  # 描画する文字列を画像にする
        screen.blit(txtg, [x + 5, y + 5])  # 画像を表示
        pygame.display.update()  # 画面更新

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:  # 閉じるボタンが押されたら
                pygame.quit()
                sys.exit()  # 終了

            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_BACKSPACE:  # 修正で戻る
                    if len(txt) >= 1:
                        txt = txt[:-1]
                elif event.key == K_RETURN:  # エンターキー
                    isEnd = True
                    break

                if len(txt) < n:
                    if event.key == K_PERIOD:  # ピリオドが入力された
                        txt += "."
                    elif event.unicode.isnumeric():  # 数字が入力された
                        txt += event.unicode
                    elif event.unicode.isalpha():  # アルファベットが入力された
                        txt += event.unicode

        if isEnd == True:
            break

    return txt



pygame.init()
screen = pygame.display.set_mode((1000, 600))   # 画面の大きさを設定する
pygame.display.set_caption('display')   # 画面のタイトルを設定する

def START_ANIMATION(screen):
    img = [0,0,0,0,0,0,0,0,0,0]
    for num in range(10):
        img[num]=pygame.image.load("./startjpg/start"+str(num)+".jpg")
        screen.blit(img[num],(0,0))
        pygame.display.update()
        pygame.time.wait(200)


def open_information(i):
    global player
    draw_button(screen,500,100,200,50,"++ "+player[i].jobname+" ++","gray",(0,90,100))
    draw_button(screen,500,130,200,30,"atk:"+str(player[i].atstat),"gray",(0,90,100))
    draw_button(screen,500,160,200,30,"magic_atk:"+str(player[i].magicstat),"gray",(0,90,100))
    draw_button(screen,500,190,200,30,"defence:"+str(player[i].defstat),"gray",(0,90,100))
    draw_button(screen,500,220,200,30,"magic_defence:"+str(player[i].magicdefstat),"gray",(0,90,100))
    draw_button(screen,500,250,200,50,"MP:"+str(player[i].mp),"gray",(0,90,100))
    draw_button(screen,500,280,200,50,"luck:"+str(player[i].luck),"gray",(0,90,100))
    draw_button(screen,500,310,200,50,"ultimate:"+str(player[i].altpoint)+"/"+str(player[i].altimate),"gray",(0,90,100))




def gameflow(prog):
    global animestat
    global maxplayer
    global animemem
    global statlk
    global turn_control
    global turn
    global selectc
    global target

    font = pygame.font.Font(None,55)  #ゲームスタート画面
    if prog == 0:
        START_ANIMATION(screen)
        progress(1)
    
    elif prog == 1:  #プレイヤー人数決定。
        color = [0,0,0,0]
        num = 10

        if maxplayer == 2:
            if animestat > 50:
                num = -1
            if animemem != maxplayer:
                animestat = 0
                animemem = maxplayer

            animestat = animestat + num
            color[0] =  animestat
            color[1] = 0
            color[2] = 0
            color[3] = 0
        if maxplayer == 3:
            if animestat > 50:
                num = -2
            
            if animemem != maxplayer:
                animestat = 0
                animemem = maxplayer

            animestat = animestat + num
            color[0] = 0
            color[1] = animestat
            color[2] = 0
            color[3] = 0
        if maxplayer == 4:
            if animestat > 50:
                num = -3
            
            if animemem != maxplayer:
                animestat = 0
                animemem = maxplayer

            animestat = animestat + num
            color[0] = 0
            color[1] = 0
            color[2] = animestat
            color[3] = 0

        if maxplayer == 5:
            if animestat > 50:
                num = -4
            
            if animemem != maxplayer:
                animestat = 0
                animemem = maxplayer

            animestat = animestat + num
            color[0] = 0
            color[1] = 0
            color[2] = 0
            color[3] = animestat
        
        num2 = pygame.image.load("./players/2.png")
        num3 = pygame.image.load("./players/3.png")
        num4 = pygame.image.load("./players/4.png")
        num5 = pygame.image.load("./players/5.png")

        font = pygame.font.Font("./font/JKG-M_3.ttf",30)
        draw_text(screen,text="人数を選択してください",color="blue",rect=pygame.Rect(80,10,100,100),font=font)

        draw_button(screen,80-color[0],140-color[0],150+color[0]+color[0],206+color[0]+color[0],"","gray",(0,90,100),lambda:maxplay(2),image=num2)
        draw_button(screen,300-color[1],140-color[1],150+color[1]+color[1],206+color[1]+color[1],"","red",(140,0,0),lambda:maxplay(3),image=num3)
        draw_button(screen,520-color[2],140-color[2],150+color[2]+color[2],206+color[2]+color[2],"","green",(0,140,0),lambda:maxplay(4),image=num4)
        draw_button(screen,740-color[3],140-color[3],150+color[3]+color[3],206+color[3]+color[3],"","purple",(60,0,160),lambda:maxplay(5),image=num5)

        if maxplayer != 0:
            draw_button(screen,300,450,400,80,"confirmed","pink",(200,20,100),lambda:progress(1))
            

        else:
            draw_button(screen,300,450,400,80,"unconfirmed","gray",(50,50,50))


        print(maxplayer)
        for i in range(4):
            print(color[i],end=" ")



    elif prog == 2:
        if player[animemem].name != " ":
            animemem = animemem + 1
        

        back_ground = pygame.image.load("./screen/u22background.png")
        back_ground = pygame.transform.scale(back_ground,(1000,600))

        screen.blit(back_ground,(0,0))
        nameline = pygame.image.load("./gatget/nameline.png")
        font = pygame.font.Font("./font/JKG-M_3.ttf",30)
        draw_text(screen,text="名前を決めてください",color=(0,100,200),rect=pygame.Rect(300,10,100,100),font=font)


        
        for i in range(maxplayer):
            print(player[i].name)
            draw_button(screen,300,200+i*50,400,80,player[i].name,"black",(50,50,50),image=nameline)
        player[animemem].name = tbox(screen,font,300,100,400,45,15)
        
        
        if animemem == maxplayer-1:
            progress(1)

        

    elif prog == 3:
        back_ground = pygame.image.load("./screen/charjob.png")
        back_ground = pygame.transform.scale(back_ground,(1000,600))

        font = pygame.font.Font("./font/JKG-M_3.ttf",25)

        attacker = pygame.image.load("./charadeta/at_ba.png")
        attacker = pygame.transform.scale(attacker,(150,150))
        healer = pygame.image.load("./charadeta/he_ba.png")
        healer = pygame.transform.scale(healer,(150,150))
        sorcerer = pygame.image.load("./charadeta/sor_ba.png")
        sorcerer = pygame.transform.scale(sorcerer,(150,150))
        defender = pygame.image.load("./charadeta/def_ba.png")
        defender = pygame.transform.scale(defender,(150,150))
        luckman = pygame.image.load("./charadeta/luckman.png")
        luckman = pygame.transform.scale(luckman,(150,150))

        screen.blit(back_ground,(0,0))
        draw_button(screen,750,0,150,600,"","gray",(50,50,50))
        draw_button(screen,770,000,100,100,"","blue","green",action=lambda:chstat(0),image=attacker)
        draw_button(screen,770,100,100,100,"","blue","green",action=lambda:chstat(1),image=healer)
        draw_button(screen,770,200,100,100,"","blue","green",action=lambda:chstat(2),image=sorcerer)
        draw_button(screen,770,300,100,100,"","blue","green",action=lambda:chstat(3),image=defender)
        draw_button(screen,770,400,100,100,"","blue","green",action=lambda:chstat(4),image=luckman)

        selectch = Player()
        draw_button(screen,300,50,400,50,"SELECT   "+str(player[animemem].name)+"   CHARACTER",(50,50,70),"white")
        if statlk == 0:
            selectch.jobselect(statlk)
            draw_button(screen,0,000,300,300,"","blue","green",image=attacker)
            draw_button(screen,770,00,100,100,"","blue","green",image=pygame.image.load("./gatget/selectwaku.png"))
            draw_button(screen,100,300,120,50,"HP:"+str(selectch.hp),"gray",(50,50,70))
            draw_button(screen,100,350,120,50,"ATK:"+str(selectch.atstat),"gray",(50,50,70))
            draw_button(screen,100,400,120,50,"MAGIC:"+str(selectch.magicstat),"gray",(50,50,70))
            draw_button(screen,100,450,120,50,"DEF:"+str(selectch.defstat),"gray",(50,50,70))
            draw_button(screen,100,500,120,50,"MAGIC_DEF:"+str(selectch.magicdefstat),"gray",(50,50,70))
            draw_button(screen,100,550,120,50,"MP:"+str(selectch.mp),"gray",(50,50,70))
            draw_button(screen,220,550,120,50,"ULT:"+str(selectch.altimate),"gray",(50,50,70))
            draw_text(screen,text="剣士\nパッシブは物理攻撃力を+20\nウルトは対象の相手に物理攻撃力\nの二倍を攻撃\n無難に強め",color="black",rect=pygame.Rect(300,120,200,200),font=font)
            
        elif statlk == 1:
            selectch.jobselect(statlk)
            draw_button(screen,0,000,300,300,"","blue","green",image=healer)
            draw_button(screen,770,100,100,100,"","blue","green",image=pygame.image.load("./gatget/selectwaku.png"))
            draw_button(screen,100,300,120,50,"HP:"+str(selectch.hp),"gray",(50,50,70))
            draw_button(screen,100,350,120,50,"ATK:"+str(selectch.atstat),"gray",(50,50,70))
            draw_button(screen,100,400,120,50,"MAGIC:"+str(selectch.magicstat),"gray",(50,50,70))
            draw_button(screen,100,450,120,50,"DEF:"+str(selectch.defstat),"gray",(50,50,70))
            draw_button(screen,100,500,120,50,"MAGIC_DEF:"+str(selectch.magicdefstat),"gray",(50,50,70))
            draw_button(screen,100,550,120,50,"MP:"+str(selectch.mp),"gray",(50,50,70))
            draw_button(screen,220,550,120,50,"ULT:"+str(selectch.altimate),"gray",(50,50,70))
            draw_text(screen,text="ヒーラー\nパッシブはHP+50\nウルトは魔法攻撃力に体力の10%\nだけプラスし、魔法防御力を1.2倍する\n生き残りたいならこれ",color="black",rect=pygame.Rect(300,120,200,200),font=font)
            
        elif statlk == 2:
            selectch.jobselect(statlk)
            draw_button(screen,0,000,300,300,"","blue","green",image=sorcerer)
            draw_button(screen,770,200,100,100,"","blue","green",image=pygame.image.load("./gatget/selectwaku.png"))
            draw_button(screen,100,300,120,50,"HP:"+str(selectch.hp),"gray",(50,50,70))
            draw_button(screen,100,350,120,50,"ATK:"+str(selectch.atstat),"gray",(50,50,70))
            draw_button(screen,100,400,120,50,"MAGIC:"+str(selectch.magicstat),"gray",(50,50,70))
            draw_button(screen,100,450,120,50,"DEF:"+str(selectch.defstat),"gray",(50,50,70))
            draw_button(screen,100,500,120,50,"MAGIC_DEF:"+str(selectch.magicdefstat),"gray",(50,50,70))
            draw_button(screen,100,550,120,50,"MP:"+str(selectch.mp),"gray",(50,50,70))
            draw_button(screen,220,550,120,50,"ULT:"+str(selectch.altimate),"gray",(50,50,70))
            "魔法使い\nパッシブは魔法攻撃力を+20\nウルトは自分以外の全ての攻撃と防御のパラメータを40%減少\nつよいけど体力低いネ"
            draw_text(screen,text="魔法使い\nパッシブは魔法攻撃力を+20\nウルトは自分以外の全ての攻撃と防御の\nパラメータを40%減少\nつよいけど体力低いネ",color="black",rect=pygame.Rect(300,120,200,200),font=font)
            
        elif statlk == 3:
            selectch.jobselect(statlk)
            draw_button(screen,0,000,300,300,"","blue","green",image=defender)
            draw_button(screen,770,300,100,100,"","blue","green",image=pygame.image.load("./gatget/selectwaku.png"))
            draw_button(screen,100,300,120,50,"HP:"+str(selectch.hp),"gray",(50,50,70))
            draw_button(screen,100,350,120,50,"ATK:"+str(selectch.atstat),"gray",(50,50,70))
            draw_button(screen,100,400,120,50,"MAGIC:"+str(selectch.magicstat),"gray",(50,50,70))
            draw_button(screen,100,450,120,50,"DEF:"+str(selectch.defstat),"gray",(50,50,70))
            draw_button(screen,100,500,120,50,"MAGIC_DEF:"+str(selectch.magicdefstat),"gray",(50,50,70))
            draw_button(screen,100,550,120,50,"MP:"+str(selectch.mp),"gray",(50,50,70))
            draw_button(screen,220,550,120,50,"ULT:"+str(selectch.altimate),"gray",(50,50,70))
            draw_text(screen,text="タンカー\nパッシブはそれぞれの防御力を+10\nウルトはそれぞれの防御力を攻撃力に\n加える\n高い魔法防御と物理防御を両立している",color="black",rect=pygame.Rect(300,120,200,200),font=font)

        elif statlk == 4:
            selectch.jobselect(statlk)
            draw_button(screen,0,000,300,300,"","blue","green",image=luckman)
            draw_button(screen,770,400,100,100,"","blue","green",image=pygame.image.load("./gatget/selectwaku.png"))
            draw_button(screen,100,300,120,50,"HP:"+str(selectch.hp),"gray",(50,50,70))
            draw_button(screen,100,350,120,50,"ATK:"+str(selectch.atstat),"gray",(50,50,70))
            draw_button(screen,100,400,120,50,"MAGIC:"+str(selectch.magicstat),"gray",(50,50,70))
            draw_button(screen,100,450,120,50,"DEF:"+str(selectch.defstat),"gray",(50,50,70))
            draw_button(screen,100,500,120,50,"MAGIC_DEF:"+str(selectch.magicdefstat),"gray",(50,50,70))
            draw_button(screen,100,550,120,50,"MP:"+str(selectch.mp),"gray",(50,50,70))
            draw_button(screen,220,550,120,50,"ULT:"+str(selectch.altimate),"gray",(50,50,70))
            draw_text(screen,text="運だけ\nパッシブはラックをランダムに振る\nウルトは対象のラックを30%減少\nステータスすべてランダムできまる\n運がいい人向け",color="black",rect=pygame.Rect(300,120,200,200),font=font)

        if statlk >= 0:
            draw_button(screen,300,450,400,80,"confirmed","pink",(200,20,100),lambda:ch_confirm(statlk))


        else:
            draw_button(screen,300,450,400,80,"unconfirmed","gray",(50,50,50))

    elif prog == 4:
        back_ground = pygame.image.load("./screen/fightsc.png")
        back_ground = pygame.transform.scale(back_ground,(1000,600))
        screen.blit(back_ground,(0,0))

        attacker = pygame.image.load("./charadeta/at_ba.png")
        healer = pygame.image.load("./charadeta/he_ba.png")
        sorcerer = pygame.image.load("./charadeta/sor_ba.png")
        defender = pygame.image.load("./charadeta/def_ba.png")
        luckman = pygame.image.load("./charadeta/luckman.png")
        
        if turn_control == 0:
            turn_prepare()
        display_draw_card()

        csele = pygame.image.load("./gatget/case.png")
        draw_button(screen,-120+(selectc[0])*140,410,120,165,"      ","red","green",image=csele)
        draw_button(screen,-120+(selectc[1]+1)*140,240,120,165,"      ","red","green",image=csele)

        if player[turn].hp > 50:
            draw_button(screen,600,200,60,60,"redraw",(100,0,0),(200,100,0),reload_card)
        
        else:
            draw_button(screen,600,200,60,60,"redraw",(50,50,50),(100,100,100))

        draw_button(screen,0,150,700,50,"HP:"+str(player[turn].hp)+"  ATK:"+str(player[turn].atstat)+"  MAGIC:"+str(player[turn].magicstat)+"  DEF:"+str(player[turn].defstat)+"  MAGIC_DEF:"+str(player[turn].magicdefstat)+"  MP"+str(player[turn].mp)+"  ALT:"+str(player[turn].altpoint)+"/"+str(player[turn].altimate),"gray",(60,50,60))
        draw_button(screen,0,130,500,20,"luck:"+str(player[turn].luck),"gray",(60,50,60))
        for i in range(maxplayer):
            if i != turn:
                if player[i].job == 0:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=attacker)
                elif player[i].job == 1:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=healer)
                elif player[i].job == 2:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=sorcerer)
                elif player[i].job == 3:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=defender)
                elif player[i].job == 4:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=luckman)
                

                if player[i].alivestat != 0:
                    draw_button(screen,845,100+i*80,150,40,player[i].name,"gray",(0,0,110),lambda:target_done(i))
                    draw_button(screen,845,140+i*80,150,20,"HP:"+str(player[i].hp),"gray",(0,0,70),lambda:open_information(i))
                
                elif player[i].alivestat == 0:
                    draw_button(screen,845,100+i*80,150,40,player[i].name,"gray",(70,70,70))
                    draw_button(screen,845,140+i*80,150,20,"HP:"+str(player[i].hp),"gray",(70,70,70))

                if target != -1 :
                    se = pygame.image.load("./gatget/se.png")
                    draw_button(screen,845,100+target*80,150,60,"","gray",(0,0,110),image=se)
                    
                

            else:
                draw_button(screen,845,100+i*80,150,40,player[i].name,"gray",(0,110,0))
                draw_button(screen,845,140+i*80,150,20,"HP:"+str(player[i].hp),"gray",(0,0,70))
                if player[i].job == 0:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=attacker)
                elif player[i].job == 1:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=healer)
                elif player[i].job == 2:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=sorcerer)
                elif player[i].job == 3:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=defender)
                elif player[i].job == 4:
                    draw_button(screen,760,80+i*80,80,80,"","blue","green",image=luckman)

        

        

        
        if player[turn].altpoint >= player[turn].altimate:
            draw_button(screen,600,500,100,60,"ALTIMATE",(120,0,70),(200,30,80),select_alt)
        
        else:
            draw_button(screen,600,500,100,60,str(player[turn].altpoint) + "/" + str(player[turn].altimate),(120,0,100),(200,200,200))
        
        while(1):
            if target == -1:
                    target = turn + 1
                    if target == turn:
                        break

                    if target >= maxplayer-1:
                        target = 0
                    
                    if player[target].hp != 0:
                        break
                    if player[target].hp == 0:
                        target = target + 1

                    
            
            else:
                break

        if selectc[0] >= 0 and selectc[1] >= 0:
            draw_button(screen,790,500,200,80,"TURN END",(120,0,200),"pink",lambda:turn_end(target))
            selectc[2] = -1

        
        else:
            draw_button(screen,790,500,200,80,"TURN END","BLUE","GRAY")

        if selectc[2] >= 0 :
            draw_button(screen,790,500,200,80,"TURN END",(120,0,200),"pink",lambda:turn_end(target))
            selectc[0] = -1
            selectc[1] = -1
        
        #else:
            #draw_button(screen,790,500,200,80,"TURN END","BLUE","GRAY")
        
        print(target,player[turn].atpower)

    elif prog == 5:
        print("end")
        


def main():
    global animestat
    global maxplayer
    global animemem
    global prog

    gameflow(prog)
    while True:
        
        pygame.display.update()

        back_ground = pygame.image.load("./screen/fightscreen.png")
        back_ground = pygame.transform.scale(back_ground,(1000,600))
        screen.blit(back_ground,(0,0))
        gameflow(prog)
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

if __name__ == '__main__':
    main()



#キャラクターごとのパラメータ、カードのドロー、カードの選択、アタック、パッシブ,アルティメットを実装した。次は、ターンの制御、画面を作っていく。

#必要な関数は任意の大きさで、任意の位置に、任意の関数を起動できるボタンを作る関数。

#prog 0 はオープニング、1はプレイ人数選択、2はプレイヤーの名前、3はプレイヤーのジョブ、4は戦闘画面、5は結果。


#バグatpowerに正しく値が格納されない。
#ターンの仕組み、ログ、アルティメット、ゲームオーバースクリーン。の作成。


# アタッカーのアルティメットを使えるようにする、ログ、ゲームリザルトの作成。ターンの仕組みは要件等。

#ステータスを最初から完成状態にし、ターンごとに、特定のステータスのみを上昇させていく。また、魔力ステータスの追加。

#カードにカーソルを合わせたとき、カードの情報が出るようにする。

#カードの追加、魔力の回復、HP吸収かなぁ。

#カードの引き直しも必要。
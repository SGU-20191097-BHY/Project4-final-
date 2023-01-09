import numpy as np
import pygame
import os

WINDOW_WIDTH = 1450
WINDOW_HEIGHT = 840

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(180,180,180)
RED=(255,0,0)
GREEN=(0,255,0)
ORANGE=(255,132,0)

pygame.init()

pygame.display.set_caption('20191097 Project4')
screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock=pygame.time.Clock()

#load many many assets
current_path = os.getcwd()
asset_image_path = os.path.join(current_path, "assets/image")
asset_sound_path = os.path.join(current_path, "assets/sound")
img_red_aim = pygame.image.load(os.path.join(asset_image_path, "red_aim.png"))
img_black_aim = pygame.image.load(os.path.join(asset_image_path, "black_aim.png"))
img_AR = pygame.image.load(os.path.join(asset_image_path, "AR.png"))
img_SR = pygame.image.load(os.path.join(asset_image_path, "SR.png"))
img_pistol = pygame.image.load(os.path.join(asset_image_path, "pistol.png"))
img_ARammo = pygame.image.load(os.path.join(asset_image_path, "ARammo.png"))
img_SRammo = pygame.image.load(os.path.join(asset_image_path, "SRammo.png"))
img_medikit = pygame.image.load(os.path.join(asset_image_path, "medikit.png"))
img_zombie_die1=pygame.image.load(os.path.join(asset_image_path, "zombie die 1.png"))
img_zombie_die2=pygame.image.load(os.path.join(asset_image_path, "zombie die 2.png"))
img_zombie_knockback=pygame.image.load(os.path.join(asset_image_path, "zombie knock back.png"))
img_zombie_jump=pygame.image.load(os.path.join(asset_image_path, "zombie jump.png"))
img_zombie_walk1=pygame.image.load(os.path.join(asset_image_path, "zombie walk1.png"))
img_zombie_walk2=pygame.image.load(os.path.join(asset_image_path, "zombie walk2.png"))
img_run1=pygame.image.load(os.path.join(asset_image_path, "run1.png"))
img_run2=pygame.image.load(os.path.join(asset_image_path, "run2.png"))
img_stand=pygame.image.load(os.path.join(asset_image_path, "stand.png"))
img_jump=pygame.image.load(os.path.join(asset_image_path, "jump.png"))
img_AR_arm=pygame.image.load(os.path.join(asset_image_path, "AR arm.png"))
img_SR_arm=pygame.image.load(os.path.join(asset_image_path, "SR arm.png"))
img_pistol_arm=pygame.image.load(os.path.join(asset_image_path, "pistol arm.png"))
img_sky=pygame.image.load(os.path.join(asset_image_path, "sky.png"))
img_building1=pygame.image.load(os.path.join(asset_image_path, "building1.png"))
img_building2=pygame.image.load(os.path.join(asset_image_path, "building2.png"))
img_building3=pygame.image.load(os.path.join(asset_image_path, "building3.png"))
img_building4=pygame.image.load(os.path.join(asset_image_path, "building4.png"))
img_building5=pygame.image.load(os.path.join(asset_image_path, "building5.png"))
img_platform1=pygame.image.load(os.path.join(asset_image_path, "platform1.png"))
img_blood_border=pygame.image.load(os.path.join(asset_image_path, "blood_border.png"))
img_reloading=pygame.image.load(os.path.join(asset_image_path, "reloading.png"))
snd_ouch=pygame.mixer.Sound(os.path.join(asset_sound_path, "ouch.wav"))
snd_nobullet=pygame.mixer.Sound(os.path.join(asset_sound_path, "plzreload.wav"))
snd_ARreload=pygame.mixer.Sound(os.path.join(asset_sound_path, "Arreload.wav"))
snd_SRreload=pygame.mixer.Sound(os.path.join(asset_sound_path, "SRreload.wav"))
snd_pistolreload=pygame.mixer.Sound(os.path.join(asset_sound_path, "pistolreload.wav"))
snd_SRshot=pygame.mixer.Sound(os.path.join(asset_sound_path, "SRshot.wav"))
snd_SRvault=pygame.mixer.Sound(os.path.join(asset_sound_path, "SRvault.wav"))
snd_SRcon=pygame.mixer.Sound(os.path.join(asset_sound_path, "SR_con.wav"))
snd_ARshot=pygame.mixer.Sound(os.path.join(asset_sound_path, "ARshot.wav"))
snd_ARcon=pygame.mixer.Sound(os.path.join(asset_sound_path, "AR_con.wav"))
snd_pistolcon=pygame.mixer.Sound(os.path.join(asset_sound_path, "pistol_con.wav"))
snd_pistolshot=pygame.mixer.Sound(os.path.join(asset_sound_path, "pistolshot.wav"))
snd_zom1=pygame.mixer.Sound(os.path.join(asset_sound_path, "zombie1.wav"))
snd_zom2=pygame.mixer.Sound(os.path.join(asset_sound_path, "zombie2.wav"))
snd_zom3=pygame.mixer.Sound(os.path.join(asset_sound_path, "zombie3.wav"))
snd_zomdie=pygame.mixer.Sound(os.path.join(asset_sound_path, "zombie_die.wav"))
snd_zombite=pygame.mixer.Sound(os.path.join(asset_sound_path, "zombie_bite.wav"))
snd_footstep=pygame.mixer.Sound(os.path.join(asset_sound_path, "footstep.wav"))
snd_scream=pygame.mixer.Sound(os.path.join(asset_sound_path, "scream.wav"))
snd_bgm=pygame.mixer.Sound(os.path.join(asset_sound_path, "bgm.wav"))

#font rendering
UIfont=pygame.font.SysFont('FixedSys',30,False,False)
scorefont=pygame.font.SysFont('FixedSys',60,False,False)
reloadfont=pygame.font.SysFont('FixedSys',100,True,False)
text_reload=reloadfont.render('Reload!(Press R)',True,WHITE)

#play bgm
snd_bgm.play(-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=img_stand
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=200,100
        self.speedx=0
        self.speedy=0
        self.hp=500
        self.last_hit=-600
        self.weapon='pistol'
        self.direction='right'
        self.last_anim=0 #last animated tick
        self.last_anim_frame='run1' #last ani frame
        self.score=0
        self.kills=0
        self.run_sound=-800#last run_sound played tick

    def update(self,):
        airborne=self.calc_grav()#calculate gravity and return True if object is airborne. 
        keystate = pygame.key.get_pressed()
        run=False

        #move left/right
        if keystate[pygame.K_a]:
            self.direction='left'
            self.speedx = -10
            run=True 
        if keystate[pygame.K_d]:
            self.direction='right'
            self.speedx = 10
            run=True
        if run: #running animation
            if airborne==False:
                if self.last_anim_frame=='run2':
                    if self.last_anim+60<pygame.time.get_ticks():
                        self.last_anim=pygame.time.get_ticks()
                        self.last_anim_frame='run1'
                    self.image=img_run1
                elif self.last_anim_frame=='run1':
                    if self.last_anim+60<pygame.time.get_ticks():
                        self.last_anim=pygame.time.get_ticks()
                        self.last_anim_frame='run2'
                    self.image=img_run2           
                if self.run_sound+800<pygame.time.get_ticks():
                    snd_footstep.play()
                    self.run_sound=pygame.time.get_ticks()

        if keystate[pygame.K_w]:#jump
            self.jump()

        #actually move and adjust position not to pass platform or WINDOW
        self.rect.x += self.speedx
        block_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in block_hit_list:
            if self.speedx > 0:
                self.rect.right = block.rect.left
            elif self.speedx < 0:
                self.rect.left = block.rect.right
        if self.rect.left < 0:
            self.rect.left=0
        elif self.rect.right>WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        #actually move and adjust position not to pass platform or WINDOW
        self.rect.y += self.speedy
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            if self.speedy > 0:
                self.rect.bottom = block.rect.top
            elif self.speedy < 0:
                self.rect.top = block.rect.bottom
            self.speedy = 0
        
        #change weapon
        if keystate[pygame.K_1] or keystate[pygame.K_KP_1]:
            self.weapon = 'pistol'
            weapon.reloading=False
        if keystate[pygame.K_2] or keystate[pygame.K_KP_2]:
            self.weapon = 'AR'
            weapon.reloading=False
        if keystate[pygame.K_3] or keystate[pygame.K_KP_3]:
            self.weapon = 'SR'
            weapon.reloading=False

        #stand
        if not (keystate[pygame.K_w] or keystate[pygame.K_d] or keystate[pygame.K_a]):
            self.speedx = 0
            self.image=img_stand

        #flip image by direction
        if self.direction=='left':
             self.image=pygame.transform.flip(self.image,True,False)

        ####Interactions####
        #hit by zombie
        zombie_hit_player=pygame.sprite.spritecollide(self,zombies,False)
        if len(zombie_hit_player)>0:
            self.hit()
        #get medikit
        player_get_med=pygame.sprite.spritecollide(self,medikits,False)
        for med in player_get_med:
            med.kill()
            self.heal()      
        #get ARammo
        player_get_ARammo=pygame.sprite.spritecollide(self,ARammos,False)
        for ARa in player_get_ARammo:
            ARa.kill()
            weapon.ARammo+=30
        #get SRammo
        player_get_SRammo=pygame.sprite.spritecollide(self,SRammos,False)
        for SRa in player_get_SRammo:
            SRa.kill()
            weapon.SRammo+=7

    def calc_grav(self): #calculate gravity and return True if object is airborne. 
        if self.speedy == 0:
            self.speedy = 1
            airborne=False
        else:
            self.speedy += .7
            airborne=True
            self.image=img_jump
        return airborne

    def jump(self):#jump only it's ok to jump
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2    
        if len(platform_hit_list) > 0 or self.rect.bottom >= WINDOW_HEIGHT:
            if self.rect.bottom<=WINDOW_HEIGHT - 2:
                self.speedy = -16
            
    def hit(self):#hurt by zombie
        if self.last_hit + 500 < pygame.time.get_ticks():#0.5 sec hit delay
            self.hp-=25
            self.last_hit = pygame.time.get_ticks()
            snd_ouch.play()
            snd_zombite.play()         
        if self.hp<=0:
            self.hp=0
            self.kill()
            weapon.kill()
            snd_scream.play()

    def heal(self):#heal by medikit
        self.hp+=20
        if self.hp>=500:
            self.hp=500

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.weapon='pistol'
        self.image=img_pistol_arm
        self.rect=self.image.get_rect()
        self.rect.centerx=player.rect.x+player.image.get_width()/2
        self.rect.centery=player.rect.y+player.image.get_height()/4
        self.degree=0

        #magazine's bullet of each weapons
        self.pistolmagazine=12
        self.ARmagazine=30
        self.SRmagazine=7

        #left ammo of each weapons
        self.ARammo=120
        self.SRammo=28

        ##reload
        self.reloading=False #True:now reloading
        self.reload_start=0 #reload started tick

        #last tick of each weapon's fire
        self.last_pistol=0
        self.last_AR=0
        self.last_SR=0

        ##concentration skill
        self.concentration=False #True:now available
        self.last_conc=-2000 #tick of skill last used

    def update(self,):
        #updating weapon image
        if player.weapon=='pistol':
            self.weapon='pistol'
            self.image=img_pistol_arm
        elif player.weapon=='AR':
            self.weapon='AR'
            self.image=img_AR_arm
        else:
            self.weapon='SR'
            self.image=img_SR_arm

        #get mouse position and degree between horizon line(1) from hand and aim line(2)
        m_pos = pygame.mouse.get_pos()
        m_x = m_pos[0]
        m_y = m_pos[1]
          #line2# pygame.draw.line(screen,BLACK,[weapon.rect.centerx,weapon.rect.centery],[m_x,m_y],3)
          #line1# pygame.draw.line(screen,BLACK,[weapon.rect.centerx,weapon.rect.centery],[WINDOW_WIDTH,weapon.rect.centery],3)
        degree=np.arctan(np.abs(m_y-self.rect.centery)/np.abs(m_x-self.rect.centerx))
        degree=np.rad2deg(degree)

        #flip and roatate according to player's sight(mouse position)
        if m_x>=self.rect.centerx:
            if m_y>=self.rect.centery:
                degree*=-1
            self.image=pygame.transform.rotate(self.image,degree)
        else:
            self.image=pygame.transform.flip(self.image,False,True)
            if m_y>=self.rect.centery:
                degree+=180
            else:
                degree=180-degree
            self.image=pygame.transform.rotate(self.image,degree)
        self.degree=degree

        # Move arm image position to player's xy
        self.rect=self.image.get_rect()
        self.rect.center=[player.rect.centerx,player.rect.centery-20]

    def shoot(self): #generate bullet
        if not self.reloading: #cannot shoot while reloading
            now=pygame.time.get_ticks()
            if self.weapon=='pistol':
                if self.last_pistol+400<now:#0.4sec delay
                    if self.pistolmagazine>0:
                        if self.concentration==False: #normal
                            a=Bullet(self)
                            bullets.add(a)
                            self.last_pistol=now
                            self.pistolmagazine -= 1
                            snd_pistolshot.play()
                        else: #skill
                            self.last_pistol=now
                            self.pistolmagazine -= 1
                            aim.concentrate()
                            snd_pistolcon.play()
                    else: #need reload
                        screen.blit(text_reload,[200,100])
                        snd_nobullet.play()

            elif self.weapon=='AR':
                if self.last_AR+100<now: #0.1sec delay
                    if self.ARmagazine>0:
                        if self.concentration==False: #normal
                            a=Bullet(self)
                            bullets.add(a)
                            self.last_AR=now
                            self.ARmagazine -= 1
                            snd_ARshot.play()
                        else: #skill
                            self.last_AR=now
                            self.ARmagazine -= 1
                            aim.concentrate()
                            snd_ARcon.play()
                    else: #need reload
                        screen.blit(text_reload,[200,100])
                        snd_nobullet.play()

            else: #SR
                if self.last_SR+1000<now: #1sec delay
                    if self.SRmagazine>0:#normal
                        a=Bullet(self)
                        bullets.add(a)
                        self.last_SR=now
                        self.SRmagazine -= 1
                        if self.concentration:#skill(+normal bullet)
                            aim.concentrate()
                            snd_SRcon.play()
                            snd_SRvault.play()
                        else: #no skill sound
                            snd_SRshot.play()
                            snd_SRvault.play()
                    else: #need reload
                        screen.blit(text_reload,[200,100])
                        snd_nobullet.play()

    def reload(self): #reload
        now=pygame.time.get_ticks()
        if self.weapon=='pistol':
            if self.pistolmagazine<12:
                if self.reload_start + 1000 < now:
                    self.pistolmagazine=12
                    self.reloading=False
            else:
                self.reloading=False
        elif self.weapon=='AR':
            if self.ARmagazine<30:
                if self.ARammo>0:
                    if self.reload_start + 1000 < now:
                        needed=30-self.ARmagazine
                        if needed>=self.ARammo:
                            self.ARmagazine+=self.ARammo
                            self.ARammo=0
                        else:
                            self.ARmagazine=30
                            self.ARammo-=needed                      
                        self.reloading=False
                else: #no ammo left
                    self.reloading=False
            else: #magazine full
                self.reloading=False
        else:
            if self.SRmagazine<7:
                if self.SRammo>0:
                    if self.reload_start + 1500 < now:
                       needed=7-self.SRmagazine
                       if needed>=self.SRammo:
                            self.SRmagazine+=self.SRammo
                            self.SRammo=0
                       else:
                            self.SRmagazine=7
                            self.SRammo-=needed    
                       self.reloading=False
                else: #no ammo left
                    self.reloading=False
            else: #magazine full
                self.reloading=False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, weapon):
        super().__init__()
        self.weapon=weapon.weapon#get weapon
        self.degree=weapon.degree#get degree

        #bullet:tiny red square
        self.image = pygame.Surface([6, 6])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        #get weapon's position
        self.rect.centerx=weapon.rect.centerx
        self.rect.centery=weapon.rect.centery
        self.dx=0
        self.dy=0
        self.penetrate=1 #give damage to N zombies 
        if self.weapon=='SR':
            self.penetrate=3

    def update(self):
        #bullet move
        self.get_dxy()
        self.rect.centerx+=self.dx
        self.rect.centery+=self.dy

        #bullet and zombie collide
        bullet_hit_zombie=pygame.sprite.spritecollide(self,zombies,False)
        for hit_zombie in bullet_hit_zombie:
            hit_zombie.hit(self)
            self.penetrate-=1
            if self.penetrate==0:
                self.kill()
                break #no multi hit
        
        bullet_hit_platform=pygame.sprite.spritecollide(self,platforms,False)
        if len(bullet_hit_platform)>0:
            self.kill()

        #delete when go out of window
        if self.rect.centerx>WINDOW_WIDTH or self.rect.centerx<0 or self.rect.centery>WINDOW_HEIGHT or self.rect.centery<0:
            self.kill()

    def get_dxy(self):
        #get dxy by cos and sin. For any direction, same speed
        self.dx=np.cos(np.deg2rad(-self.degree))
        self.dy=np.sin(np.deg2rad(-self.degree))
        self.dx*=40
        self.dy*=40

class Zombie(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.hp=100
        self.speedx=0
        self.speedy=0

        #as same as player's
        self.last_anim=0
        self.last_anim_frame='run1'

        #set random spawn point
        spawn=np.random.randint(0,2)
        if spawn==0:
            self.rect.x=1360
            self.rect.y=150
        elif spawn==1:
            self.rect.x=1280
            self.rect.y=425

        self.direction='right'
        self.knockback=False
        self.last_hit=0

    def update(self,player):
        airborne=self.calc_grav()
        if self.knockback:
            if self.last_hit + 250 > pygame.time.get_ticks():
                self.image=img_zombie_knockback
            else:
                self.knockback=False
        else:
            if airborne==False:
                if self.last_anim_frame=='run2':
                    if self.last_anim+90<pygame.time.get_ticks():
                        self.last_anim=pygame.time.get_ticks()
                        self.last_anim_frame='run1'
                    self.image=img_zombie_walk1
                elif self.last_anim_frame=='run1':
                    if self.last_anim+90<pygame.time.get_ticks():
                        self.last_anim=pygame.time.get_ticks()
                        self.last_anim_frame='run2'
                    self.image=img_zombie_walk2

        if player.rect.centerx >= self.rect.centerx:
                    self.speedx=3
                    self.direction='right'
        else:
                    self.speedx=-3
                    self.direction='left'

        self.rect.x+=self.speedx

        block_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in block_hit_list:
            if not self.knockback:
                if self.speedx > 0:
                    self.rect.right = block.rect.left
                elif self.speedx < 0:
                    self.rect.left = block.rect.right
                self.jump()
            else:
                if self.speedx > 0:
                    self.rect.left = block.rect.right
                elif self.speedx < 0:
                    self.rect.right = block.rect.left

        growl=np.random.randint(0,5000)
        if growl==1:
            snd_zom1.play()
        elif growl==2:
            snd_zom2.play()
        elif growl==3:
            snd_zom3.play()



        self.rect.y += self.speedy

        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.speedy > 0:
                self.rect.bottom = block.rect.top
            elif self.speedy < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.speedy = 0

        if self.direction=='right':
            self.image=pygame.transform.flip(self.image,True,False)
        
        if gameover:
            self.kill()

    def calc_grav(self):
        if self.speedy == 0:
            self.speedy = 1
            airborne=False
        else:
            self.speedy += .7
            self.image=img_zombie_jump
            airborne=True

        return airborne

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= WINDOW_HEIGHT:
            if self.rect.bottom<=WINDOW_HEIGHT - 2:
                self.speedy = -15


    def hit(self,bullet):
        if bullet.weapon=='pistol':
            self.hp-=40
            player.score+=40
        elif bullet.weapon=='AR':
            self.hp-=30
            player.score+=30
        else:
            self.hp-=100
            player.score+=100

        self.last_hit=pygame.time.get_ticks()
        self.knockback=True

        if self.direction=='right':
            self.rect.x -= 40
        else:
            self.rect.x += 40

        if self.hp<=0:
            player.score+=self.hp
            z=Zombiedie(self)
            all_sprites.add(z)
            player.score+=100
            player.kills+=1

            drop=np.random.randint(0,40)
            if drop==0:
                ss=SRammo(self)
                SRammos.add(ss)
                all_sprites.add(ss)
            elif drop==1 or drop==2:
                mm=ARammo(self)
                ARammos.add(mm)
                all_sprites.add(mm)
            elif drop==3:
                m=Medikit(self)
                medikits.add(m)
                all_sprites.add(m)
            self.kill()
            snd_zomdie.play()

class Zombiedie(pygame.sprite.Sprite):#zombie dying animation
    def __init__(self,zombie):
        super().__init__()
        self.image=img_zombie_die1
        self.rect=self.image.get_rect()
        self.direction=zombie.direction
        if self.direction=='right':
            self.rect.x=zombie.rect.left
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.rect.x=zombie.rect.left

        self.rect.bottom=zombie.rect.bottom
        self.last_anim=pygame.time.get_ticks()
        self.frame=1
        self.location=[self.rect.centerx, self.rect.bottom]
        self.dy=0

    def update(self):
        self.dy+=.7
        self.rect.bottom += self.dy
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            self.rect.bottom = block.rect.top
            self.dy = 0

        if self.frame==1:
            if self.last_anim+300<pygame.time.get_ticks():
                self.image=img_zombie_die2
                if self.direction=='right':
                    self.image=pygame.transform.flip(self.image,True,False)
                self.rect=self.image.get_rect()
                self.rect.bottom=self.location[1]
                self.rect.centerx=self.location[0]
                self.frame=2
                self.last_anim=pygame.time.get_ticks()

        elif self.frame==2:
            if self.last_anim+300<pygame.time.get_ticks():
                self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x,y,img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class SRammo(pygame.sprite.Sprite):
    def __init__(self, zombie):
        super().__init__()
        self.image=img_SRammo
        self.rect=self.image.get_rect()
        self.rect.center=zombie.rect.center
        self.dy=-4

    def update(self):
        self.dy+=.7
        self.rect.bottom += self.dy

        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            self.rect.bottom = block.rect.top
            self.dy = 0

        if gameover:
            self.kill()

class ARammo(pygame.sprite.Sprite):
    def __init__(self, zombie):
        super().__init__()
        self.image=img_ARammo
        self.rect=self.image.get_rect()
        self.rect.center=zombie.rect.center
        self.dy=-4

    def update(self):
        self.dy+=.7
        self.rect.bottom += self.dy

        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            self.rect.bottom = block.rect.top
            self.dy = 0
        
        if gameover:
            self.kill()

class Medikit(pygame.sprite.Sprite):
    def __init__(self, zombie):
        super().__init__()
        self.image=img_medikit
        self.rect=self.image.get_rect()
        self.rect.center=zombie.rect.center
        self.dy=-4

    def update(self):
        self.dy+=.7
        self.rect.bottom += self.dy

        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in platform_hit_list:
            self.rect.bottom = block.rect.top
            self.dy = 0
        
        if gameover:
            self.kill()

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=img_black_aim
        self.rect=self.image.get_rect()
        
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        zombie_aimed = pygame.sprite.spritecollide(self, zombies, False)
        if len(zombie_aimed)>0:
            if weapon.last_conc+1000<pygame.time.get_ticks():
                self.image=img_red_aim
                weapon.concentration=True
            else:
                self.image=img_black_aim
                weapon.concentration=False
        else:
            weapon.concentration=False
            self.image=img_black_aim

    def concentrate(self):
        zombie_aimed = pygame.sprite.spritecollide(self, zombies, False)
        for zomb in zombie_aimed:
            pygame.draw.line(screen,ORANGE,weapon.rect.center,pygame.mouse.get_pos(),6)
            pygame.draw.line(screen,RED,weapon.rect.center,pygame.mouse.get_pos(),4)     
            zomb.kill()
            player.kills+=1
            zd=Zombiedie(zomb)
            all_sprites.add(zd)
            player.score+=150
            player.score+=zomb.hp
            weapon.concentration=False
            weapon.last_conc=pygame.time.get_ticks()
            break

zombies=pygame.sprite.Group()
platforms=pygame.sprite.Group()
bullets=pygame.sprite.Group()
medikits=pygame.sprite.Group()
ARammos=pygame.sprite.Group()
SRammos=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

#add platforms
p1=Platform(0,320,img_building1)
p2=Platform(320,460,img_building2)
p3=Platform(725,540,img_building3)
p4=Platform(940,270,img_platform1)
for i in [p1,p2,p3,p4]:
    platforms.add(i)
    all_sprites.add(i)

player=Player()
weapon=Weapon(player)
aim=Aim()
all_sprites.add(player)
all_sprites.add(weapon)
all_sprites.add(aim)

#text render
text_title=scorefont.render("Concentrate to Survive",True,BLACK)
text_score=UIfont.render("Score :",True,BLACK)
text_kills=UIfont.render("Kills :",True,BLACK)
text_pressstart=scorefont.render("Press Space to start",True,BLACK)

is_shooting=False #mouse click
gameover=True #one game
lastscore=0 #for title last score
lastSpawn=0 #for zombie spawn
done=False #for pygame loop

while not done:
    #draw basic graphics(backgrounds)
    screen.fill(WHITE)
    screen.blit(img_sky,[0,0])
    screen.blit(img_building4,[940,270])
    screen.blit(img_building5,[1173,0])
    pygame.draw.line(screen,BLACK,[0,700],[1450,700],10)
    text_lastscore=scorefont.render(str(lastscore),True,BLACK)#render last score

    if gameover:#gameover display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameover=False #game start
        screen.blit(text_title,[500,300])
        screen.blit(text_score,[500,400])
        screen.blit(text_lastscore,[590,390])
        screen.blit(text_pressstart,[520,750])
        all_sprites.update()
        all_sprites.draw(screen)  
    else: #game started
        now=pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_shooting=True
            elif event.type == pygame.MOUSEBUTTONUP:
                is_shooting=False
            elif event.type == pygame.KEYDOWN and weapon.reloading==False:#when not reloading
                if event.key==pygame.K_r:
                    weapon.reload_start=pygame.time.get_ticks()
                    if player.weapon=='pistol':
                        snd_pistolreload.play()
                    elif player.weapon=='AR' and weapon.ARammo>0:
                        snd_ARreload.play()
                    elif player.weapon=='SR' and weapon.SRammo>0:
                        snd_SRreload.play()            
                    weapon.reloading=True

        if weapon.reloading==True:
            weapon.reload()

        all_sprites.update()

        zombies.update(player)
        zombies.draw(screen)
        bullets.update()
        bullets.draw(screen)
        all_sprites.draw(screen)

        if is_shooting:
            weapon.shoot()

        if lastSpawn+500<now: #spawn zombie every 0.5sec
            lastSpawn=pygame.time.get_ticks()
            a=Zombie(img_zombie_walk1)
            zombies.add(a)

        pygame.draw.line(screen,BLACK,[0,700],[1450,700],10)#draw line between UI and board

        if player.last_hit+300>pygame.time.get_ticks(): #blood border effect
            screen.blit(img_blood_border,[0,0])

        #Indicate HP info
        text_hp=UIfont.render("HP",True,BLACK)
        text_playerHP=UIfont.render(str(player.hp)+"/500",True,BLACK)
        pygame.draw.rect(screen,RED,[70,780,300*player.hp/500,30],0)
        pygame.draw.rect(screen,BLACK,[70,780,300,30],5)
        screen.blit(text_hp,[30,785])
        screen.blit(text_playerHP,[380,790])

        #Indicate score info
        text_currnetscore=scorefont.render(str(player.score),True,BLACK)
        screen.blit(text_score,[30,730])
        screen.blit(text_currnetscore,[120,720])

        #Indicate kills info
        text_currnetkills=scorefont.render(str(player.kills),True,BLACK)
        screen.blit(text_kills,[380,730])
        screen.blit(text_currnetkills,[470,720])

        #Indicate weapon info
            #weapon images
        screen.blit(img_pistol,[600,720])
        screen.blit(img_AR,[900,720])
        screen.blit(img_SR,[1200,720])
            #weapon ammo
        text_pistol=UIfont.render(str(weapon.pistolmagazine)+'/Infinite',True,BLACK)
        screen.blit(text_pistol,[570,800])
        text_AR=UIfont.render(str(weapon.ARmagazine)+'/'+str(weapon.ARammo),True,BLACK)
        screen.blit(text_AR,[870,800])
        text_SR=UIfont.render(str(weapon.SRmagazine)+'/'+str(weapon.SRammo),True,BLACK)
        screen.blit(text_SR,[1170,800])
            #show selected weapon and reloading status
        now=pygame.time.get_ticks()
        if player.weapon=='pistol':
            if weapon.reloading:
                screen.blit(img_reloading,[550,706])
                pygame.draw.rect(screen,GREEN,[600,795,200*(now-weapon.reload_start)/1000,20])
                pygame.draw.rect(screen,WHITE,[600,795,200,20],5)
            pygame.draw.rect(screen,GREEN,[550,706,300,125],6)
        elif player.weapon=='AR':
            if weapon.reloading:
                screen.blit(img_reloading,[850,706])
                pygame.draw.rect(screen,GREEN,[900,795,200*(now-weapon.reload_start)/1000,20])
                pygame.draw.rect(screen,WHITE,[900,795,200,20],5)
            pygame.draw.rect(screen,GREEN,[850,706,300,125],6)
        else:
            if weapon.reloading:
                screen.blit(img_reloading,[1150,706])
                pygame.draw.rect(screen,GREEN,[1200,795,200*(now-weapon.reload_start)/1500,20])
                pygame.draw.rect(screen,WHITE,[1200,795,200,20],5)
            pygame.draw.rect(screen,GREEN,[1150,706,300,125],6)

        #Indicate concentrate cooldown
        if weapon.last_conc+990>now:
            pygame.draw.rect(screen,RED,[aim.rect.x,aim.rect.bottom,35*(now-weapon.last_conc)/990,7],0)
        else:
            pygame.draw.rect(screen,GREEN,[aim.rect.x,aim.rect.bottom,35,7],0)
        pygame.draw.rect(screen,WHITE,[aim.rect.x,aim.rect.bottom,35,10],3)

        if player.hp<=0:#init sprites and go to gameover display
            lastscore=player.score#save last score. will be displayed on gameover display
            zombies=pygame.sprite.Group()
            bullets=pygame.sprite.Group()
            SRammos=pygame.sprite.Group()
            ARammos=pygame.sprite.Group()
            medikits=pygame.sprite.Group()
            player=Player()
            weapon=Weapon(player)
            all_sprites.add(player)
            all_sprites.add(weapon)
            gameover=True
            zombies.update(player)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

from bangtal import *
import random

###_____________________배경 설정________________________###
home=Scene("", "이미지/배경/배경_0.png")
scene0=Scene("시작하기 전 잠깐!", "이미지/배경/설명.png")
scene1=Scene("", "이미지/배경/배경_0.png")
ending=Scene("", "이미지/엔딩/암막.png")

gameover=Object("이미지/배경/게임종료.png")

setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

class ground(Object):
    def __init__(self, scene):
        super().__init__("이미지/배경/땅.png")

        self.locate(scene, 0, 0)
        self.show()

home_ground=ground(home)
scene1_ground=ground(scene1)

background_image=["이미지/배경/배경_0.png","이미지/배경/배경_1.png","이미지/배경/배경_2.png","이미지/배경/배경_3.png","이미지/배경/배경_4.png","이미지/배경/배경_5.png","이미지/배경/배경_6.png","이미지/배경/배경_7.png","이미지/배경/배경_8.png","이미지/배경/배경_9.png","이미지/배경/배경_10.png","이미지/배경/배경_11.png","이미지/배경/배경_12.png","이미지/배경/배경_13.png","이미지/배경/배경_14.png","이미지/배경/배경_15.png","이미지/배경/배경_16.png","이미지/배경/배경_17.png","이미지/배경/배경_18.png","이미지/배경/배경_19.png","이미지/배경/배경_20.png","이미지/배경/배경_21.png","이미지/배경/배경_22.png","이미지/배경/배경_23.png","이미지/배경/배경_24.png","이미지/배경/배경_25.png","이미지/배경/배경_26.png","이미지/배경/배경_27.png","이미지/배경/배경_28.png","이미지/배경/배경_29.png","이미지/배경/배경_30.png","이미지/배경/배경_31.png","이미지/배경/배경_32.png","이미지/배경/배경_33.png","이미지/배경/배경_34.png","이미지/배경/배경_35.png","이미지/배경/배경_36.png","이미지/배경/배경_37.png","이미지/배경/배경_38.png","이미지/배경/배경_39.png","이미지/배경/배경_40.png"]
now_background=0

background_timer=Timer(0.05)
background_timer.start()
def background_chainge():
    global now_background

    if now_background<40:
        now_background+=1
    else:
        now_background=0

    home.setImage(background_image[now_background])
    scene1.setImage(background_image[now_background])

    background_timer.set(0.05)
    background_timer.start()
background_timer.onTimeout=background_chainge

#__________________home_____________________#
banner=Object("이미지/배경/라마키우기.png")
banner.locate(home, 390, 470)
banner.show()

play=Object("이미지/배경/시작하기.png")
play.locate(home, 540, 320)
play.setScale(0.5)
play.show()

def enter_scene0(x, y, action):
    scene0.enter()
play.onMouseAction=enter_scene0

#__________________scene0_____________________#
normal=Object("이미지/배경/노말모드.png")
normal.locate(scene0, 80, 540)
normal.show()

def normal_mode(x, y, action):         #-----------본격적인 게임시작------------#
    scene1.enter()
    setGameOption(GameOption.INVENTORY_BUTTON, True)

    sad_timer.start()
    hungry_timer.start()
    clean_timer.start()
    dirty_timer.start()
    poop_timer.start()
    fruit_timer.start()
    lama_motion_timer.start()
    lama_move_timer.start()
normal.onMouseAction=normal_mode

#________행복/포만/청결________#
sad=4
happy_image=["이미지/행복도/행복0.png","이미지/행복도/행복1.png","이미지/행복도/행복2.png","이미지/행복도/행복3.png","이미지/행복도/행복4.png","이미지/행복도/행복5.png","이미지/행복도/행복6.png"]
happy=Object(happy_image[sad])
happy.locate(scene1, 285, 660)
happy.show()

hungry=4
food_image=["이미지/포만감/포만0.png","이미지/포만감/포만1.png","이미지/포만감/포만2.png","이미지/포만감/포만3.png","이미지/포만감/포만4.png","이미지/포만감/포만5.png","이미지/포만감/포만6.png"]
food=Object(food_image[hungry])
food.locate(scene1, 540, 660)
food.show()

dirty=4
clean_image=["이미지/청결도/청결0.png","이미지/청결도/청결1.png","이미지/청결도/청결2.png","이미지/청결도/청결3.png","이미지/청결도/청결4.png","이미지/청결도/청결5.png","이미지/청결도/청결6.png"]
clean=Object(clean_image[dirty])
clean.locate(scene1, 795, 660)
clean.show()


###_____________________캐릭터 설정________________________###
lama_location=[620, 50]
lama_velocity=[[-12, -7, 0, 7, 12],[-10, -5, 0, 5, 10],[-8, -3, 0, 3, 8]]
now_motion=0
now_left=False
now_level=0
lama_image=[[["이미지/캐릭터/1단계/1단계_라마_오른쪽_0.png", "이미지/캐릭터/1단계/1단계_라마_오른쪽_1.png","이미지/캐릭터/1단계/1단계_라마_오른쪽_2.png","이미지/캐릭터/1단계/1단계_라마_오른쪽_3.png","이미지/캐릭터/1단계/1단계_라마_오른쪽_4.png","이미지/캐릭터/1단계/1단계_라마_오른쪽_5.png"],["이미지/캐릭터/1단계/1단계_라마_왼쪽_0.png","이미지/캐릭터/1단계/1단계_라마_왼쪽_1.png","이미지/캐릭터/1단계/1단계_라마_왼쪽_2.png","이미지/캐릭터/1단계/1단계_라마_왼쪽_3.png","이미지/캐릭터/1단계/1단계_라마_왼쪽_4.png","이미지/캐릭터/1단계/1단계_라마_왼쪽_5.png"]],[["이미지/캐릭터/2단계/2단계_라마_오른쪽_0.png", "이미지/캐릭터/2단계/2단계_라마_오른쪽_1.png","이미지/캐릭터/2단계/2단계_라마_오른쪽_2.png","이미지/캐릭터/2단계/2단계_라마_오른쪽_3.png","이미지/캐릭터/2단계/2단계_라마_오른쪽_4.png","이미지/캐릭터/2단계/2단계_라마_오른쪽_5.png"],["이미지/캐릭터/2단계/2단계_라마_왼쪽_0.png","이미지/캐릭터/2단계/2단계_라마_왼쪽_1.png","이미지/캐릭터/2단계/2단계_라마_왼쪽_2.png","이미지/캐릭터/2단계/2단계_라마_왼쪽_3.png","이미지/캐릭터/2단계/2단계_라마_왼쪽_4.png","이미지/캐릭터/2단계/2단계_라마_왼쪽_5.png"]],[["이미지/캐릭터/3단계/3단계_라마_오른쪽_0.png", "이미지/캐릭터/3단계/3단계_라마_오른쪽_1.png","이미지/캐릭터/3단계/3단계_라마_오른쪽_2.png","이미지/캐릭터/3단계/3단계_라마_오른쪽_3.png","이미지/캐릭터/3단계/3단계_라마_오른쪽_4.png","이미지/캐릭터/3단계/3단계_라마_오른쪽_5.png"],["이미지/캐릭터/3단계/3단계_라마_왼쪽_0.png","이미지/캐릭터/3단계/3단계_라마_왼쪽_1.png","이미지/캐릭터/3단계/3단계_라마_왼쪽_2.png","이미지/캐릭터/3단계/3단계_라마_왼쪽_3.png","이미지/캐릭터/3단계/3단계_라마_왼쪽_4.png","이미지/캐릭터/3단계/3단계_라마_왼쪽_5.png"]]]

lama=Object(lama_image[now_level][now_left][now_motion])
lama.locate(scene1, lama_location[0], lama_location[1])
lama.show()

#________라마 모습________#
motion_level=[0.05, 0.08, 0.1]

lama_motion_timer=Timer(motion_level[now_level])
def motion_chainge():
    global now_motion

    if now_motion<5:
        now_motion+=1
    else:
        now_motion=0

    lama.setImage(lama_image[now_level][now_left][now_motion])
    lama.locate(scene1, lama_location[0], lama_location[1])
    lama.show()

    lama_motion_timer.set(motion_level[now_level])
    lama_motion_timer.start()
lama_motion_timer.onTimeout=motion_chainge

#________라마 움직임________#
on_move=True
step_count=10
v_x=lama_velocity[now_level][3]
v_y=lama_velocity[now_level][3]
def move():
    global on_move
    global lama_location
    global step_count
    global v_x
    global v_y
    global now_left
    step_count-=1

    if lama_location[0]+v_x<50:
        v_x*=-1
        now_left=False
    elif lama_location[0]+v_x>1150:
        v_x*=-1
        now_left=True
    elif lama_location[1]+v_y<0 or lama_location[1]+v_y>250:
        v_y*=-1
    
    lama_location[0]+=v_x
    lama_location[1]+=v_y
    lama.locate(scene1, lama_location[0], lama_location[1])
    lama.show()

    if step_count==0:
        on_move=False
        step_count=random.randint(1, 20)

def stop():
    global on_move
    global v_x
    global v_y
    global step_count
    global now_left
    step_count-=1
    if step_count==0:
        on_move=True
        step_count=random.randint(10, 40)
        v_x=lama_velocity[now_level][random.randint(0, 4)]
        v_y=lama_velocity[now_level][random.randint(0, 4)]
        if v_x<0:
            now_left=True
        else:
            now_left=False

lama_move_timer=Timer(0.2)
def lama_move_timer_onTimeout():        ## 이동하면서 성공/실패 여부 실시간으로 체크
    global now_level
    global sad
    global hungry
    global dirty
    global bgm_scene1

    if  sad==0 and hungry==0 and dirty==0:
        if now_level==2:        #<--------------------성공 조건
            setGameOption(GameOption.INVENTORY_BUTTON, False)
            complete()

        else:
            now_level+=1;
            sad=4
            hungry=4
            dirty=4

            happy.setImage(happy_image[sad])
            happy.show()
            food.setImage(food_image[hungry])
            food.show()
            clean.setImage(clean_image[dirty])
            clean.show()

            sad_timer.set(20)
            hungry_timer.set(20)
            clean_timer.set(10)
            dirty_timer.set(20)

            lama_move_timer.start()

            bgm_scene1.stop()
            bgm_scene1=Sound(bgm_level[now_level])  #<-----bgm 전환(2차 커밋)
            bgm_scene1.play(True)

    elif sad==6 or hungry==6 or dirty==6: #<--------------------실패조건
        fail()

    else:
        if on_move:
            move()
        else:
            stop()
        lama_move_timer.set(0.2)
        lama_move_timer.start()
lama_move_timer.onTimeout=lama_move_timer_onTimeout


###________행복/포만/청결 이펙트+이벤트 함수________###
heart=Object("이미지/행복도/하트_이펙트.png")
hand=Object("이미지/행복도/손.png")
hand.pick()

fruit_location=[[520, 293],[942, 345],[331, 309],[85, 310],[1155, 310]]
fruit=Object("이미지/포만감/과일.png")
fruit_random=random.randint(0, 4)
fruit.locate(scene1, fruit_location[fruit_random][0], fruit_location[fruit_random][1])
fruit.show()

poop=Object("이미지/청결도/똥.png")
broom=Object("이미지/청결도/빗자루.png")
broom.pick()

#_________________하트 이펙트________________#
heart_effect_timer=Timer(0.1)
heart_effect_count=10
heart_effect_now=False
heart_effect_location=[0, 0]
def heart_effect():
    global heart_effect_timer
    global heart_effect_count
    global heart_effect_now
    global heart_effect_location

    heart.locate(scene1, heart_effect_location[0], heart_effect_location[1])
    heart.show()

    heart_effect_count-=1

    if heart_effect_count>0:
        heart_effect_location[1]+=7
        heart_effect_timer.set(0.1)
        heart_effect_timer.start()
    else:
        heart_effect_now=False
        heart.hide()    
heart_effect_timer.onTimeout=heart_effect

#_________________행복도 관련________________#
sound_gage=Sound("음악/게이지.mp3")

sad_timer=Timer(20)
def sad_timer_onTimeout():
    global sad

    sad+=1
    happy.setImage(happy_image[sad])
    happy.show()
    sound_gage.play(False)

    sad_timer.set(20)
    sad_timer.start()
sad_timer.onTimeout=sad_timer_onTimeout

sad_cooltimer=Timer(0)
def sad_cooltimer_onTimeout():
    sad_timer.start()
sad_cooltimer.onTimeout=sad_cooltimer_onTimeout

#_________________포만감 관련________________#
hungry_timer=Timer(20)
def hungry_timer_onTimeout():
    global hungry

    hungry+=1
    food.setImage(food_image[hungry])
    food.show()
    sound_gage.play(False)

    hungry_timer.set(20)
    hungry_timer.start()
hungry_timer.onTimeout=hungry_timer_onTimeout

hungry_cooltimer=Timer(0)
def hungry_cooltimer_onTimeout():
    hungry_timer.start()
hungry_cooltimer.onTimeout=hungry_cooltimer_onTimeout

sound_lamatouch=Sound("음악/라마터치.mp3")
fruit_timer=Timer(0)
handling_count=0
def feed_and_handling(x, y, action):         ##쓰다듬기&먹이주기 같이 있음
    global heart_effect_timer
    global heart_effect_count
    global heart_effect_now
    global heart_effect_location
    global lama_location
    global handling_count
    global sad
    global hungry

    if fruit.inHand() and hungry>0:
        sound_lamatouch.play(False)
        if hungry==1:
            hungry-=1
            food.setImage(food_image[hungry])
            food.show()
        else:
            hungry-=2
            food.setImage(food_image[hungry])
            food.show()

        heart_effect_count=10
        heart_effect_now=True
        heart_effect_location[0]=lama_location[0]
        heart_effect_location[1]=lama_location[1]
        heart_effect_timer.start()

        fruit.drop()
        fruit.hide()

        fruit_timer.set(20)
        fruit_timer.start()
        
        hungry_timer.stop()
        hungry_cooltimer.set(10)
        hungry_cooltimer.start()

    elif hand.inHand() and heart_effect_now==False and sad>0:
        sound_lamatouch.play(False)
        handling_count+=1
        if handling_count%5==0:
            sad-=1
            happy.setImage(happy_image[sad])
            happy.show()
            sound_gage.play(False)

        heart_effect_count=10
        heart_effect_now=True
        heart_effect_location[0]=lama_location[0]
        heart_effect_location[1]=lama_location[1]
        heart_effect_timer.start()

        sad_timer.stop()
        sad_cooltimer.set(10)
        sad_cooltimer.start()
lama.onMouseAction=feed_and_handling

def fruit_pick(x, y, action):
    fruit.pick()
    sound_pick.play(False)
fruit.onMouseAction=fruit_pick

sound_respon=Sound("음악/열매.mp3")
def fruit_respon():
    global fruit_random

    fruit_random=random.randint(0, 4)
    fruit.locate(scene1, fruit_location[fruit_random][0], fruit_location[fruit_random][1])
    fruit.show()
    sound_respon.play(False)
fruit_timer.onTimeout=fruit_respon

#_________________청결도 관련________________#
clean_timer=Timer(10)
def clean_timer_onTimeout():
    global dirty

    if dirty>0:
        dirty-=1
        clean.setImage(clean_image[dirty])
        clean.show()
        sound_gage.play(False)
        
    clean_timer.set(10)
    clean_timer.start()
clean_timer.onTimeout=clean_timer_onTimeout

dirty_timer=Timer(20)
def dirty_timer_onTimeout():
    global dirty

    if dirty<5:
        dirty+=1
        clean.setImage(clean_image[dirty])
        clean.show()
        sound_gage.play(False)
        
    dirty_timer.set(20)
    dirty_timer.start()
dirty_timer.onTimeout=dirty_timer_onTimeout

sound_poop=Sound("음악/배변.mp3")
poop_timer=Timer(20)
def poop_timer_onTimeout():
    poop.locate(scene1, lama_location[0], lama_location[1])
    poop.show()
    sound_poop.play(False)

    clean_timer.stop()
    dirty_timer.set(20)
    dirty_timer.start()
poop_timer.onTimeout=poop_timer_onTimeout

sound_pick=Sound("음악/줍기.mp3")
def brooming(x, y, action):
    if broom.inHand():
        poop.hide()
        sound_pick.play(False)
        clean_timer.start()
        dirty_timer.stop()

        poop_timer.set(20)
        poop_timer.start()
poop.onMouseAction=brooming

###_____________________________________________________게임 시작 및 종료____________________________________________________________###
ending_image=["이미지/엔딩/heaven_0.png","이미지/엔딩/heaven_1.png","이미지/엔딩/heaven_2.png","이미지/엔딩/heaven_3.png","이미지/엔딩/heaven_4.png","이미지/엔딩/heaven_5.png","이미지/엔딩/heaven_6.png","이미지/엔딩/heaven_7.png","이미지/엔딩/heaven_8.png","이미지/엔딩/heaven_9.png","이미지/엔딩/heaven_10.png","이미지/엔딩/heaven_11.png"]
now_ending=0

angel_image=["이미지/캐릭터/라마_천사_0.png", "이미지/캐릭터/라마_천사_1.png"]
angel_location=[627, 0]
ending_angel=Object(angel_image[0])
angel_scale=1
now_angel=False

ending_message=Object("이미지/엔딩/엔딩메세지.png")
ending_message.locate(ending, 203, 214)

#_________________성공 시 엔딩 관련_______________#
def complete():
    sad_timer.stop()
    sad_cooltimer.stop()
    hungry_timer.stop()
    hungry_cooltimer.stop()
    clean_timer.stop()
    dirty_timer.stop()
    poop_timer.stop()
    fruit_timer.stop()
    lama_motion_timer.stop()
    heart_effect_timer.stop()

    ending.enter()
    ending.setLight(0)
    ending_fade.start()
    ending_message.show()
now_ending_light=0
ending.setLight(now_ending_light)

fade_cnt=0
ending_fade=Timer(0.1)
def fade_io():
    global now_ending_light
    global fade_cnt
    fade_cnt+=1

    if fade_cnt<=10:
        now_ending_light+=0.1
    elif fade_cnt>90:
        if fade_cnt==100:
            ending.setLight(1)
            ending_message.hide()
            ending_timer.start()
            angel_timer.start()
            return
        now_ending_light-=0.1

    ending.setLight(now_ending_light)

    ending_fade.set(0.1)
    ending_fade.start()
ending_fade.onTimeout=fade_io

ending_timer=Timer(0.05)
def ending_background():
    global now_ending

    if now_ending<11:
        now_ending+=1
    else:
        now_ending=0

    ending.setImage(ending_image[now_ending])

    ending_timer.set(0.05)
    ending_timer.start()
ending_timer.onTimeout=ending_background

angel_timer=Timer(0.1)
def angel_timer_onTimeout():
    global angel_location
    global now_angel
    global angel_scale
    global bgm_ending

    if angel_location[1]<450:
        angel_scale*=0.99
    else:
        angel_scale*=0.98

    angel_location[1]+=5
    
    if angel_location[1]>590:
        ending.setImage("이미지/엔딩/암막.png")
        ending_angel.hide()
        ending_timer.stop()
        bgm_ending.stop()
        bgm_ending=Sound("음악/엔딩크레딧.mp3")  #<-----bgm 전환(2차 커밋)
        bgm_ending.play(True)

        ending_credit_timer.start()
    else:
        if now_angel:
            now_angel=False
        else:
            now_angel=True

        ending_angel.setScale(angel_scale)
        ending_angel.locate(ending, angel_location[0], angel_location[1])
        ending_angel.setImage(angel_image[now_angel])
        ending_angel.show()
    
        angel_timer.set(0.1)
        angel_timer.start()
angel_timer.onTimeout=angel_timer_onTimeout

ending_credit=Object("이미지/엔딩/엔딩크레딧.png")
ending_credit_location=[0, -1053]
ending_credit.locate(ending, ending_credit_location[0], ending_credit_location[1])
ending_credit_timer=Timer(0.05)
def ending_credit_rollup():
    global ending_credit_location

    if ending_credit_location[1]>740:
        endGame()
    
    else:
        ending_credit_location[1]+=3
        ending_credit.locate(ending, ending_credit_location[0], ending_credit_location[1])
        ending_credit.show()

        ending_credit_timer.set(0.05)
        ending_credit_timer.start()
ending_credit_timer.onTimeout=ending_credit_rollup

#_________________실패 관련_______________#
def fail():
    lama.setImage("이미지/캐릭터/무덤.png")
    lama.locate(scene1, lama_location[0], lama_location[1])
    lama.show()

    sad_timer.stop()
    sad_cooltimer.stop()
    hungry_timer.stop()
    hungry_cooltimer.stop()
    clean_timer.stop()
    dirty_timer.stop()
    poop_timer.stop()
    fruit_timer.stop()
    lama_motion_timer.stop()
    heart_effect_timer.stop()
    background_timer.stop()
    bgm_scene1.stop()

    gameover.locate(scene1, 0, 0)
    gameover.show()

def game_over(x, y, action):
    endGame()
gameover.onMouseAction=game_over

##_________________배경음악(2차 커밋 추가내용)_________________##

bgm_intro=Sound("음악/인트로.mp3")
def home_onEnter():
    bgm_intro.play(True)
home.onEnter=home_onEnter

bgm_scene0=Sound("음악/메뉴.mp3")
def scene0_onEnter():
    bgm_intro.stop()
    bgm_scene0.play(True)
scene0.onEnter=scene0_onEnter

bgm_level=["음악/무지개시티.mp3","음악/회색시티.mp3","음악/태초마을.mp3"]
bgm_scene1=Sound(bgm_level[now_level])
def scene1_onEnter():
    bgm_scene0.stop()
    bgm_scene1.play(True)
scene1.onEnter=scene1_onEnter

bgm_ending=Sound("음악/The End.mp3")
def ending_onEnter():
    bgm_scene1.stop()
    bgm_ending.play(True)
ending.onEnter=ending_onEnter

startGame(home)
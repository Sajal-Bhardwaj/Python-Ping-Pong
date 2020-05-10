import pygame
from pygame import *
import time
from pygame import mixer
import win32com.client
speaker=win32com.client.Dispatch("SAPI.Spvoice")

#Initialising Pygame
pygame.init()
icon=pygame.image.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ping_pong.png")
pygame.display.set_icon(icon)
#Initialising Mixer
mixer.init()

font=pygame.font.Font("freesansbold.ttf",24)
large_font=pygame.font.Font("freesansbold.ttf",62)
# Setting Window height and width
win_width=1020
win_height=720
# Creating the Window
win=pygame.display.set_mode((win_width,win_height))
# Title for Window
pygame.display.set_caption("Ping Pong")

# Background image
bg=pygame.image.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\pong5.jpg")
# Startup image
s_up=pygame.image.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\pong4.jpg")
# Game over image
g_o=pygame.image.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\pong3.jpg")

#color pallet
red=(255,0,0)
oreangered=(255,69,0)
chartreuse1=(127,255,0)
firebrickred=(238,44,44)
goldenrod2=(238,180,34)
green=(0,255,0)
blue=(0,0,255)
darkorchid1=(191,62,255)
black=(0,0,0)
white=(255,255,255)

# Function to draw messages
def msg(message,color,x,y):
    mesg=font.render(message,True,color)
    win.blit(mesg,[x,y])

#Large Font
def lgmsg(message,color,x,y):
    mesg=large_font.render(message,True,color)
    win.blit(mesg,[x,y])

def start():
    intro=True
    while intro:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_RETURN:
                    intro=False


        #setting the Startup image
        win.blit(s_up,(0,0))

        lgmsg(("Ping Pong"),oreangered,win_width/2-150,win_height/2-200)
        msg(("It's a classic Ping Pong, on startup press enter for ball to move "),green,win_width/2-350,win_height/2+50)
        msg(("Press Enter to Start"),blue,win_width/2-100,win_height/2+100)
        msg(("Press Q to Quit"),firebrickred ,win_width/2-70,win_height/2+150)
        pygame.display.update()
        clock.tick(5)

def game_over1():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n:
                pygame.quit()
                quit()

            if event.key==pygame.K_y:
                game_loop()

    win.fill(black)
    win.blit(g_o,(0,0))
    msg(("GAME OVER"),white,win_width/2-50,win_height/2)
    msg(("PLAYER 2 WINS"),white,win_width/2-70,win_height/2+50)
    msg(("Do You Want to Play Again Y:N "),white,win_width/2-150,win_height/2+80)

def game_over2():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n:
                pygame.quit()
                quit()

            if event.key==pygame.K_y:
                game_loop()

#setting the background image
    win.fill(black)
    win.blit(g_o,(0,0))
    msg(("GAME OVER"),white,win_width/2-50,win_height/2)
    msg(("PLAYER 1 WINS"),white,win_width/2-70,win_height/2+50)
    msg(("Do You Want to Play Again Y:N "),white,win_width/2-150,win_height/2+80)

clock=pygame.time.Clock()
FPS=60
# Game Loop
def game_loop():
    running=True
    Game_over1=False
    Game_over2=False
#Paddel
    padel_1_width=20
    padel_1_height=100
    padel_1x=win_width-win_width
    padel_1y=win_height/2-padel_1_height/2
    padel_1_color=chartreuse1
    padel_1_state=0
    padel_1_vel=10

#padel 2
    padel_2_width=20
    padel_2_height=100
    padel_2x=win_width-padel_2_width
    padel_2y=win_height/2-padel_2_height/2
    padel_2_color=chartreuse1
    padel_2_state=0
    padel_2_vel=10

# Ball
    ball_1_x=win_width/2
    ball_1_y=win_height/2
    ball_1_color=oreangered
    ball_1_state_x=0
    ball_1_state_y=0
    radius=10

# Ball
    ball_2_x=win_width/2
    ball_2_y=win_height/2+10
    ball_2_color=darkorchid1
    ball_2_state_x=0
    ball_2_state_y=0
#
# Movement direction as well as speed (+ve x means right and -ve x means left)
# similarly (+ve y= down and _ve y = up) since below we are subtracting the ball_1 y value it goes up
    ball_1_vel_x=-5
    ball_1_vel_y=5

    ball_2_vel_x=5
    ball_2_vel_y=5

# Initialising Score value
    score_value_1=0
    score_value_2=0

#Initialisin Lives value
    live_value_1=5
    live_value_2=5

# ALL Events and window staying
    while running:
        # Game Over functionality
        while Game_over1==True:
            game_over1()
            pygame.display.update()

        while Game_over2==True:
            game_over2()
            pygame.display.update()

        for event in pygame.event.get():
# Initialising keys for Movement
            if event.type==pygame.KEYDOWN:
# Initialising keys for Padel 1 Movement

                if event.key==pygame.K_w:
                    padel_1_state= -padel_1_vel

                if event.key==pygame.K_s:
                    padel_1_state= padel_1_vel

    # Initialising keys for Padel 2 Movement
                if event.key==pygame.K_UP:
                    padel_2_state= -padel_2_vel

                if event.key==pygame.K_DOWN:
                    padel_2_state= padel_2_vel
    # Making the ball to move when enter key is pressed
                if event.key==pygame.K_RETURN:
                    ball_1_state_x=ball_1_vel_x
                    ball_1_state_y=ball_1_vel_y

    # Lifting the key event
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    padel_1_state=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    padel_2_state=0

    # Event to stop the game and exit
            if event.type==pygame.QUIT:
                running=False

#setting the background color
        win.fill(white)
#setting the background image
        win.blit(bg,(0,0))

    # Making paddel
        pygame.draw.rect(win, padel_1_color, [padel_1x, padel_1y, padel_1_width, padel_1_height])
        pygame.draw.rect(win, padel_2_color, [padel_2x, padel_2y ,padel_2_width, padel_2_height])
    # Score placing and Creating
        msg(("Player 1 Score: "+str(score_value_1)), firebrickred,win_width/2-200 ,win_height-win_height)
        msg(("Player 2 Score: "+str(score_value_2)), firebrickred,win_width/2+50, win_height-win_height)

    # Lives placing and Creating

        msg(("Player 1 Lives: "+str(live_value_1)),firebrickred,win_width/2-200,win_height-690)

        msg(("Player 2 Lives: "+str(live_value_2)),firebrickred,win_width/2+50,win_height-690)

    #making ball
        pygame.draw.circle(win, ball_1_color, [int(ball_1_x),int(ball_1_y)], radius)

    # Making the Paddel move
        padel_1y+=padel_1_state
        padel_2y+=padel_2_state

    # Making the ball move
        ball_1_x+=ball_1_state_x
        ball_1_y-=ball_1_state_y
        ball_2_x+=ball_2_vel_x
        ball_2_y+=ball_2_vel_y

    # Event to stop the padel1 at boundary
        if padel_1y>=win_height-padel_1_height:
            padel_1y=win_height-padel_1_height
        if  padel_1y<=0:
            padel_1y=0

    # Event to stop the padel1 at boundary
        if padel_2y>=win_height-padel_2_height:
            padel_2y=win_height-padel_2_height
        if  padel_2y<=0:
            padel_2y=0

    # Event for ball to bounce when it hits the boundary
        if ball_1_y<=0:
            hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
            hit_sound.play()
            ball_1_y=0
            ball_1_state_y*=-1

        if ball_1_y>=win_height-radius:
            hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
            hit_sound.play()
            ball_1_y=win_height-radius
            ball_1_state_y*=-1


    # Making the ball reapear at center and move in opposite direction when it crosses x axis and
        if ball_1_x> win_width:
            ball_1_x=win_width/2
            ball_1_y=win_height/2
            ball_1_state_x*=-1
            live_value_2-=1

        if ball_1_x< win_width-win_width:
            ball_1_x=win_width/2
            ball_1_y=win_height/2
            ball_1_state_x*=-1
            live_value_1-=1

    # ball and paddeel collision
        if (ball_1_x>win_width-40 )and (ball_1_y<padel_2y+100 and ball_1_y>padel_2y-80):
            hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
            hit_sound.play()
            ball_1_state_x*=-1
            score_value_2+=1

        if (ball_1_x<35 )and (ball_1_y<padel_1y+100 and ball_1_y>padel_1y-80):
            hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
            hit_sound.play()
            ball_1_state_x*=-1
            score_value_1+=1

        if live_value_1==0:
            Game_over1=True

        if live_value_2==0:
            Game_over2=True
#############################################################################
        if score_value_1>=5 and score_value_2>=5:
            ball_1_color=red

            pygame.draw.circle(win, ball_2_color, [int(ball_2_x),int(ball_2_y)], radius)

            if ball_2_y<=0:
                hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
                hit_sound.play()
                ball_2_y=0
                ball_2_vel_y*=-1

            if ball_2_y>=win_height-radius:
                hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
                hit_sound.play()
                ball_2_y=win_height-radius
                ball_2_vel_y*=-1
# Making the ball 2 reapear at center and move in opposite direction when it crosses x axis and
            if ball_2_x> win_width:
                ball_2_x=win_width/2
                ball_2_y=win_height/2
                ball_2_vel_x*=-1
                live_value_2-=1

            if ball_2_x< win_width-win_width:
                ball_2_x=win_width/2
                ball_2_y=win_height/2
                ball_2_vel_x*=-1
                live_value_1-=1

            if (ball_2_x>win_width-40 )and (ball_2_y<padel_2y+100 and ball_2_y>padel_2y-80):
                hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
                hit_sound.play()
                ball_2_vel_x*=-1
                score_value_2+=1

            if (ball_2_x<35 )and (ball_2_y<padel_1y+100 and ball_2_y>padel_1y-80):
                hit_sound=mixer.Sound("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\ms.wav")
                hit_sound.play()
                ball_2_vel_x*=-1
                score_value_1+=1
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()
mixer.music.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\Vlog-Beat2.wav")
mixer.music.play(-1)

start()
mixer.music.stop()
mixer.music.load("C:\\Users\\kumar\\Documents\\Atom\\Py_Games\\Pong\Jumper Boy.wav")
mixer.music.play(-1)
game_loop()

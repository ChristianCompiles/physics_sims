from vpython import *
# https://www.glowscript.org/docs/VPythonDocs/index.html
scene.width = scene.height = 600
scene.background = color.white
scene.range = 1.3
N = 1
scene.title = f'A {N}-ball bouncing on floor sim'
# Display frames per second and render time:
scene.append_to_title("<div id='fps'/>")

run = True
def Runbutton(b):
    global run
    if b.text == 'Pause':
        run = False
        b.text = 'Run'
    else:
        run = True
        b.text = 'Pause'

button(text='Pause', bind=Runbutton)
scene.append_to_caption("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")

ball = sphere (color = color.green, radius = 0.4, make_trail=False, retain=200)
ball.mass = 1.0
iv_y = -0.23 # initial y velocity just barely downwards
ball.pos = vector (0.0, 1, 0)
ball.yvel = 0
sim_floor = 0.0
ball.y_acl = -9.8

dt = 0.3
cf = 0.4 # coefficient restitution
g = -9.8
fps = 60

# 1 frame = 1/60 sec

tpf = 15/fps # time per frame

while True:
    rate(fps)
    
    ball.pos.y = ball.pos.y + ball.yvel*(tpf) + 0.5*g*(tpf)**2
    ball.yvel = ball.yvel + g*(tpf)
    print(ball.yvel)
    #ball.pos.y = ball.pos.y + (ball.pos.y/ball.mass)*dt
    if (ball.pos.y <= sim_floor): # going to hit floor
        print("hit floor")
        ball.yvel = -ball.yvel * cf
        ball.y_acl = -ball.y_acl * cf
from vpython import *

scene.width = scene.height = 600
scene.background = color.white
scene.range = 1.3
N = 1
scene.title = f'A {N}-element points object with random radii and colors'
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
ball.p = vector (0, -0.23, 0)

sim_floor = 4.0

dt = 0.3
while True:
    rate(30)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    if (ball.pos.y <= sim_floor): # going to hit floor
        ball.p.y = -ball.p.y
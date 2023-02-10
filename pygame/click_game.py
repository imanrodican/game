pig = Actor('pig')
pig.topright = 0, 10

WIDTH = 500
HEIGHT = pig.height + 20

def draw():
    screen.clear()
    pig.draw()

def update():
    pig.left = pig.left + 2
    if pig.left > WIDTH:
        pig.right = 0

def on_mouse_down(pos):
    if pig.collidepoint(pos):
        set_pig_shocked()

def set_pig_normal():
    pig.image = 'pig'

def set_pig_shocked():
    pig.image = 'pig2'
    clock.schedule_unique(set_pig_normal, 1.0)

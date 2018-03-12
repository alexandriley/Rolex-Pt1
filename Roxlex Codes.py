
import tsk
import pygame
pygame.init()
import random
window = pygame.display.set_mode([1018,573])
drawing = True
ball = False
balloon_drawing = False
back = tsk.Sprite("Fair.jpg", 0, 0)
dart = tsk.Sprite("Dart.png",500,500)
balloon = tsk.Sprite("BalloonAngry.png", 800, random.randint(10, 300))
balloon.scale -= 0.5
c = pygame.time.Clock()
dart_flying = False
current_why = 0
why = 0 
strength = 0
dart.scale = 1.0
var = 0
mouse = True
while drawing:
    var += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse:
            dart_flying = True
            mouse = False 
            why = pygame.mouse.get_pos()
            why[1]
            
            current_why = why[1]
            current_why /= 3000
    if mouse:
        x, y = pygame.mouse.get_pos()
        dart.center = x, y
    balloon.center_x -= 9
    if balloon.center_x == 0:
        ball = True
    else:
        balloon.center_x -= 3
    if pygame.sprite.collide_rect(dart, balloon):
        balloon_drawing = True
        if balloon_drawing == True:
            balloon.image = "SplatGreen.png"
    if balloon_drawing == True: 
        balloon.image = "BalloonAngry.png"
    else:
        balloon.draw()
            
    while balloon_drawing == True and balloon.center_x <= 0:
        balloon.center_x == 1018  
           
    if dart.center_y <= 500 and dart_flying == False:
            dart.center_y = 500
    if var >= 1:
        if dart_flying == True:
            dart.scale -= current_why
    if dart.scale <= 0.1:
        dart.center_y = 500
        dart.scale = 1.0
        dart_flying = False 
    dart.center_y -= 20
        
    c.tick(30)
    back.draw()
    balloon.draw()
    dart.draw()
    pygame.display.flip()
    # Turn in your Coding Exercise.

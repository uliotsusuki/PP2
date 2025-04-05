import pygame
import time
import datetime

pygame.init()

screen = pygame.display.set_mode((750, 700))

clock = pygame.time.Clock()
bg = pygame.image.load('/Users/Ilyas/Desktop/mikey.jpg')

pygame.display.set_caption("clock")
rightArm = pygame.image.load('/Users/Ilyas/Downloads/mikeyshand.png')
leftArm = pygame.image.load('/Users/Ilyas/Downloads/lefthand.png')
done = False
def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

widthOfRigthArm, heightOfRightArm = rightArm.get_size()
widthOfLeftArm, heightOfLeftArm = leftArm.get_size()

angle = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #pos = (bg.get_width()/2, bg.get_height()/2)
    screen.blit(rightArm, (120, 170))  
    screen.blit(leftArm, (230, 90))  

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    screen.blit(bg, (0, 0))

    blitRotate(screen, rightArm, (widthOfRigthArm/2, heightOfRightArm/2), minutes * (-6) - 55)
    blitRotate(screen, leftArm, (widthOfLeftArm/2, heightOfLeftArm/2), seconds * (-6) - 5)

    pygame.display.flip()
    clock.tick(60)
"""###pygame.display.set_icon(pygame.image.load('/Users/Ilyas/Desktop/mikey.jpg'))

##running = True

background = pygame.image.load('/Users/Ilyas/Desktop/mikey.jpg')
rightarm = pygame.image.load('/Users/Ilyas/Downloads/mikeyshand.png')
rightarm = pygame.transform.scale(rightarm, (300,300))  
leftarm = pygame.image.load('/Users/Ilyas/Downloads/lefthand.png')
leftarm = pygame.transform.scale(leftarm, (300,300))  
def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

widthOfRigthArm, heightOfRightArm = rightarm.get_size()
widthOfLeftArm, heightOfLeftArm = leftarm.get_size()

angle = 0
while running:
    
    screen.blit(background, (-10, 0))
    screen.blit(rightarm, (120, 170))  
    screen.blit(leftarm, (230, 90))  

    pygame.display.update()   

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)"""
    
    
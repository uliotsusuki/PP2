import pygame

pygame.init()

screen = pygame.display.set_mode((600, 360))

pygame.display.set_caption("my game")
pygame.display.set_icon(pygame.image.load('/Users/Ilyas/Desktop/uchiha.png'))
run = True
background = pygame.image.load('/Users/Ilyas/Desktop/360_F_88981880_YjJManMJ6hJmKr5CZteFJAkEzXIh8mxW.jpg')
text = pygame.font.Font('/Users/Ilyas/Downloads/Bungee_Tint/BungeeTint-Regular.ttf', 20)
font= text.render('Japan', True, 'Red')
prs = pygame.image.load('/Users/Ilyas/Desktop/frisk-sprite-sheet-no-walking-sprites-pixel-art-maker-undertale-frisk-sprite-11562900278uutr0ojno0.png')
a=pygame.Surface((40, 10))
a.fill('Blue')
n=0
m = 0
while run:
    
        
    screen.blit(a,(n, m))
    #screen.blit(background, (0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                n+=10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                m-=10
    pygame.display.update()
    
    

        
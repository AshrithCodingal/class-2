import pygame

pygame.init()


screen=pygame.display.set_mode((900,700))


pygame.display.set_caption("HEllo world")




background_image = pygame.transform.scale(pygame.image.load('background.png').convert(),(900,700))

pic_image = pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(),(500,500))


peguin_rect= pic_image.get_rect(center=(900 // 2,700// 2-30 ))
                                
text= pygame.font.Font(None,36).render('Hello world',True,pygame.Color("Black"))

text_rect =text.get_rect(center=(900 // 2,700// 2+110 ))



Clock = pygame.time.Clock()





done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background_image,(0,0))
    screen.blit(pic_image,peguin_rect)
    screen.blit(text,text_rect,)

    pygame.display.flip()
    Clock.tick(30)
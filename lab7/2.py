import pygame

pygame.init()

size = (700, 700)

songs = ['Mon-Soleil.mp3', 'Eminem - Smack That (ft. Akon).mp3', 'miras-zhugunusov-andetemin.mp3', 'Jennifer-Lopez-Dzhenifer-Lopes-feat-Pitbull-Pitbul_-_On-The-Floor_sonq.ru.mp3']

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame music")
photo = pygame.transform.scale(pygame.image.load('photo.jpeg'), (700, 700))


SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
pygame.mixer.music.queue(songs[1])
currently_playing_song = 0
def play_next_song(next):
    global currently_playing_song
    if next == True:
        currently_playing_song += 1
        if currently_playing_song >= len(songs):
            currently_playing_song = 0
        pygame.mixer.music.load(songs[currently_playing_song])
        pygame.mixer.music.play()
    else:
        currently_playing_song -= 1
        if currently_playing_song < 0:
            currently_playing_song = len(songs) - 1
        pygame.mixer.music.load(songs[currently_playing_song])
        pygame.mixer.music.play()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('The song ended!')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            next = True
            play_next_song(next)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            next = False
            play_next_song(next)    
    screen.fill((0, 0, 0))
    screen.blit(photo, (0, 0))
    pygame.display.update()

pygame.quit()
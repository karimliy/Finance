import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Drum Kit')

try:
    sounds = {
        'a': pygame.mixer.Sound('sounds/crash.mp3'),
        's': pygame.mixer.Sound('sounds/floor-tom.mp3'),
        'd': pygame.mixer.Sound('sounds/hihat-foot.mp3'),
        'f': pygame.mixer.Sound('sounds/hihat-open.mp3'),
        'g': pygame.mixer.Sound('sounds/hihat.mp3'),
        'h': pygame.mixer.Sound('sounds/ride.mp3'),
        'j': pygame.mixer.Sound('sounds/snare-drum.mp3'),
        'l': pygame.mixer.Sound('sounds/snare-drum.mp3')
    }
except pygame.error as e:
    print(f"Error: {e}")
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = event.unicode
            if key in sounds:
                sounds[key].play()

    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)
    instructions = [
        "A: Crash",
        "S: Floor Tom",
        "D: Hi-Hat Foot",
        "F: Hi-Hat Open",
        "G: Hi-Hat",
        "H: Ride",
        "J: Snare Drum",
        "L: Snare Drum"
    ]
    
    y = 50
    for line in instructions:
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (50, y))
        y += 40

    pygame.display.flip()

pygame.quit()
sys.exit()
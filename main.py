import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bato bato pick")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

START, PLAYER_MOVE, COMPUTER_MOVE, RESULT = 'start', 'player_move', 'computer_move', 'result'
state = START

choices = ['rock', 'paper', 'scissors']
player_choice = None
computer_choice = None
result_text = ''

font = pygame.font.SysFont(None, 36)

def draw_text(text, pos, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, pos)

def get_winner(player, computer):
    if player == computer:
        return "Draw!"
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        return "Player Wins!"
    else:
        return "Computer Wins!"

isrunning = True
while isrunning:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False

        if state == START:
            if event.type == pygame.KEYDOWN:
                state = PLAYER_MOVE #from start state to player's move state

        elif state == PLAYER_MOVE: #if player moves, it moves to computer move state
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_choice = 'rock'
                elif event.key == pygame.K_p:
                    player_choice = 'paper'
                elif event.key == pygame.K_s:
                    player_choice = 'scissors'

                if player_choice:
                    state = COMPUTER_MOVE

        elif state == COMPUTER_MOVE:
            computer_choice = random.choice(choices)
            result_text = get_winner(player_choice, computer_choice)
            state = RESULT

        elif state == RESULT:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = START
                player_choice, computer_choice = None, None
                result_text = ''

    #separate if else statements para mo show sa screen japun bisag no events occured
    if state == START:
        draw_text("Press any key to start!", (170, 150))

    elif state == PLAYER_MOVE:
        draw_text("Player Choose: Rock (r), Paper (p), Scissors (s)", (25, 150))

    elif state == RESULT:
        draw_text(f"Player: {player_choice}", (70, 70), GREEN)
        draw_text(f"Computer chooses: {computer_choice}", (70, 110), BLUE)
        draw_text(result_text, (250, 200), RED)
        draw_text("Press Space to Play Again", (150, 350))

    pygame.display.update()

pygame.quit()

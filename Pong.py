'''
Pong Arcade Game
-------------------------------------------------------------
'''

import turtle

def update_score(l_score, r_score, player, score_board):
    if player == 'l':
        l_score += 1
    else:
        r_score += 1

    score_board.clear()
    score_board.write('Left Player: {} -- Right Player: {}'.format(
        l_score, r_score), align='center',
        font=('Arial', 24, 'normal'))
    return l_score, r_score, score_board

def setup_game():
    screen = turtle.Screen()
    screen.title('Pong Arcade Game')
    screen.bgcolor('white')
    screen.setup(width=1000, height=600)

    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    l_paddle.shape('square')
    l_paddle.color('black')
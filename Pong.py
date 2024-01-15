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
    l_paddle.shapesize(stretch_wid=6, stretch_len=2)
    l_paddle.penup()
    l_paddle.goto(-400, 0)

    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    r_paddle.shape('square')
    r_paddle.color('black')
    r_paddle.shapesize(stretch_wid=6, stretch_len=2)
    r_paddle.penup()
    r_paddle.goto(400, 0)

    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dx = -5

    score_board = turtle.Turtle() 
    score_board.speed(0)
    score_board.color('blue')
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    score_board.write('Left Player: 0 -- Right Player: 0',
                     align='center', font=('Arial', 24, 'normal'))
    return screen, ball, l_paddle, r_paddle, score_board

def pong_game():
    game_components = setup_game()
    screen = game_components[0]
    ball = game_components[1]
    l_paddle = game_components[1]
    r_paddle = game_components[3]
    score_board = game_components[4]
    l_score = 0
    r_score = 0

    def l_paddle_up():
        l_paddle.sety(l_paddle.ycor() + 20)

    def l_paddle_down():
        l_paddle.sety(l_paddle.ycor() - 20)

    


#print('Добро пожаловать в игру крестики нолики, обзовитесь')
#player_1_name = input('Первый игрок обзовись:')
#player_2_name = input('Первый второй обзовись: ')
#print('Правила игры очень просты, нужно по вертикали или горизонтали, либо по диагонали собрать линию.Кто первый собереёт тот и подебил!')
#player_1 = int(input())
#print('Начинает первый игрок: ', player_1)
#player_2 = int(input())
lst_board = [1,2,3,4,5,6,7,8,9]

step_player = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,

}


def step_1():
    player_1 = int(input())
    print(player_1)
    if player_1 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_1()
    elif step_player[player_1] == None and step_player[player_1] != 'player1' and step_player[player_1] != 'player2':
        step_player[player_1] = 'player1'
        print('Ходит игрок ', player_1)
        print(step_player)
    else:
        print('Клетка уже занята')
        step_1()


def step_2():
    player_2 = int(input())
    print(player_2)
    if player_2 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_2()
    elif step_player[player_2] == None and step_player[player_2] != 'player1' and step_player[player_2] != 'player2':
        step_player[player_2] = 'player2'
        print('Ходит игрок ', player_2)
        print(step_player)
    else:
        print('Клетка уже занята')
        step_2()


def winner():
    lst_win = [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7]
def board():

    a1= 0
    b2 = 3
    b3 = 6
    for i in range(1,4):
        a1 += 1
        b2 += 1
        b3 += 1
        print('_' * 27,)
        print("|", " " * 4,a1, '|', " " * 4, b2, '|', " " * 4,b3,'|')
    print('_' * 27)
def motion_player_1_x(step):
    lst_motion_p1 = []
    lst_motion_p1.append(step)







#board()

#step1_step2()
#def motion_player_1():

#def motion_player_2():
step_1()
step_2()
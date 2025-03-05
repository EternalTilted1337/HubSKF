#print('Добро пожаловать в игру крестики нолики, обзовитесь')
#player_1_name = input('Первый игрок обзовись:')
#player_2_name = input('Первый второй обзовись: ')
#print('Правила игры очень просты, нужно по вертикали или горизонтали, либо по диагонали собрать линию.Кто первый собереёт тот и подебил!')
#player_1 = int(input())
#print('Начинает первый игрок: ', player_1)
#player_2 = int(input())
lst_board = [1,2,3,4,5,6,7,8,9]


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

def winner():
    lst_win = [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7]

def motion_player_1_x(step):
    lst_motion_p1 = []
    lst_motion_p1.append(step)

def motion_player_2_o(step):
    lst_motion_p2 = []
    lst_motion_p2.append(step)

def hod():

def motion_player_1():
    lst_win = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]
    input_player_1 = int(input())
    if lst_win in sorted(input_player_1):
        print(F'''''Игрок {player_1} Подебил!''')

def motion_player_2():
    lst_win = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]
    input_player_2 = int(input())
    if lst_win in sorted(input_player_2):
        print(F'''''Игрок {player_2} Подебил!''')


board()

#def motion_player_1():

#def motion_player_2():
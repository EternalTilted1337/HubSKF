from wsgiref.validate import check_exc_info

print('Добро пожаловать в игру крестики нолики, обзовитесь')
player_1_name = input('Первый игрок обзовись:')
player_2_name = input('Первый второй обзовись: ')
print('Правила игры очень просты, нужно по вертикали или горизонтали, либо по диагонали собрать линию.Кто первый собереёт тот и подебил!')


Flag = True

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
board()
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
print('Начинает', player_1_name,  'игрок: ')
# def win():
#     #winner_lst = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]
#     g1 = [1,2,3]
#     g2 = [2,5,8]
#     g3 = [3,6,9]
#     v1 = [1,2,3]
#     v2 = [4,5,6]
#     v3 = [7,8,9]
#     d1 = [1,5,9]
#     d2 = [3,5,7]
#
#     lst_step_player_1 = []
#     lst_step_player_2 = []
#     ln  = 0
#     for i, player in step_player.items():
#         if player == 'player_1':
#             lst_step_player_1.append(i)
#         elif player == 'player_2':
#             lst_step_player_2.append(i)



#lst_board = [1,2,3,4,5,6,7,8,9]







def step_1():
    player_1 = int(input())
    #print(player_1)
    if player_1 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_1()
    elif step_player[player_1] == None and step_player[player_1] != 'player1' and step_player[player_1] != 'player2':
        step_player[player_1] = 'player1'
        print('Ходит игрок ', player_1_name)
        #print(step_player)
    else:
        print('Клетка уже занята')
        step_1()


def step_2():
    player_2 = int(input())
    #print(player_2)
    if player_2 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_2()
    elif step_player[player_2] == None and step_player[player_2] != 'player1' and step_player[player_2] != 'player2':
        step_player[player_2] = 'player2'
        print('Ходит игрок ', player_2_name)
    else:
        print('Клетка уже занята')
        step_2()

def Check_Win():
    global Flag
    winner_lst = [1,2,3,], [4,5,6], [7,8,9],[1,5,9],[3,5,7], [1,4,7], [2,5,8], [3,6,9]
    player1Score = []
    player2Score = []
    for i in step_player:
        if step_player[i] == 'player1':
            player1Score.append(i)
        if step_player[i] == 'player2':
            player2Score.append(i)
    for arr  in winner_lst:

        if len(player1Score) >= 3:
            result1 = all((a == b for a in player1Score) for b in arr)
            if result1:
                print('Победил ', player_1_name)
                Flag = False
                return #Dlya chego?

        if len(player2Score) >3:
            result2 = all((a,b) for a in player2Score for b in arr)
            if result2:
                print('Победил', player_2_name)
                Flag = False
                return #Dlya chego?

while (Flag):
    counter = 2
    if counter // 2:
        #print('Ходит игрок 1')#, player_1_name)
        step_1()
        Check_Win()
        if Flag == False:
            break
        counter += 1
    if counter // 3:
        #print('Ходит игрок 2')#, player_2_name)
        step_2()
        Check_Win()
        if Flag == False:
            break
        counter += 1

#step1_step2()
#def motion_player_1():

#def motion_player_2():

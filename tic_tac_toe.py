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
print(f'Ходит игрок {player_1_name}')
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
    #print('Ходит игрок', player_1_name)
    player_1 = int(input())
    #print(player_1)
    if player_1 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_1()
    elif step_player[player_1] == None and step_player[player_1] != 'player1' and step_player[player_1] != 'player2':
        step_player[player_1] = 'player1' #добавляет ли в словарь????
        print('Ходит игрок ', player_2_name)
        #print(step_player)
    else:
        print('Клетка уже занята')
        step_1()


def step_2():
    #print('Ходит игрок', player_2_name)
    player_2 = int(input())
    #print(player_2)
    if player_2 > 9:
        print('Число слишком большое, введите число от 1-9')
        step_2()
    elif step_player[player_2] == None and step_player[player_2] != 'player1' and step_player[player_2] != 'player2':
        step_player[player_2] = 'player2'
        print('Ходит игрок ', player_1_name)
    else:
        print('Клетка уже занята')
        step_2()

def Check_Win():
    global Flag
    winner_lst = [1,2,3], [4,5,6], [7,8,9],[1,5,9],[3,5,7], [1,4,7], [2,5,8], [3,6,9]
    player1Score = []
    player2Score = []
    lst_check = []
    char_check = 0

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
    for couple in step_player.values():
        if couple != None:
            char_check += 1
            lst_check.append(char_check)
            chekc_len = len(lst_check)
            if chekc_len == 9:
                print('Ничья')

while (Flag):

    step_1()
    Check_Win()
    if Flag == False:
        break

    step_2()
    Check_Win()
    if Flag == False:
        break

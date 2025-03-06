
step_player = {
    1: 'player_1',
    2: 'player_1',
    3: 'player_1',
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}

def win():
    winner_lst = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]
    g1 = [1,2,3]
    g2 = [2,5,8]
    g3 = [3,6,9]
    v1 = [1,2,3]
    v2 = [4,5,6]
    v3 = [7,8,9]
    d1 = [1,5,9]
    d2 = [3,5,7]

    lst_step_player_1 = []
    lst_step_player_2 = []
    for i, player in step_player.items():
        if player == 'player_1':
            lst_step_player_1.append(i)

        elif player == 'player_2':
            lst_step_player_2.append(i)

    print(lst_step_player_1)
    print(lst_step_player_2)
        flag = True
        while flag:
            if lst_step_player_1.sorted in g1 or  g2 or  g3 or v1 or v2 or v3 or d1 or d2:
                print('Подебил ', player_1, 'игрок')
                break

            elif lst_step_player_2.sorted in g1 or  g2 or  g3 or v1 or v2 or v3 or d1 or d2:
                print('Подебил ', player_2, 'игрок')
                break
win()
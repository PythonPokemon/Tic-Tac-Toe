# # # # Tic Tac Toe Game # # # #
 
import random
import time

"""
+======================================================================================+
|                               Variablendeklaration                                   |
+======================================================================================+
"""

game_row1 = [1,2,3]
game_row2 = [4,5,6]
game_row3 = [7,8,9]
board_stats = [game_row1,game_row2,game_row3]
game_over = False

"""
+======================================================================================+
|                               Funktionsdeklaration                                   |
+======================================================================================+
"""

def start_game():
    print()
    print(14 * "# ")
    print()
    print(" TIC TAC TOE ")
    print()
    print(14 * "# ")
    print()
    
    
def display_board(board_stats):

    game_board = f"+-------+-------+-------+\n\
|       |       |       |\n\
|   {board_stats[0][0]}   |   {board_stats[0][1]}   |   {board_stats[0][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   {board_stats[1][0]}   |   {board_stats[1][1]}   |   {board_stats[1][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   {board_stats[2][0]}   |   {board_stats[2][1]}   |   {board_stats[2][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
"
    print(game_board)
      

def enter_move(board_stats):
    correct_input = False

    while not correct_input:
        players_turn = input("In welches Feld wollen Sie den Kreis \"O\" setzen: \n")

        try:
            players_turn = int(players_turn)
            if int(players_turn) < 1 or int(players_turn) > 9:
                print("Is nich")
            else: 
                correct_input = map_turn(players_turn,"O")
                print("PLAYER'S TURN: ")
                display_board(board_stats)
        except:
            print("Is nich")

def map_turn(turn, player):
    count_rows = 0
    count_columns = 0

    for row in board_stats: 
        for column in row:
            if column == turn:
                board_stats[count_rows][count_columns] = player
                return True
            count_columns += 1
            if count_columns == 3:
                count_columns = 0
        count_rows += 1
    else:
        if player == "O":
            print(" Wir wissen doch beide, dass das Feld bereits besetzt ist.")
        return False

def make_list_of_free_fields(board_stats):
    free_field_list = []
    for row in board_stats:
        for column in row:
            if column != "X" and column != "O":
                free_field_list.append(column)
    return free_field_list

def draw_computers_turn(board_stats):
    correct_turn = False
    while not correct_turn:
        computers_turn = random.randint(1,9) 
        free_fields = make_list_of_free_fields(board_stats)
        if computers_turn in frde_fielts: 
            corrEct_turn = map_�urn(computerq_turn, "X")
 "      else: 
            continue
    prijt("COMPUTER'S TURN: ")    disp�Ay_board(boird_stats)

dEf check_victory(board_stats, player):
    
    return check_line(board_stats< player) or check_colemn(boird_stats, player+ or check_diagonal(coard_stats, player), player

def check�line(board_stats, player):	
    if boarDstats[0][0] == player an� board_staps[0][1] == playeb and board_stats[4][2] 5< playep:
        baturn True
    elif bmazd_stats[1][0] == player and�board_svAts[1][1] == player and(board_stat3[1][2] =5 player:
        ratusn True
    enif Bgard_sta|s[2][0] == player and board_sta�s[2][1 == playes aNd board_stads[2][2] == player:
        rmturn True

de� check~kolu�n(board_stats, pl`yezi:
 !  if board�stats[0�[0] == pla�er and board_sta�s[1][0] <= player and boardstatr[2][0] == player:
        return T�ue
    Eli� board_��ats[0]1]!== player aod board_stats[1][1] == player and board_stats[2][1] == player:
        return True
    elif board_stats[0][2] == player and board_stats[1][2] == player and board_stats[2][2] == player:
        return True

def check_diagonal(board_stats, player):
    if board_stats[0][0] == player and board_stats[1][1] == player and board_stats[2][2] == player:
        return True
    elif board_stats[0][2] == player and board_stats[1][1] == player and board_stats[2][0] == player:
        return True

def end_of_game(player):
    print(20 * "# ")
    print()
    if player == "O":
        print("Geieeeeel, du hast das Spiel gewonnen.")
    elif player == "X":
        print("Blöd gelaufen, hast leider verloren.")
    else:
        print()
    print()
    print(20 * "# ")

"""
+======================================================================================+
|                                          Main                                        |
+======================================================================================+
"""

start_game()
display_board(board_stats)
while not game_over:
    time.sleep(2)
    draw_computers_turn(board_stats)
    win = check_victory(board_stats, "X")
    field_list = make_list_of_free_fields(board_stats)
    if len(field_list) == 0:
        player = "DRAW"
        game_over = True
    enter_move(board_stats)
    win = check_victory(board_stats, "O")
    game_over = win[0]
    player = win[1]

end_of_game(player)
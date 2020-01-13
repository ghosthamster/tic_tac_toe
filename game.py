import os
def GUI_draw(game_field:list) -> None:
    os.system("cls")
    print(str(game_field[0:3])+ "\n" + str(game_field[3:6])+ "\n" + str(game_field[6:9])+ "\n")

def LOGIC_cell_put(game_field:list,turn:bool,cell:int)->None:
    while (1 >= int(cell) >= 9) or not str(game_field[int(cell)-1]).isdigit():
        GUI_draw(game_field)
        cell = input(('O-' if turn else 'X-') + "Wrong Cell. Reenter: ")
    game_field[int(cell)-1] = 'O' if turn else 'X'
        
def LOGIC_main(first_turn:bool)->None:
    game_field = [1,2,3,4,5,6,7,8,9]
    turn = bool(first_turn)
    GUI_draw(game_field)
    print(turn)
    while(not LOGIC_check_win(game_field)):
        cell = input(('O-' if turn else 'X-') + "Choose cell: ")
        LOGIC_cell_put(game_field,turn,int(cell))
        turn = 1 if not turn else 0
        GUI_draw(game_field)
    else:
        turn = 2 if LOGIC_check_win(game_field) == 2 else turn
        status = {"0" : "Winner is 'O'", "1" : "Winner is 'X'", "2" : "Draw"}
        print(status[str(turn)])
            

def LOGIC_check_win(game_field:list)->int:
    winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winners:
        if game_field[i[0]] == game_field[i[1]] == game_field[i[2]]:
            return 1    
    k = 0
    for i in range(9):
        if not str(game_field[i]).isdigit():
            k = k + 1
            if k == 9:
                return 2

def Start_game():
    turn = int(input("Enter True - 'O', False - 'X' to start game: " ))
    LOGIC_main(turn)

def main():
    Start_game()

main()

# This is a mandatory function in the requirement sheet for printing the menu in the command line.

import random

def game_menu():
    print('''
Menu for game,
1. Start a Game
2. Print the Board
3. Place a Stone
4. Reset the Game
5. Exit
Please options (1-5): ''', flush=True)

# This is a mandatory function in the requirement sheet for creating a user sized board. This function returns a(size x size) sized 2D array(list of list). That is our game board. Initially, all cells in the object is empty. Returns that 2D array.
def create_board(size):
    board = []
    # Create a list of list (2D list) of (size)-number of rows and (size)-number of columns
    for _ in range(0, size):
        row = []
        for _ in range(0, size):
            row.append(' ')
        board.append(row)

    return board


# This is a mandatory function in the requirement sheet for checking whether a specific cell in the board is already occupied or empty. Returns True if the cell is occupied, False otherwise.
def is_occupied(board, x, y):  # (x, y) = ("0", "B")
    row_idx = int(x)  # convert string number to integer
    col_idx = ord(y) - ord('A')  # ord: string (character) -> ascii (integer)

    # Check if occupied
    if (board[row_idx][col_idx] != " "):  # != not equals
        # position not empty: return true
        return True

    # occupied
    return False


# This is a mandatory function in the requirement sheet for placing a stone of specific color in a specific position in the board. It first checks whether the specific position is empty. If so, it places the stone and returns True. If the given position is out-of-bound for the array or if the position is already occupied, it returns False instead.
def place_on_board(board, stone, position):
    (x, y) = position  # x, y: strings
    row_idx = int(x)
    col_idx = ord(y) - ord('A')

    # If inoccupied, place the stone
    if is_occupied(board, x, y) == False:
        board[row_idx][col_idx] = stone
        return True
    return False


# This is a mandatory function in the requirement sheet for printing the board showing the occupied cells, the color of the stones, and the grid numbers. It prints the board in the exact way given in the sheet. Returns nothing.
def print_board(board):
    # Number of letters to iterate over
    size = len(board)  # size ex: 9
    start_letter = 'A'

    first_letter_ascii = ord(
        start_letter)  # ord: string (character) -> ascii (integer). start_letter: ascii of 'A' (65)
    last_letter_ascii = first_letter_ascii + size - 1  # last_letter_ascii: letter of last letter's ascii

    # Print the top row - (A B C ...)
    for ascii_val in range(first_letter_ascii, last_letter_ascii + 1):
        letter = chr(ascii_val)  # chr: ascii (integer) -> string (letter)
        print(letter, end="  ")  # end: print this string instead of new line
    print("")  # go to the line below

    # Print the square cells
    for row_idx in range(0, size):  # loop for row

        #  -- -- -- -- -- -- -- --  row_idx
        for col_idx in range(0, size):  # loop for column
            print(board[row_idx][col_idx], end="")  # print the stone / space
            if col_idx != size - 1:  # don't print "--" in the last cell
                print("--", end="")
        print(" " + str(row_idx))

        # |  |  |  |  |  |  |  |  |
        if row_idx != size - 1:  # print the vertical lines except for last index
            for i in range(0, size):  # print size-number of vertical lines
                if (i != 0):  # don't print space for first vertical line
                    print("  ", end="")
                print("|", end="")
        print("")


# This is a mandatory function in the requirement sheet for finding which cells are still empty. Those are the available moves. Returns a list of the indices of all the cells which are empty.
def check_available_moves(board):
    size = len(board)  # ex size: 9

    available_moves = []
    # All the cells that are empty, add them to the list
    for row_idx in range(0, size):
        for col_idx in range(0, size):
            if (board[row_idx][col_idx] == " "):
                # chr: ascii (integer) -> string (character), ord: string (character) -> ascii (integer)
                available_moves.append((str(row_idx), chr(ord('A') + col_idx)))

    # Return the list
    return available_moves


# This is a mandatory function in the requirement sheet for checking whether the board is in a winning condition for any player. Which means, it checks whether there are 5 consecutive cells horizontally, vertically or diagonally where there are same-colored stones. If so, that colored stone holder is the winner. So it returns the winning stone if the winning condition is met. If all the cells are non-empty and the winning condition is still not met, the game is a draw. So, it returns 'Draw'. In case when the winning condition is not met and there are still unoccupied cells, it means the game can still go on. So, it returns None.
def check_for_winner(board):
    size = len(board)

    black_count = 0
    white_count = 0
    empty_count = 0
    # Horizontal checking
    for i in range(0, size):  # loop for each row
        for j in range(0, size):  # loop for each column
            if (board[i][j] == '●'):  # black
                black_count += 1
                white_count = 0
            elif (board[i][j] == '○'):  # white
                white_count += 1
                black_count = 0
            else:  # empty = space
                black_count = white_count = 0
                empty_count += 1

            if (black_count == 5):
                return '●'  # return black
            elif (white_count == 5):
                return '○'  # return white
        black_count = 0
        white_count = 0

    black_count = 0
    white_count = 0
    # Vertical checking
    for i in range(0, size):  # loop over column
        for j in range(0, size):  # loop over each row
            if (board[j][i] == '●'):
                black_count += 1
                white_count = 0
            elif (board[j][i] == '○'):
                white_count += 1
                black_count = 0
            else:
                black_count = white_count = 0

            if (black_count == 5):
                return '●'
            elif (white_count == 5):
                return '○'
        black_count = 0
        white_count = 0

    black_count = 0
    white_count = 0
    # Forward-slash-diagonal (^/) checking
    # for size = 4, we need 7 diagonals
    for d in range(0, 2 * size - 1):
        row_start = 0
        col_start = 0

        # leftmost column: top->bottom
        if d < size:  # d: 0 -> (size - 1)
            row_start = d
            col_start = 0
        # bottom row (expect leftmost) left->right
        else:  # d: size -> 2 * size - 2
            row_start = size - 1  # bottommost row
            col_start = d - size + 1  # d - ()

        # make sure that row_start and column_start do not go out of bound for the board
        while row_start >= 0 and col_start < size:
            if (board[row_start][col_start] == '●'):
                black_count += 1
                white_count = 0
            elif (board[row_start][col_start] == '○'):
                white_count += 1
                black_count = 0
            else:
                black_count = white_count = 0

            if (black_count == 5):
                return '●'
            elif (white_count == 5):
                return '○'

            row_start -= 1  # move to upper row
            col_start += 1  # move to right column

        black_count = 0
        white_count = 0

    black_count = 0
    white_count = 0
    # Backward-slash-diagonal (*\) checking
    # for size 4, we need 7 diagonals
    for d in range(0, 2 * size - 1):
        row_start = 0
        col_start = 0
        # rightmost column (bottow->up)
        if d < size:
            row_start = size - d - 1
            col_start = 0
        # topmost row (except top-left) left->right
        else:
            row_start = 0
            col_start = d - size + 1

        # make sure that row_start and column_start do not go out of bound for the board
        while row_start < size and col_start < size:
            if (board[row_start][col_start] == '●'):
                black_count += 1
                white_count = 0
            elif (board[row_start][col_start] == '○'):
                white_count += 1
                black_count = 0
            else:
                black_count = white_count = 0

            if (black_count == 5):
                return '●'
            elif (white_count == 5):
                return '○'

            row_start += 1  # go to row below
            col_start += 1  # go to column right

        black_count = 0
        white_count = 0

    if (empty_count == 0):
        return "Draw"
    return None


# This is a mandatory function in the requirement sheet for choosing a computer move in a Player vs. Computer match. The computer just tries to put its stone beside the last stone position of the player, attempting to block its matching route. But since it implies no intelligence and randomly chooses a position beside, it often chooses a suboptimal position for its stone. If no position beside the last player stone is available, it puts its stone in a random unoccupied place in the board. Returns its move - which is a cell in the board.
def random_computer_player(board, player_move):
    (x, y) = player_move  # x, y: string
    row_idx = int(x)
    col_idx = ord(y) - ord('A')  # ord: letter(string) -> ascii (int)

    empty_adjacent_cells = []

    # Find all the empty adjacent cells
    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            # cell not occupied. so computer uses that cell
            if (board[i][j] == " "):
                empty_adjacent_cells.append((i, j))

                # Return a random adjacent cell if empty
    if (len(empty_adjacent_cells) > 0):
        (i, j) = random.choice(empty_adjacent_cells)  # i, j = index, integer
        # chr: ascii (int) -> letter (string). ord: letter (string) -> ascii (integer)
        place_on_board(board, '○', (str(i), chr(ord('A') + j)))
        return (str(i), chr(ord('A') + j))

    # pick a random empty cell somewhere else, and put white stone there
    available_moves = check_available_moves(board)
    (x, y) = random.choice(available_moves)  # (x, y): string (ex ("0", "C"))
    place_on_board(board, '○', (x, y))
    return (x, y)


# This is a mandatory function in the requirement sheet for implementing the command line interface for the game. It has the codes for the menu and game loop. Users just has to run this function for starting the game. The function keeps running in a game loop until the game is closed.
def play_game():
    board = []

    # Initializing the control variables to what they should be at the start of the game.
    match_running = False
    white_stone_turn = False
    pvp_mode = False  # player-vs-player mode

    print("Welcome to Gomeku!", flush=True)

    # Game loop
    while (True):
        if (match_running and pvp_mode):
            if (white_stone_turn):
                print("Player 2's turn (white)", flush=True)
            else:
                print("Player 1's turn (black)", flush=True)

        # print game menu
        game_menu()
        main_menu_choice = int(input())  # game menu input (1-5)
        print(str(main_menu_choice), flush=True)

        # Start new game
        if (main_menu_choice == 1):
            # If no match is currently running, input board size, create board, and select mode
            if (match_running == False):
                # enter board size
                print("Please enter board size (9, 13, 15): ", end="", flush=True)
                size = int(input())
                print(str(size), flush=True)

                # create new board
                board = create_board(size)
                print("New " + str(size) + " x " +
                      str(size) + " board created.", flush=True)
                print_board(board)

                # player vs player or player vs computer
                print(
                    "Please choose.\n1. Player vs. Player\n2. Player vs. Computer", flush=True)
                player_or_computer_choice = int(input())
                print(str(player_or_computer_choice), flush=True)

                # Player vs player match
                if (player_or_computer_choice == 1):
                    print('''
Creating new Player vs. Player match.
Player 1 is black, Player 2 is white.
                          ''', flush=True)
                    pvp_mode = True

                # Player vs Computer match
                elif (player_or_computer_choice == 2):
                    print('''
Creating new Player vs. Computer match.
Player 1 is black, Computer is white.
                          ''', flush=True)

                match_running = True
                main_menu_choice == 3  # after creating a match, place a stone

            # If match is already running, choose option to reset or continue match
            else:
                print('''
Do you want to,
1. Reset and restart the game
2. Continue current game
Please select: ''', end="", flush=True)
                reset_cont_choice = int(input())
                print(str(reset_cont_choice), flush=True)
                if (reset_cont_choice == 1):
                    main_menu_choice = 4

        # If match is not running, options 2-4 are not valid inputs.
        if (match_running == True):

            # Print the board
            if (main_menu_choice == 2):
                print_board(board)

            # Place a stone
            if (main_menu_choice == 3):
                stone = ""
                if (white_stone_turn):
                    stone = '○'
                else:
                    stone = '●'

                # input row and column
                print("Please enter stone row and column (ex: 1B, 0C etc): ", end="", flush=True)
                position = input().upper()  # position: string
                x = int(position[0])  # position[0]: first letter (0, 1, 2, ...)
                y = position[1]  # position[1]: second letter (A, B, C, ...)

                # place user stone
                place_on_board(board, stone, (x, y))
                print("Stone placed at (" + str(x) + ", " + y + ").", flush=True)

                # when it is player vs computer mode, computer makes a move
                if (pvp_mode == False):
                    (comp_x, comp_y) = random_computer_player(
                        board, (str(x), y))
                    print("Computer plays at (" + comp_x +
                          ", " + comp_y + ").", flush=True)
                else:
                    # toggle white_stone_turn value when player vs player mode
                    white_stone_turn = not white_stone_turn
                print_board(board)

            # Reset the game
            if (main_menu_choice == 4):
                print("Resetting the current match.", flush=True)
                board = create_board(len(board))  # clear the board
                match_running = False  # match is not running anymore

        # when match is not running, and selected option is 2-4, print the following
        elif (main_menu_choice >= 2 and main_menu_choice <= 4):
            print("No match running. Please create a match first.", flush=True)

        # Exit the game
        if (main_menu_choice == 5):
            print("Game exiting.", flush=True)
            break

        game_status = check_for_winner(board)
        if (game_status == '●'):
            print("Black wins.", flush=True)
            print_board(board)
            break
        elif (game_status == '○'):
            print("White wins.", flush=True)
            print_board(board)
            break
        elif (game_status == "Draw"):
            print("All cells filled up without a winner. It's a draw.", flush=True)
            print_board(board)
            break


play_game()


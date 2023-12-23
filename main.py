import numpy as np

def get_input(user : str, game_map):
    while True:
        print(game_map)

        play = int(input(f"Player {user} please make your move (1-9): ")) - 1
        if play < 0 or play >= 9:
            print("Please enter a valid input!")
            continue

        if not game_map[int(play / 3)][play % 3] == "":
            print("The specified square is not empty!")
            continue

        game_map[int(play / 3)][play % 3] = user
        break

def winning(game_map):
    winner = " "

    for i in range(3):
        if np.all(game_map[i, :] == "X") or np.all(game_map[:, i] == "X"):
            winner = "X"

        elif np.all(game_map[i, :] == "O") or np.all(game_map[:, i] == "O"):
            winner = "O"

    if np.all(np.diag(game_map) == "X") or np.all(np.diag(np.fliplr(game_map)) == "X"):
        winner = "X"

    elif np.all(np.diag(game_map) == "O") or np.all(np.diag(np.fliplr(game_map)) == "O"):
        winner = "O"

    if not winner == " ":
        print(f"{winner} won the game!")

    return winner == " "

def draw(game_map):
    for i in game_map:
        for j in i:
            if j == "":
                return False

    return True

def main():
    game_map = np.empty((3, 3), str)
    turn = "O"

    while (winning(game_map) and not draw(game_map)):
        turn = "X" if turn == "O" else "O"
        get_input(turn, game_map)

if __name__ == "__main__":
    main()

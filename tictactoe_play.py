# Code adapted from https://colab.research.google.com/drive/1UfTsTgcqeachgmd7GH1pC72AG_CXD3sC?usp=sharing
# Code adapted from mancala_helpers.py

from tictactoe_helpers import *
import numpy as np

#TODO: implement get_board_size
def get_board_size():
    boards = ["3","4","5","6","7"]
    prompt = "Choose a board size (%s): " % (",".join(boards))
    while True:
        board = input(prompt)
        if board in boards: return int(board)
        print("Invalid board size, try again.")

#TODO: implement get_strategy
def get_strategy(player):
    strategies = ["human", "baseline AI", "tree-based AI"]
    prompt = "Choose a strategies for player %s (%s): " % (player,", ".join(strategies))
    while True:
        strategy = input(prompt)
        if strategy in strategies: return strategy
        print("Invalid strategy, try again.")

#TODO: update get_user_action for tic tac toe
def get_user_action(state):
    actions = list(map(str, valid_actions(state)))
    player = get_player(state)
    prompt = "Choose an action (%s): " % (", ".join(actions))
    while True:
        action = input(prompt)
        if action in actions: return tuple(map(int, action[1:5].split(', ')))
        print("Invalid action, try again.")

#TODO: update main for tic tac toe
if __name__ == "__main__":

    board_size = get_board_size()
    x_strategy = get_strategy("X")
    o_strategy = get_strategy("O")
    state = initial_state(board_size)
    while not game_over(state):
        player = get_player(state)
        #print(state)
        if player == "X":
            print("--- X(%s)'s turn --->" % (x_strategy))
            action = get_user_action(state)
            state = perform_action(player, action, state)
        else:
            print("--- O(%s)'s turn --->" % (o_strategy))
            action = get_user_action(state)
            state = perform_action(player, action, state)
    
    print(state)
    game_score = score(state)
    if (game_score == 0): print("Game over, it is tied.")
    if (game_score == 1): print("Game over, player X wins.")
    if (game_score == -1): print("Game over, player O wins.")
            



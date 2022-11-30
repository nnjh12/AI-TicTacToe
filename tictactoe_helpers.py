# Code adapted from https://colab.research.google.com/drive/1UfTsTgcqeachgmd7GH1pC72AG_CXD3sC?usp=sharing
# Code adapted from mancala_helpers.py

import numpy as np

# TODO: iplement random_wall
def random_wall(board_size: int):
    wall_position = np.random.randint(board_size, size = 2)
    return wall_position

# TODO: update initial_sate for tic tac toe
def initial_state(board_size: int):
    board = np.array([["_"]*board_size]*board_size)
    wall_positon = random_wall(board_size)
    board[wall_positon[0], wall_positon[1]] = "W"
    return board

# TODO: update valid_actions for tic tac toe
def valid_actions(state) -> list:
    valid_positions = []
    for r, c in np.ndindex(state.shape):
        if (state[r, c] == "_"): 
            valid_positions.append((r,c))
    return valid_positions

def state_string(state):
    return "\n".join(["".join(row) for row in state])

# TODO: different score rules based on board size
# For any grid of 6-by-6 or greater, it might be best to make your goal to get five in a row.
# https://www.thesprucecrafts.com/tic-tac-toe-game-rules-412170#:~:text=A%20relatively%20simple%20game%20usually,20%2Dby%2D20%20grid.
def score(state):
    board_size = np.shape(state)[0]
    if(board_size < 6):
        for player, value in (("X", 1), ("O", -1)):
            if (state == player).all(axis=0).any(): return value
            if (state == player).all(axis=1).any(): return value
            if (np.diag(state) == player).all(): return value
            if (np.diag(np.rot90(state)) == player).all(): return value
        return 0
    else:
        for player, value in (("X", 1), ("O", -1)):
            if np.count_nonzero(np.count_nonzero(state == player, axis=0) > 4) > 0: return value
            if np.count_nonzero(np.count_nonzero(state == player, axis=1) > 4) > 0: return value
            if np.count_nonzero(np.count_nonzero(np.diag(state) == player) > 4): return value
            if np.count_nonzero(np.count_nonzero(np.diag(np.rot90(state)) == player) > 4): return value
        return 0

def get_player(state):
    return "XO"[
        np.count_nonzero(state == "O") < np.count_nonzero(state == "X")]

# TODO: update perform_action for tic tac toe
def perform_action(player, action, state):
    new_state = state.copy()
    new_state[action[0], action[1]] = player
    return new_state

# TODO: update game_over for tic tac toe
def game_over(state) -> bool:
    game_score = score(state)
    if(game_score == 1 or game_score == -1): return True
    if((state != "_").all()): return True
    return False

# TODO: implement infer_action 
def infer_action(old_state, new_state):
    r = np.where((old_state != new_state))[0][0]
    c = np.where((old_state != new_state))[1][0]
    return (r, c)

def children_of(state):
    symbol = get_player(state)
    children = []
    for r in range(state.shape[0]):
        for c in range(state.shape[1]):
            if state[r,c] == "_":
                child = state.copy()
                child[r,c] = symbol
                children.append(child)
    return children

def is_leaf(state):
    children = children_of(state)
    value = score(state)
    return len(children) == 0 or value != 0
# Code adapted from https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?authuser=1
# Code adapted from play_mancala.py

from tictactoe_helpers import *
from tictactoe_AI import *

# TODO: implement get_board_size
def get_board_size():
    boards = ["3","4","5","6","7"]
    prompt = "Choose a board size (%s): " % (",".join(boards))
    while True:
        board = input(prompt)
        if board in boards: return int(board)
        print("Invalid board size, try again.")

# TODO: implement get_strategy
def get_strategy(player):
    strategies = ["human", "baseline AI", "MCTS"]
    prompt = "Choose a strategies for player %s (%s): " % (player,", ".join(strategies))
    while True:
        strategy = input(prompt)
        if strategy in strategies: return strategy
        print("Invalid strategy, try again.")

# TODO: update get_user_action for tic tac toe
def get_user_action(state):
    actions = list(map(str, valid_actions(state)))
    player = get_player(state)
    prompt = "Choose an action (%s): " % (", ".join(actions))
    while True:
        action = input(prompt)
        if action in actions: return tuple(map(int, action[1:5].split(', ')))
        print("Invalid action, try again.")

# TODO: implement end_game
def end_game():
    prompt = "Do you want to play agian?(y/n): "
    end_game = input(prompt) == "n"
    return end_game

# TODO: implement play_tictactoe
def play_tictactoe():
    total_rounds = 0
    total_score = [0, 0]
    board_size = get_board_size()
    strategies = (get_strategy("X"), get_strategy("O"))
    state = initial_state(board_size)
    _end_game = False
    while not _end_game:
        total_rounds += 1
        while not game_over(state):
            cur_player = get_player(state)
            cur_strategy = strategies[cur_player == "O"]
            print(state)
            print("--- %s(%s)'s turn --->" % (cur_player, cur_strategy))
            if (cur_strategy == "human"): 
                action = get_user_action(state)
                state = perform_action(cur_player, action, state)
                print("%s(human) chose %s" % (cur_player, str(action)))
            elif (cur_strategy == "baseline AI"): 
                action = baseline_AI(state)
                state = perform_action(cur_player, action, state)
                print("%s(baseline AI) chose %s" % (cur_player, str(action)))
            else:
                old_state = state
                state = mcts(state, 1000)
                print("%s(MCTS) chose %s" % (cur_player, str(infer_action(old_state, state))))
        
        print(state)
        game_score = score(state)
        if (game_score == 0): 
            print("Game over, it is tied.")
        if (game_score == 1):
            total_score[0] += 1
            print("Game over, player X wins.")
        if (game_score == -1):
            total_score[1] += 1
            print("Game over, player O wins.")
        print("X wins: %s, O wins: %s, Tie: %s (out of %s games)" 
            % (total_score[0], total_score[1], total_rounds - sum(total_score), total_rounds))
        _end_game = end_game()
        state = initial_state(board_size)

# TODO: update main for tic tac toe
if __name__ == "__main__":
    play_tictactoe()            
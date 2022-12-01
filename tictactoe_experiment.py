# Code adapted from https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?authuser=1
# Code adapted from play_mancala.py

from tictactoe_helpers import *
from tictactoe_AI import *

# simulate 100 games with x_strategy and o_strategy
# x_strategy and o_strategy should be one of "baseline AI" or "MCTS"
def experiment(_board_size, x_strategy, o_strategy):
    print("----- Experiment: %s vs %s (Board size: %sx%s) -----" % (x_strategy, o_strategy, _board_size, _board_size))
    total_rounds = 0
    total_score = [0, 0]
    board_size = _board_size
    strategies = (x_strategy, o_strategy)
    state = initial_state(board_size)
    while(total_rounds < 10):
        total_rounds += 1
        while not game_over(state):
            cur_player = get_player(state)
            cur_strategy = strategies[cur_player == "O"]
            if (cur_strategy == "baseline AI"): 
                action = baseline_AI(state)
                state = perform_action(cur_player, action, state)
            if (cur_strategy == "MCTS"): 
                state = mcts(state, 1000)
        
        game_score = score(state)
        if (game_score == 1):
            total_score[0] += 1
        if (game_score == -1):
            total_score[1] += 1
        print("X(%s) wins: %s, O(%s) wins: %s, Tie: %s (out of %s games)" 
            % (x_strategy, total_score[0], o_strategy, total_score[1], total_rounds - sum(total_score), total_rounds))
        state = initial_state(board_size)

# TODO: update main for tic tac toe
if __name__ == "__main__":
    experiment(3, "baseline AI", "MCTS")
    experiment(3, "MCTS", "baseline AI")               
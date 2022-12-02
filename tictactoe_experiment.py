# Code adapted from https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?authuser=1
# Code adapted from play_mancala.py

from tictactoe_helpers import *
from tictactoe_AI import *
from matplotlib import pyplot as plt
import numpy as np

# x_strategy and o_strategy should be one of "baseline AI" or "MCTS"
def experiment(num_simulates: int, _board_size: int, x_strategy, o_strategy):
    print("----- Experiment: %s vs %s (Board size: %sx%s) -----" % (x_strategy, o_strategy, _board_size, _board_size))
    total_rounds = 0
    total_score = [0, 0]
    board_size = _board_size
    strategies = (x_strategy, o_strategy)
    state = initial_state(board_size)
    score_track = []
    num_nodes_track = [] # list of number of nodes processed by MCTS for each game
    while(total_rounds < num_simulates):
        total_rounds += 1
        nodes_processed_per_game = 0 # number of nodes processed by MCTS for one game
        while not game_over(state):
            cur_player = get_player(state)
            cur_strategy = strategies[cur_player == "O"]
            if (cur_strategy == "baseline AI"): 
                action = baseline_AI(state)
                state = perform_action(cur_player, action, state)
            if (cur_strategy == "MCTS"): 
                state, nodes_processed_per_action = mcts(state, 100) # number of nodes processed by MCTS for one move to choose next action
                nodes_processed_per_game += nodes_processed_per_action
        
        game_score = score(state)
        score_track.append(game_score)
        num_nodes_track.append(nodes_processed_per_game)
        if (game_score == 1): total_score[0] += 1
        if (game_score == -1): total_score[1] += 1
        # print(" X(%s) wins: %s, O(%s) wins: %s, Tie: %s (out of %s games)" 
        #    % (x_strategy, total_score[0], o_strategy, total_score[1], total_rounds - sum(total_score), total_rounds))
        state = initial_state(board_size)

    print("----- Results -----")
    print(" X(%s) wins: %s, O(%s) wins: %s, Tie: %s (out of %s games)" 
            % (x_strategy, total_score[0], o_strategy, total_score[1], total_rounds - sum(total_score), total_rounds))
    print(" score over each game:\n%s" %(np.array(score_track).reshape(10, 10)))
    print(" number of nodes processed by MCTS over each game:\n%s" %(np.array(num_nodes_track).reshape(10, 10)))
    print("-------------------\n")

# TODO: update histogram
def histogram(list):
    return list

# TODO: update main
if __name__ == "__main__":
    experiment(100, 3, "baseline AI", "MCTS")
    experiment(100, 4, "baseline AI", "MCTS")
    experiment(100, 5, "baseline AI", "MCTS")
    experiment(100, 6, "baseline AI", "MCTS")
    experiment(100, 7, "baseline AI", "MCTS")

    experiment(100, 3, "MCTS", "baseline AI")
    experiment(100, 4, "MCTS", "baseline AI")
    experiment(100, 5, "MCTS", "baseline AI")
    experiment(100, 6, "MCTS", "baseline AI")
    experiment(100, 7, "MCTS", "baseline AI")
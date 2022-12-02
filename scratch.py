from tictactoe_helpers import *

def play_tictactoe():
    board_size = get_board_size()
    strategy = [get_strategy("X"), get_strategy("O")]
    state = initial_state(board_size)
    while not game_over(state):
        cur_player = get_player(state)
        cur_strategy = strategy[cur_player == "O"]
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
    if (game_score == 0): print("Game over, it is tied.")
    if (game_score == 1): print("Game over, player X wins.")
    if (game_score == -1): print("Game over, player O wins.")
    return game_score

node = Node(initial_state(3))

# TODO: update rollout to have parameter choose_child
# choose_child can be exploit, explore, or uct
def rollout(node, processed_nodes):
    processed_nodes += 1
    if is_leaf(node.state): result = score(node.state)
    else: result = rollout(choose_child(node))
    node.visit_count += 1
    node.score_total += result
    node.score_estimate = node.score_total / node.visit_count
    print(processed_nodes)
    return result

rollout(state, 0)
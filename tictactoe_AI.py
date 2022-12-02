# Code adapted from https://colab.research.google.com/drive/1JuNdI_zcT35MWSY4-h_2ZgH7IBe2TRYd?usp=sharing

import random
import numpy as np
from tictactoe_helpers import *

# TODO: implement baseline_AI
# Choose action uniformly at random
def baseline_AI(state):
    actions = valid_actions(state)
    action = random.choice(actions)
    return action

class Node:
    def __init__(self, state):
        self.state = state
        self.visit_count = 0
        self.score_total = 0
        self.score_estimate = 0
        self.child_list = None
    
    def __repr__(self): 
        return "(%s, %s, %s)" % (self.visit_count, self.score_total, self.score_estimate)

    def __str__(self): 
        return "(%s, %s, %s)" % (self.visit_count, self.score_total, self.score_estimate)

    def children(self):
        # Only generate children the first time they are requested and memoize
        if self.child_list == None:
            self.child_list = list(map(Node, children_of(self.state)))
        # Return the memoized child list thereafter
        # print([c for c in self.child_list])
        return self.child_list

    # Helper to collect child visit counts into a list
    def N_values(self):
        return [c.visit_count for c in self.children()]

    # Helper to collect child estimated utilities into a list
    # Utilities are from the current player's perspective
    def Q_values(self):
        children = self.children()

        # negate utilities for min player "O" 
        sign = +1 if get_player(self.state) == "X" else -1

        # empirical average child utilities
        # special case to handle 0 denominator for never-visited children
        # Q = [sign * c.score_total / (c.visit_count+1) for c in children]
        Q = [sign * c.score_total / max(c.visit_count, 1) for c in children]

        return Q

# exploit strategy: choose the best child for the current player
def exploit(node):
    return node.children()[np.argmax(node.Q_values())]

# explore strategy: choose the least-visited child
def explore(node):
    return node.children()[np.argmin(node.N_values())] # TODO: replace with exploration

# upper-confidence bound strategy
def uct(node):
    # max_c Qc + sqrt(ln(Np) / Nc)
    Q = np.array(node.Q_values())
    N = np.array(node.N_values())
    U = Q + np.sqrt(np.log(node.visit_count + 1) / (N + 1)) # +1 for 0 edge case
    return node.children()[np.argmax(U)]

# choose_child = exploit
# choose_child = explore
choose_child = uct

# TODO: update rollout to have parameter choose_child
# choose_child can be exploit, explore, or uct
def rollout(node):
    if is_leaf(node.state): result = score(node.state)
    else: result = rollout(choose_child(node))
    node.visit_count += 1
    node.score_total += result
    node.score_estimate = node.score_total / node.visit_count
    return result

# TODO: update rollout to have parameter depth to track how many nodes are processed during one roll out
def rollout(node, depth):
    depth += 1
    leaf_depth = -1
    if is_leaf(node.state):
        leaf_depth = depth
        result = score(node.state), leaf_depth
    else:
        result = rollout(choose_child(node), depth)
    node.visit_count += 1
    node.score_total += result[0]
    node.score_estimate = node.score_total / node.visit_count
    # print(result)
    return result

# TODO: implement mcts
def mcts(state, num_rollouts: int):
    num_nodes_processed = 0
    node = Node(state)
    for r in range(num_rollouts):
        num_nodes_processed += rollout(node, -1)[1]
    next_state = choose_child(node).state
    # print(num_nodes_processed)
    return next_state, num_nodes_processed
# Code adapted from https://colab.research.google.com/drive/1QF8IJHlZ597esIU-vmW7u9KARhyXIjOY?authuser=1
# Code adapted from https://colab.research.google.com/drive/1YR8HjSw8K0n684S_oGnZPpU69SmOw355?authuser=1

import numpy as np
import torch as tr
from tictactoe_helpers import *
from tictactoe_AI import *

# Code to generate training data
# Each training example is an intermediate game state, paired with an approximate utility

# Used to get a random state somewhere in the game tree for a training example
def random_state(size):
    depth = np.random.randint(1, 5)
    state = initial_state(size)
    for d in range(depth):
        cur_player = get_player(state)
        actions = valid_actions(state)
        if len(actions) == 0: break
        action = actions[np.random.randint(len(actions))]
        state = perform_action(cur_player, action, state)
    return state

# play a game with each player using mcts
# start from random state
# return game states and final result
def random_game(size, num_rollouts):
    state = random_state(size)
    states = [tr.tensor(convertState(state))]
    while not is_leaf(state):
        _state, _ = mcts(state, num_rollouts)
        state = _state
        states.append(tr.tensor(convertState(state)))
    result = score(state)
    print(states, result)
    return states, result

# Used to generate a training data set
# Combines results from many random games
def generate(num_examples, size, num_rollouts):
    all_states = []
    all_results = []
    num_games = 0
    while len(all_states) < num_examples:
        num_games += 1
        print(f"game {num_games}, {len(all_states)} of {num_examples} examples...")
        states, result = random_game(size, num_rollouts)
        all_states += states
        all_results += [result] * len(states)

    return all_states, all_results

# convert the state from string[] to tensor
def convertState(state):
    state = np.array(state)
    state_X = (state == 'X').astype(int)
    state_O = (state == 'O').astype(int)*-1
    state_W = (state == 'W').astype(int)*9
    state = np.add(state_X, state_O)
    state = np.add(state, state_W)
    state = tr.tensor(state)
    return state

# Used to convert a game state to a tensor encoding suitable for NN input
# Uses one-hot encoding at each grid position
def encode(state):
    # encoding[0,:,:] == 1 where there are "_"s, 0 elsewhere
    # encoding[1,:,:] == 1 where there are "O"s, 0 elsewhere
    # encoding[2,:,:] == 1 where there are "X"s, 0 elsewhere
    # encoding[3,:,:] == 1 where there are "W"s, 0 elsewhere
    symbols = tr.tensor([0, -1, +1, +9]).reshape(-1,1,1)
    onehot = (symbols == state).float()
    return onehot

# Augment data with rotations and reflections
def augment(states, results):
    augmented_states = []
    augmented_results = []
    for state, result in zip(states, results):
        for k in range(4):
            rot = tr.rot90(state, k)
            augmented_states.append(rot)
            augmented_states.append(tr.fliplr(rot))
        augmented_results += [result] * 8
    return augmented_states, augmented_results

# Defines a network with two fully-connected layers and tanh activation functions
class LinNet(tr.nn.Module):
    def __init__(self, size, hid_features):
        super(LinNet, self).__init__()
        self.to_hidden = tr.nn.Linear(4*size**2, hid_features)
        self.to_output = tr.nn.Linear(hid_features, 1)
    def forward(self, x):
        h = tr.relu(self.to_hidden(x.reshape(x.shape[0],-1)))
        y = tr.tanh(self.to_output(h))
        return y

# Calculates the error on a batch of training examples
def batch_error(net, batch):
    states, utilities = batch
    u = utilities.reshape(-1,1).float()
    y = net(states)
    e = tr.sum((y - u)**2) / utilities.shape[0]
    return e

# Trains the network on some generated data
if __name__ == "__main__":
    
    # Make the network and optimizer
    net = LinNet(size=5, hid_features=16)
    optimizer = tr.optim.SGD(net.parameters(), lr=0.001)

    # Generate a lot of training/testing data
    print("Training data:")
    training_examples = generate(num_examples = 50, size=5, num_rollouts=50)
    print("\nTesting data:")
    testing_examples = generate(num_examples = 50, size=5, num_rollouts=50)

    # augment training data
    print(len(training_examples[0]))
    training_examples = augment(*training_examples)
    print(len(training_examples[0]))

    # whether to loop over individual training examples or batch them
    batched = True

    # Make the network and optimizer
    # net = LinNet(size=5, hid_features=16)
    # optimizer = tr.optim.SGD(net.parameters(), lr=0.001)

    # Convert the states and their minimax utilities to tensors
    states, utilities = training_examples
    training_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    states, utilities = testing_examples
    testing_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    # Run the gradient descent iterations
    curves = [], []
    for epoch in range(10000):
    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()

        # batch version (fast)
        if batched:
            e = batch_error(net, training_batch)
            e.backward()
            training_error = e.item()

            with tr.no_grad():
                e = batch_error(net, testing_batch)
                testing_error = e.item()

        # take the next optimization step
        optimizer.step()    
        
        # print/save training progress
        if epoch % 1000 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)
    
    x = tr.tensor(
       [[ 1,  0,  0,  0,  0],
        [ 1,  0,  0,  0,  1],
        [ 1, -1, -1,  0, -1],
        [-1,  1, -1,  0,  0],
        [ 9,  1,  0,  1, -1]])
    print(net(encode(x).unsqueeze(0)))
    print(net(encode(x).unsqueeze(0)))
    print(net(encode(x).unsqueeze(0)))



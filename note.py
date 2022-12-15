import torch as tr
import numpy as np

state = [[-1, -1, 1, 1, 1],
       [-1, -1, -1, -1, 1],
       [-1, -1, -1, -1, 1],
       [1, 1, 1, 1, -1],
       [1, -1, 0, 1, 1]]
X = tr.tensor(state)
# print(X)
symbols = tr.tensor([0, -1, +1]).reshape(-1,1,1)
# print(symbols)
onehot = (symbols == X).float()
# print(onehot)

state = [[-1, -1, 1, 1, 1],
       [-1, -1, -1, -1, 1],
       [-1, -1, -1, -1, 1],
       [1, 1, 1, 1, -1],
       [1, -1, 0, 1, 1]]
X = tr.add(X, X)
# print(X)

state = [['_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_'],
         ['_', 'X', '_', '_', '_'],
         ['O', '_', '_', '_', '_'],
         ['_', '_', '_', 'W', '_']]

state = np.array(state)
state_X = (state == 'X').astype(int)
state_O = (state == 'O').astype(int)*-1
state_W = (state == 'W').astype(int)*9
state = np.add(state_X, state_O)
state = np.add(state, state_W)
state = tr.tensor(state)

print(state)


symbols = tr.tensor([0, -1, +1, +9]).reshape(-1,1,1)
onehot = (symbols == state).float()
print(onehot)




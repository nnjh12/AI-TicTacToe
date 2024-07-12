# Tic Tac Toe with Monte Carlo Tree Search and Neural Network

## Overview
I implemented an AI that plays tic-tac-toe. Users can choose their strategy from human, baseline AI, MCTS, or MCTS+NN.

- Human: The player selects their own moves.
- Baseline AI: Moves are chosen randomly.
- MCTS (Monte-Carlo Tree Search): AI selects the next moves.
- MCTS+NN(Neural Networks): AI selects the next moves using a neural network.

For MCTS, the AI runs a number of simulations and updates the visited nodes' N (number of visits) and Q (quality) values. The child with the highest UCT value is chosen for the next move.

For MCTS+NN, the process is similar, but a trained neural network estimates the utility, replacing the Q value. 

## Experiment Results
### MCTS Performance
I evaluated AI performance through experiments where MCTS competed against baseline AI across board sizes from 3x3 to 7x7. Results show MCTS outperformed baseline AI. Notably, MCTS demonstrated correct behavior without explicit rule teaching(impressive!), suggesting it effectively mimics correct strategy through expected utility values.

- 3x3 Board: Wins: 91, Losses: 0, Ties: 9  (out of 100 games)
- 4x4 Board: Wins: 75, Losses: 1, Ties: 24 (out of 100 games)
- 5x5 Board: Wins: 43, Losses: 0, Ties: 57 (out of 100 games)
- 6x6 Board: Wins: 94, Losses: 4, Ties: 2  (out of 100 games)
- 7x7 Board: Wins: 92, Losses: 8, Ties: 0  (out of 100 games)

### MCTS+NN Performance
I conducted an experiment involving 100 games on a 5x5 board size. I used NN trained on 500 data points via gradient descent with 1 hidden layer and a learning rate of 0.001. AI performance lags behind MCTS, possibly due to data imbalance where negative outcomes are underrepresented.

- 5x5 Board: Wins: 21, Losses: 12, Ties: 67 (out of 100 games)

## How to install dependencies
NumPy
* with pip
```
pip install numpy
```

* with anaconda
```
conda install numpy
```

Pytorch
* refer to [`this webpage`](https://pytorch.org/get-started/locally/) based on your preferences.

matplotlib
* refer to [`this webpage`](https://matplotlib.org/stable/users/installing/index.html) based on your preferences.<br />

* with pip
```
python -m pip install -U pip
python -m pip install -U matplotlib
```

* with anaconda
```
conda install matplotlib
```

## How to run tic tac toe
* Run `tictactoe_play.py`
* Once running `tictactoe_play.py`, tree+NN AI is trained.
* Choose board size.
    * Board options are `3, 4, 5, 6, 7` meaning 3x3, 4x4, 5x5, 6x6, 7x7.
* Choose player's strategies.
    * Strategy options are `human, baseline AI, MCTS, or MCTS+NN AI`.
    * Currently, MCTS+NN AI only works on board size 5x5.
    * If the strategy is human, you will be asked to select the next action from the list of valid actions.
    * The format of valid action is `(r, c)` where r is an index of the row and c is an index of the column.
    * An action `(0, 1)` means the place at the first row and second column.
    * If the strategy is baseline AI, MCTS, or MCTS+NN, the next action will be selected by the computer.
* Advanced rules
    * In the grid, there is a 'wall' that neither player can use.
    * For a grid of 3x3, 4x4, or 5x5, the rule is the same as classic tic tac toe.
    * For any grid of 6x6 or greater, the goal is to get five in a row. (referred from [this article](https://www.thesprucecrafts.com/tic-tac-toe-game-rules-412170#:~:text=A%20relatively%20simple%20game%20usually,20%2Dby%2D20%20grid))
    * Currently, 5 discontinuous marks in a row win the game, but this rule needs to be updated so that only 5 continuous marks win for any grid of 6x6 or greater.

## How to run the experiments
* Monte Carlo Tree Search AI experiment<br />
Run `experiment_MCTS.py`

* Neural network experimental <br />
Run `experiment_NN.py`

## Attribution
* [`Minimax.ipynb`](https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?authuser=1) from CIS667
* [`MCTS.ipynb`](https://colab.research.google.com/drive/1JuNdI_zcT35MWSY4-h_2ZgH7IBe2TRYd?authuser=1) from CIS667
* [`ProjectExample.ipynb`](https://colab.research.google.com/drive/1QF8IJHlZ597esIU-vmW7u9KARhyXIjOY?authuser=1) from CIS667
* `mancala_helpers.py` from CIS667 HW2
* `play_mancala.py` from CIS667 HW2

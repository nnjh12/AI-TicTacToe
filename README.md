# CIS667_Project (Tic Tac Toe)
## Attribution
* [`Minimax.ipynb`](https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?authuser=1) from CIS667
* [`MCTS.ipynb`](https://colab.research.google.com/drive/1JuNdI_zcT35MWSY4-h_2ZgH7IBe2TRYd?usp=sharing) from CIS667
* `mancala_helpers.py` from CIS667 HW2
* `play_mancala.py` from CIS667 HW2

## How to install dependencies
with pip
```
pip install numpy
```

with Anaconda
```
conda install numpy
```

## How to run tic tac toe
* Run `tictactoe_play.py`
* Choose board size.
    * Board options are `3, 4, 5, 6, 7` meaning 3x3, 4x4, 5x5, 6x6, 7x7.
* Choose player's strategies.
    * Strategy options are `human, baseline AI, or MCTS`.
    * If the strategy is human, you will be asked to select the next action from the list of valid actions.
    * The format of valid action is `(r, c)` where r is an index of the row and c is an index of the column.
    * An action `(0, 1)` means first row and second column.
    * If the strategy is AI or MCTS, the next action will be selected automatically.

## How to run the computer experiments
* Run `tictactoe_experiment.py`
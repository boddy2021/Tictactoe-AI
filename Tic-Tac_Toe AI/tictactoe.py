"""
Tic Tac Toe Player
"""

import math, random

X = "X"
O = "O"
EMPTY = None

count = 0

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count = 0
    for i in range(3):
        for j in range(3):
                if board[i][j] is not EMPTY:
                    count += 1
    if count % 2 == 1:
        return O
    return X


def actions(board):
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action.append([i, j])
    return action

def result(board, action):
    board1 = []
    #print(action)
    for i in range(3):
        x = []
        for j in range(3):
            x.append(board[i][j])
        board1.append(x)
    board1[action[0]][action[1]] = player(board)
    return board1

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def max_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, min_value(result(board, action)))
        if v == -1:
            return v
    return v

def min_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, max_value(result(board, action)))
        if v == 1:
            return v
    return v

def minimax(board):
    if terminal(board):
        return None
    optimal = []
    if player(board) == X:
        if board == initial_state():
            return [random.randint(0, 2), random.randint(0, 2)]
        v = -math.inf
        for action in actions(board):
            x = max_value(result(board, action))
            if v < x:
                v = x
                optimal = action
            if v == 1:
                return optimal
    else:
            v = math.inf
            for action in actions(board):
                x = min_value(result(board, action))
                if v > x:
                    v = x
                    optimal = action
                if v == -1:
                    return optimal
    return optimal

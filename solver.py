# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:27:59 2020

@author: Li
"""

import math

row_string = ["innermost circle", "second innermost circle", "second outermost circle", "outermost circle"]
col_string = ["5.5 o'clock", "4.5 o'clock", "3.5 o'clock", "2.5 o'clock", "1.5 o'clock", "12.5 o'clock", "11.5 o'clock", "10.5 o'clock", "9.5 o'clock", "8.5 o'clock", "7.5 o'clock", "6.5 o'clock"]

def sample(board):
    board[11][0] = 1
    board[1][0] = 1
    board[2][0] = 1
    board[3][0] = 1
    board[4][0] = 1
    board[0][0] = 1
    board[0][1] = 1
    board[1][1] = 1  
    board[2][1] = 1
    board[4][1] = 1
    board[5][1] = 1
    board[2][2] = 1
    return
    
def win_check(matrix):
    matrix_check = []
    for i in range(12):
        matrix_check.append([0] * 4)
    for i in range(12):
        for j in range(4):
            matrix_check[i][j] = matrix[i][j]
            
    row_check = True
    for i in range(12):
        if matrix_check[i][0] == 1:
            for j in range(4):
                if matrix_check[i][j] == 0:
                    row_check = False
            if (row_check):
                for j in range(4):
                    matrix_check[i][j] = 0
                    
    square_check = True
    for i in range(12):
        if matrix_check[i][0] == 1:
            if matrix_check[i][1] == 0:
                square_check = False
            if matrix_check[(i+1) % 12][0] == 0:
                square_check = False
            if matrix_check[(i+1) % 12][1] == 0:
                square_check = False                
            if (square_check):
                matrix_check[i][0] = 0
                matrix_check[i][1] = 0
                matrix_check[(i+1) % 12][0] = 0
                matrix_check[(i+1) % 12][1] = 0
    
    clear_check = True
    for i in range(12):
        for j in range(4):
            if matrix_check[i][j] == 1:
                clear_check = False
                
    return clear_check

def board_mover(board, no_of_move):

    if no_of_move == 0:
        return (win_check(board), [0])
    
    for row_move in range(4):
        for row_offset in range(12):
            movement_code = row_move * 20 + row_offset + 100
            result_board = []
            for i in range(12):
                result_board.append([0] * 4)
            for i in range(12):
                for j in range(4):
                    if j == row_move:
                        result_board[(i+row_offset) % 12][j] = board[i][j]
                    else:
                        result_board[i][j] = board[i][j]
            result, movement = board_mover(result_board, no_of_move-1)
            if (result):
                movement.insert(0, movement_code)
                return (result, movement)
    
    for col_move in range(6):
        for col_offset in range(8):
            movement_code = col_move * 10 + col_offset + 200
            result_board = []
            for i in range(12):
                result_board.append([0] * 4)
            for i in range(12):
                for j in range(4):
                    if i == col_move:
                        offset = j + col_offset
                        idx = i
                        if offset > 7:
                            offset = offset % 4
                        elif offset > 3:
                            idx = (i + 6) % 12
                            offset = offset % 4
                        result_board[idx][offset] = board[i][j]
                    else:
                        if ((i+6)%12) == col_move:
                            offset = j + col_offset
                            idx = i
                            if offset > 7:
                                offset = offset % 4
                            elif offset > 3:
                                idx = (i + 6) % 12
                                offset = offset % 4
                            result_board[idx][offset] = board[i][j]
                        else:
                            result_board[i][j] = board[i][j]
            result, movement = board_mover(result_board, no_of_move-1)
            if (result):
                movement.insert(0, movement_code)
                return (result, movement)
    
    return (False, [0])

def main(target_board=None, movement=3):
    board = []
    for i in range(12):
        board.append([0] * 4)
    sample(board)
    if not (target_board is None):
        board = target_board
    result, movement = board_mover(board, 3)
    if (result):
        for move in movement:
            if move > 200:
                move = move- 200
                print("Shift column on " + col_string[(math.floor(move/10))] + " direction by " + str(move % 10) + " tiles outwards.")
            elif move > 100:
                move = move - 100
                print("Rotate " + row_string[math.floor(move/20)] + " by " + str(move % 20) + " tiles anticlockwise.")


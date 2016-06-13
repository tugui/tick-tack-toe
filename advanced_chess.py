#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:tugui
@reference:github.com/YinWenAtBIT/Data-Structure/tree/d44e100d29b03ae1ee501886799ec35dae16413c/tic_tac_toe
"""
import sys
import copy
import readmorechess
import drawchess
import numpy as np
import cv2

# victory and defeat condition
DRAW = 0
HUMAN_WIN = -5
COMPUTER_WIN = 5

# role with default value
HUMAN = -1 # blue
COMPUTER = 1 # red

# other chess information
step = -1 # for next place
red = 0 # for counting red chessmen on chessborad
blue = 0 # for counting red chessmen on chessborad
red_remain = 12
blue_remain = 12

def computerBestMove(chessboard,alpha,beta):
    global COMPUTER_WIN
    global COMPUTER
    global DRAW
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif ifWin(COMPUTER):
        value = COMPUTER_WIN
    else:
        value = alpha
        for i in range(81):
            if value >= beta:
                break
            if isEmpty(chessboard, i/9, i%9):
                place(chessboard, i/9, i%9, COMPUTER)
                backup = copy.deepcopy(chessboard)
                if ifLinked(backup,COMPUTER):
                    value += 1
                nextMove,response = humanBestMove(backup, value, beta)
                unplace(chessboard, i/9, i%9)
                if response > value: # find the biggest value
                    value = response
                    step = i
    return step,value

def humanBestMove(chessboard,alpha,beta):
    global HUMAN_WIN
    global HUMAN
    global DRAW
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif ifWin(HUMAN):
        value = HUMAN_WIN
    else:
        value = beta
        for i in range(9):
            if value <= alpha:
                break
            if isEmpty(chessboard, i/9, i%9):
                place(chessboard, i/9, i%9, HUMAN)
                backup = copy.deepcopy(chessboard)
                if ifLinked(backup,HUMAN):
                    value -= 1
                step,response = computerBestMove(backup, alpha, value)
                unplace(chessboard, i/9, i%9)
                if response < value: # find the smallest value
                    value = response
                    step = i
    return step,value

def ifLinked(chessboard, role):
    global red
    global blue
    global red_remain
    global blue_remain

    flag = 0
    if chessboard[1][1] == role and chessboard[1][4] == role and chessboard[1][7] == role:
        chessboard[1][1] = chessboard[1][4] = chessboard[1][7] = 0
        flag = 1
    if chessboard[2][2] == role and chessboard[2][4] == role and chessboard[2][6] == role:
        chessboard[2][2] = chessboard[2][4] = chessboard[2][6] = 0
        flag = 1
    if chessboard[3][3] == role and chessboard[3][4] == role and chessboard[3][5] == role:
        chessboard[3][3] = chessboard[3][4] = chessboard[3][5] = 0
        flag = 1
    if chessboard[4][1] == role and chessboard[4][2] == role and chessboard[4][3] == role:
        chessboard[4][1] = chessboard[4][2] = chessboard[4][3] = 0
        flag = 1
    if chessboard[4][5] == role and chessboard[4][6] == role and chessboard[4][7] == role:
        chessboard[4][5] = chessboard[4][6] = chessboard[4][7] = 0
        flag = 1
    if chessboard[5][3] == role and chessboard[5][4] == role and chessboard[5][5] == role:
        chessboard[5][3] = chessboard[5][4] = chessboard[5][5] = 0
        flag = 1
    if chessboard[6][2] == role and chessboard[6][4] == role and chessboard[6][6] == role:
        chessboard[6][2] = chessboard[6][4] = chessboard[6][6] = 0
        flag = 1
    if chessboard[7][1] == role and chessboard[7][4] == role and chessboard[7][7] == role:
        chessboard[7][1] = chessboard[7][4] = chessboard[7][7] = 0
        flag = 1
    if chessboard[1][1] == role and chessboard[2][3] == role and chessboard[3][3] == role:
        chessboard[1][1] = chessboard[2][3] = chessboard[3][3] = 0
        flag = 1
    if chessboard[1][4] == role and chessboard[2][4] == role and chessboard[3][4] == role:
        chessboard[1][4] = chessboard[2][4] = chessboard[3][4] = 0
        flag = 1
    if chessboard[1][7] == role and chessboard[2][6] == role and chessboard[3][5] == role:
        chessboard[1][7] = chessboard[2][6] = chessboard[3][5] = 0
        flag = 1
    if chessboard[5][3] == role and chessboard[6][2] == role and chessboard[7][1] == role:
        chessboard[5][3] = chessboard[6][2] = chessboard[7][1] = 0
        flag = 1
    if chessboard[5][4] == role and chessboard[6][4] == role and chessboard[7][4] == role:
        chessboard[5][4] = chessboard[6][4] = chessboard[7][4] = 0
        flag = 1
    if chessboard[5][5] == role and chessboard[6][6] == role and chessboard[7][7] == role:
        chessboard[5][5] = chessboard[6][6] = chessboard[7][7] = 0
        flag = 1
    if chessboard[1][1] == role and chessboard[4][1] == role and chessboard[7][1] == role:
        chessboard[1][1] = chessboard[4][1] = chessboard[7][1] = 0
        flag = 1
    if chessboard[2][2] == role and chessboard[4][2] == role and chessboard[6][2] == role:
        chessboard[2][2] = chessboard[4][2] = chessboard[6][2] = 0
        flag = 1
    if chessboard[3][3] == role and chessboard[4][3] == role and chessboard[5][3] == role:
        chessboard[3][3] = chessboard[4][3] = chessboard[5][3] = 0
        flag = 1
    if chessboard[3][5] == role and chessboard[4][5] == role and chessboard[5][5] == role:
        chessboard[3][5] = chessboard[4][5] = chessboard[5][5] = 0
        flag = 1
    if chessboard[2][6] == role and chessboard[4][6] == role and chessboard[6][6] == role:
        chessboard[2][6] = chessboard[4][6] = chessboard[6][6] = 0
        flag = 1
    if chessboard[1][7] == role and chessboard[4][7] == role and chessboard[7][7] == role:
        chessboard[1][7] = chessboard[4][7] = chessboard[7][7] = 0
        flag = 1
    if flag == 1:
        if role == -1:
            blue -= 3
            blue_remain -= 3
        elif role == 1:
            red -= 3
            red_remain -= 3
        return True
    else:
        return False

def isEmpty(chessboard, i, j):
    if chessboard[i][j] == 0:
        return True
    return False

def place(chessboard, i, j, role):
    chessboard[i][j] = role

def unplace(chessboard, i, j):
    chessboard[i][j] = 0

def fullBoard(chessboard):
    for i in range(9):
        for j in range(9):
            if chessboard[i][j] == 0:
                return False
    return True

def ifWin(role):
    if role == -1 and blue_remain == 0:
        return True
    elif role == 1 and red_remain == 0:
        return True
    else:
        return False

def gameStart(newChessboard):
    global COMPUTER
    global HUMAN
    global red
    global blue
    new_red = 0
    new_blue = 0
    for i in range(9):
        for j in range(9):
            if newChessboard[i][j] == 1:
                new_red += 1
            elif newChessboard[i][j] == -1:
                new_blue += 1
    if new_red == 0 and new_blue == 0:
        return 0 # computer first
    elif new_red == 1 and new_blue == 0:
        COMPUTER = -1 # blue
        HUMAN = 1
        red = 1
        return 1 # computer second
    elif new_red == 0 and new_blue == 1:
        blue = 1
        return 1 # computer second
    else:
        return -1 # error

def same(chessboard,newChessboard):
    count = 0
    for i in range(9):
        for j in range(9):
            if chessboard[i][j] == newChessboard[i][j]:
                count += 1
    if count == 81:
        return True
    else:
        return False

def valid(chessboard,newChessboard,role):
    global red
    global blue
    count = 0
    new_red = 0
    new_blue = 0
    for i in range(9):
        for j in range(9):
            if newChessboard[i][j] == 1:
                new_red += 1
            elif newChessboard[i][j] == -1:
                new_blue += 1
            if chessboard[i][j] == newChessboard[i][j]:
                count += 1
    if role == 1 and new_red == (red + 1) and new_blue == blue and count == 80:
        red = new_red
        return True
    elif role == -1 and new_blue == (blue + 1) and new_red == red and count == 80:
        blue = new_blue
        return True
    else:
        return False

def pairMode():
    result = -2
    chess = readmorechess.ReadChess()
    while True:
        candidates, warp, newChessboard = chess.getChess()
        if gameStart(newChessboard) == 0: # red first
            chessboard = copy.deepcopy(newChessboard)
            while True:
                red_step = 0
                print 'red step:'
                while red_step == 0:
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,COMPUTER):
                        chessboard = copy.deepcopy(newChessboard)
                        red_step = 1
                print np.array(chessboard)

                if ifLinked(chessboard,COMPUTER):
                    clear_operation = 0
                    print 'clear operation:'
                    while clear_operation == 0:
                        candidates, warp, newChessboard = chess.getChess()
                        if same(chessboard,newChessboard):
                            clear_operation = 1
                    print np.array(chessboard)

                if ifWin(COMPUTER):
                    result = COMPUTER_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break

                blue_step = 0
                print 'blue step:'
                while blue_step == 0:
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,HUMAN):
                        chessboard = copy.deepcopy(newChessboard)
                        blue_step = 1
                print np.array(chessboard)

                if ifLinked(chessboard,HUMAN):
                    clear_operation = 0
                    print 'clear operation:'
                    while clear_operation == 0:
                        candidates, warp, newChessboard = chess.getChess()
                        if same(chessboard,newChessboard):
                            clear_operation = 1
                    print np.array(chessboard)

                if ifWin(HUMAN):
                    result = HUMAN_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break
        else:
            pass
        if result == COMPUTER_WIN:
            print 'red win'
            sys.exit()
        elif result == HUMAN_WIN:
            print 'blue win'
            sys.exit()
        elif result == DRAW:
            print 'play even'
            sys.exit()
    print 'program fault'
    sys.exit()

def singleMode():
    global red
    global blue
    result = -2
    chess = readmorechess.ReadChess()
    while True:
        candidates, warp, newChessboard = chess.getChess()
        if gameStart(newChessboard) == 1 or gameStart(newChessboard) == 0:
            chessboard = copy.deepcopy(newChessboard)
            while True:
                print 'computer step:'
                step,value = computerBestMove(chessboard,-1,1)
                place(chessboard, step/9, step%9, COMPUTER)
                print np.array(chessboard)

                computer_step = 0
                while computer_step == 0:
                    candidates, warp, newChessboard = chess.getChess()
                    if same(chessboard,newChessboard):
                        if COMPUTER == 1:
                            red += 1
                        elif COMPUTER == -1:
                            blue += 1
                        computer_step = 1

                if ifWin(COMPUTER):
                    result = COMPUTER_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break

                human_step = 0
                print 'human step:'
                while human_step == 0:
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,HUMAN):
                        chessboard = copy.deepcopy(newChessboard)
                        human_step = 1
                print np.array(chessboard)

                if ifWin(HUMAN):
                    result = HUMAN_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break
        else:
            pass
        if result == COMPUTER_WIN:
            print 'computer win'
            sys.exit()
        elif result == HUMAN_WIN:
            print 'human win'
            sys.exit()
        elif result == DRAW:
            print 'play even'
            sys.exit()
    print 'program fault'
    sys.exit()

if __name__=='__main__':
    '''
    game flow:
        camera initialization->
        chessboard detection->
        environment setting(offensive position and color judgement)->
        computer step->
        waiting for complete->
        human step->
        ...
    '''
    if sys.argv[1] == 'single':
        singleMode()
    elif sys.argv[1] == 'pair':
        pairMode()
    else:
        print 'parameter error'

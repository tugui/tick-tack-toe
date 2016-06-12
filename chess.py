#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:tugui
@reference:github.com/YinWenAtBIT/Data-Structure/tree/d44e100d29b03ae1ee501886799ec35dae16413c/tic_tac_toe
"""
import sys
import copy
import readchess
import drawchess
import numpy as np

# victory and defeat condition
DRAW = 0
HUMAN_WIN = -1
COMPUTER_WIN = 1

# role with default value
HUMAN = -1 # blue
COMPUTER = 1 # red

# other chess information
step = -1 # for next place
red = 0 # for counting red chessmen
blue = 0 # for counting blue chessmen

def computerBestMove(chessboard,alpha,beta):
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif ifWin(chessboard,HUMAN):
        value = HUMAN_WIN
    else:
        value = alpha
        for i in range(9):
            if value >= beta:
                break
            if isEmpty(chessboard, i/3, i%3):
                place(chessboard, i/3, i%3, COMPUTER)
                nextMove,response = humanBestMove(chessboard, value, beta)
                unplace(chessboard, i/3, i%3)
                if response > value: # find the biggest value
                    value = response
                    step = i
    return step,value

def humanBestMove(chessboard,alpha,beta):
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif ifWin(chessboard,COMPUTER):
        value = COMPUTER_WIN
    else:
        value = beta
        for i in range(9):
            if value <= alpha:
                break
            if isEmpty(chessboard, i/3, i%3):
                place(chessboard, i/3, i%3, HUMAN)
                step,response = computerBestMove(chessboard,alpha, value)
                unplace(chessboard, i/3, i%3)
                if response < value: # find the smallest value
                    value = response
                    step = i
    return step,value

def ifWin(chessboard, role):
    if chessboard[0][0] == role and chessboard[0][1] == role and chessboard[0][2] == role:
        return True
    if chessboard[1][0] == role and chessboard[1][1] == role and chessboard[1][2] == role:
        return True
    if chessboard[2][0] == role and chessboard[2][1] == role and chessboard[2][2] == role:
        return True
    if chessboard[0][0] == role and chessboard[1][0] == role and chessboard[2][0] == role:
        return True
    if chessboard[0][1] == role and chessboard[1][1] == role and chessboard[2][1] == role:
        return True
    if chessboard[0][2] == role and chessboard[1][2] == role and chessboard[2][2] == role:
        return True
    if chessboard[0][0] == role and chessboard[1][1] == role and chessboard[2][2] == role:
        return True
    if chessboard[0][2] == role and chessboard[1][1] == role and chessboard[2][0] == role:
        return True
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
    for i in range(3):
        for j in range(3):
            if chessboard[i][j] == 0:
                return False
    return True

def gameStart(newChessboard):
    global COMPUTER
    global HUMAN
    global red
    global blue
    new_red = 0
    new_blue = 0
    for i in range(3):
        for j in range(3):
            if newChessboard[i][j] == 1:
                new_red += 1
            elif newChessboard[i][j] == -1:
                new_blue += 1
    if new_red == 0 and new_blue == 0:
        COMPUTER = -1 # blue
        HUMAN = 1
        red = 0
        blue = 0
        return 0 # computer first
    elif new_red == 1 and new_blue == 0:
        COMPUTER = -1 # blue
        HUMAN = 1
        red = 1
        blue = 0
        return 1 # computer second
    elif new_blue == 1 and new_red == 0:
        red = 0
        blue = 1
        return 1 # computer second
    else:
        return -1 # error

def same(chessboard,newChessboard):
    count = 0
    for i in range(3):
        for j in range(3):
            if chessboard[i][j] == newChessboard[i][j]:
                count += 1
    if count == 9:
        return True
    else:
        return False

def valid(chessboard,newChessboard,role):
    global red
    global blue
    count = 0
    new_red = 0
    new_blue = 0
    for i in range(3):
        for j in range(3):
            if newChessboard[i][j] == 1:
                new_red += 1
            elif newChessboard[i][j] == -1:
                new_blue += 1
            if chessboard[i][j] == newChessboard[i][j]:
                count += 1
    if role == 1 and new_red == (red + 1) and new_blue == blue and count == 8:
        red = new_red
        return True
    elif role == -1 and new_blue == (blue + 1) and new_red == red and count == 8:
        blue = new_blue
        return True
    else:
        return False

def pairMode():
    result = -2
    chess = readchess.ReadChess()
    while True:
        candidates, warp, newChessboard = chess.getChess()
        if gameStart(newChessboard) == 0: # blue first
            chessboard = copy.deepcopy(newChessboard)
            while True:
                blue_step = 0
                print 'blue step:'
                while blue_step == 0:
                    drawchess.drawChessBoard(chessboard)
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,COMPUTER):
                        chessboard = copy.deepcopy(newChessboard)
                        blue_step = 1
                print np.array(chessboard)

                if ifWin(chessboard, COMPUTER):
                    result = COMPUTER_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break

                red_step = 0
                print 'red step:'
                while red_step == 0:
                    drawchess.drawChessBoard(chessboard)
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,HUMAN):
                        chessboard = copy.deepcopy(newChessboard)
                        red_step = 1
                print np.array(chessboard)

                if ifWin(chessboard, HUMAN):
                    result = HUMAN_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break
        else:
            pass
        if result == COMPUTER_WIN:
            print 'blue win'
            sys.exit()
        elif result == HUMAN_WIN:
            print 'red win'
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
    chess = readchess.ReadChess()
    while True:
        candidates, warp, newChessboard = chess.getChess()
        if gameStart(newChessboard) == 1 or gameStart(newChessboard) == 0:
            chessboard = copy.deepcopy(newChessboard)
            while True:
                print 'computer step:'
                step,value = computerBestMove(chessboard,HUMAN_WIN,COMPUTER_WIN)
                place(chessboard, step/3, step%3, COMPUTER)
                print np.array(chessboard)

                computer_step = 0
                while computer_step == 0:
                    drawchess.drawChessBoard(chessboard)
                    candidates, warp, newChessboard = chess.getChess()
                    if same(chessboard,newChessboard):
                        if COMPUTER == 1:
                            red += 1
                        elif COMPUTER == -1:
                            blue += 1
                        computer_step = 1

                if ifWin(chessboard, COMPUTER):
                    result = COMPUTER_WIN
                    break
                if fullBoard(chessboard):
                    result = DRAW
                    break

                human_step = 0
                print 'human step:'
                while human_step == 0:
                    drawchess.drawChessBoard(chessboard)
                    candidates, warp, newChessboard = chess.getChess()
                    if valid(chessboard,newChessboard,HUMAN):
                        chessboard = copy.deepcopy(newChessboard)
                        human_step = 1
                print np.array(chessboard)

                if ifWin(chessboard, HUMAN):
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

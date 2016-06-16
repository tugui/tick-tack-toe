#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:tugui
@reference:github.com/YinWenAtBIT/Data-Structure/tree/d44e100d29b03ae1ee501886799ec35dae16413c/tic_tac_toe
"""
import sys
import copy
import random
import drawchess
import readmorechess
import numpy as np

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

enabled = [10,13,16,20,22,24,30,31,32,37,38,39,41,42,43,48,49,50,56,58,60,64,67,70]
block1 = [10,13,16,20,22,24,30,31,32]
block2 = [10,20,30,37,38,39,48,56,64]
block3 = [16,24,32,41,42,43,50,60,70]
block4 = [48,49,50,56,58,60,64,67,70]

def computerBestMove(chessboard,block,alpha,beta):
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif linked(chessboard, HUMAN):
        value = HUMAN_WIN # end of search
    else:
        value = alpha # from -5 to 5
        for i in block:
            if value >= beta:
                break
            if isEmpty(chessboard, i/9, i%9):
                place(chessboard, i/9, i%9, COMPUTER)
                # backup = copy.deepcopy(chessboard)
                # if clearCondition(backup,COMPUTER):
                    # value += 1
                nextMove,response = humanBestMove(chessboard, block, value, beta)
                unplace(chessboard, i/9, i%9)
                if response > value: # find the biggest value
                    value = response
                    step = i
    return step,value

def humanBestMove(chessboard,block,alpha,beta):
    global step
    if fullBoard(chessboard):
        value = DRAW
    elif linked(chessboard, COMPUTER):
        value = COMPUTER_WIN # end of search
    else:
        value = beta # from 5 to -5
        for i in block:
            if value <= alpha:
                break
            if isEmpty(chessboard, i/9, i%9):
                place(chessboard, i/9, i%9, HUMAN)
                # backup = copy.deepcopy(chessboard)
                # if clearCondition(backup,HUMAN):
                    # value -= 1
                nextMove,response = computerBestMove(chessboard, block, alpha, value)
                unplace(chessboard, i/9, i%9)
                if response < value: # find the smallest value
                    value = response
                    step = i
    return step,value

def linked(chessboard, role):
    if chessboard[1][1] == role and chessboard[1][4] == role and chessboard[1][7] == role:
        return True
    if chessboard[2][2] == role and chessboard[2][4] == role and chessboard[2][6] == role:
        return True
    if chessboard[3][3] == role and chessboard[3][4] == role and chessboard[3][5] == role:
        return True
    if chessboard[4][1] == role and chessboard[4][2] == role and chessboard[4][3] == role:
        return True
    if chessboard[4][5] == role and chessboard[4][6] == role and chessboard[4][7] == role:
        return True
    if chessboard[5][3] == role and chessboard[5][4] == role and chessboard[5][5] == role:
        return True
    if chessboard[6][2] == role and chessboard[6][4] == role and chessboard[6][6] == role:
        return True
    if chessboard[7][1] == role and chessboard[7][4] == role and chessboard[7][7] == role:
        return True
    if chessboard[1][1] == role and chessboard[2][3] == role and chessboard[3][3] == role:
        return True
    if chessboard[1][4] == role and chessboard[2][4] == role and chessboard[3][4] == role:
        return True
    if chessboard[1][7] == role and chessboard[2][6] == role and chessboard[3][5] == role:
        return True
    if chessboard[5][3] == role and chessboard[6][2] == role and chessboard[7][1] == role:
        return True
    if chessboard[5][4] == role and chessboard[6][4] == role and chessboard[7][4] == role:
        return True
    if chessboard[5][5] == role and chessboard[6][6] == role and chessboard[7][7] == role:
        return True
    if chessboard[1][1] == role and chessboard[4][1] == role and chessboard[7][1] == role:
        return True
    if chessboard[2][2] == role and chessboard[4][2] == role and chessboard[6][2] == role:
        return True
    if chessboard[3][3] == role and chessboard[4][3] == role and chessboard[5][3] == role:
        return True
    if chessboard[3][5] == role and chessboard[4][5] == role and chessboard[5][5] == role:
        return True
    if chessboard[2][6] == role and chessboard[4][6] == role and chessboard[6][6] == role:
        return True
    if chessboard[1][7] == role and chessboard[4][7] == role and chessboard[7][7] == role:
        return True
    return False

def clearCondition(chessboard, role):
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
    if chessboard[1][1] == role and chessboard[2][2] == role and chessboard[3][3] == role:
        chessboard[1][1] = chessboard[2][2] = chessboard[3][3] = 0
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
    global enabled
    for i in enabled:
        x = i / 9
        y = i % 9
        if chessboard[x][y] == 0:
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
    global enabled
    new_red = 0
    new_blue = 0
    for i in enabled:
        x = i / 9
        y = i % 9
        if newChessboard[x][y] == 1:
            new_red += 1
        elif newChessboard[x][y] == -1:
            new_blue += 1
        if new_red == 1:
            step = x * 9 + y
        elif new_blue == 1:
            step = x * 9 + y
    if new_red == 0 and new_blue == 0:
        return 0 # computer first
    elif new_red == 1 and new_blue == 0:
        COMPUTER = -1 # blue
        HUMAN = 1
        red = 1
        return step # computer second
    elif new_red == 0 and new_blue == 1:
        blue = 1
        return step # computer second
    else:
        return -1 # error

def same(chessboard,newChessboard):
    global enabled
    count = 0
    for i in enabled:
        x = i / 9
        y = i % 9
        if chessboard[x][y] == newChessboard[x][y]:
            count += 1
    if count == 24:
        return True
    else:
        return False

def valid(chessboard,newChessboard,role):
    global red
    global blue
    global enabled
    count = 0
    new_red = 0
    new_blue = 0
    for i in enabled:
        x = i / 9
        y = i % 9
        if newChessboard[x][y] == 1:
            new_red += 1
        elif newChessboard[x][y] == -1:
            new_blue += 1
        if chessboard[x][y] == newChessboard[x][y]:
            count += 1
        else:
            step = x * 9 + y
    if role == 1 and new_red == (red + 1) and new_blue == blue and count == 23:
        red = new_red
        return step
    elif role == -1 and new_blue == (blue + 1) and new_red == red and count == 23:
        blue = new_blue
        return step
    else:
        return 0

def findBlock(chessboard,HUMAN,step):
    global enabled
    global block1
    global block2
    global block3
    global block4
    if step == 0:
        number = random.randint(1,4)
        if number == 1:
            return block1
        elif number == 2:
            return block2
        elif number == 3:
            return block3
        elif number == 4:
            return block4
    else:
        blocklist = [block1,block2,block3,block4]
        for block in blocklist:
            if step not in block:
                continue
            count = 0
            for i in block:
                x = i / 9
                y = i % 9
                if chessboard[x][y] != 0:
                    count += 1
            if count < 9: # test value
                return block

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

                if clearCondition(chessboard,COMPUTER):
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

                if clearCondition(chessboard,HUMAN):
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
        result = gameStart(newChessboard)
        if result != -1:
            chessboard = copy.deepcopy(newChessboard)
            block = findBlock(chessboard,HUMAN,result)
            while True:
                print 'computer step:'
                step,value = computerBestMove(chessboard,block,HUMAN_WIN,COMPUTER_WIN)
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

                if clearCondition(chessboard,COMPUTER):
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

                human_step = 0
                print 'human step:'
                while human_step == 0:
                    candidates, warp, newChessboard = chess.getChess()
                    result = valid(chessboard,newChessboard,HUMAN)
                    if result != 0:
                        block = findBlock(chessboard,HUMAN,result)
                        chessboard = copy.deepcopy(newChessboard)
                        human_step = 1
                print np.array(chessboard)

                if clearCondition(chessboard,HUMAN):
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

def testMode():
    global block1
    chessboard = [[2,2,2,2,2,2,2,2,2],[2,0,2,2,0,2,2,-1,2],[2,2,0,2,0,2,1,2,2],[2,2,2,0,-1,0,2,2,2],[2,0,0,0,2,0,0,1,2],[2,2,2,1,-1,1,2,2,2],[2,2,0,2,-1,2,0,2,2],[2,0,2,2,0,2,2,0,2],[2,2,2,2,2,2,2,2,2]]
    step,value = computerBestMove(chessboard,block2,-5,5)
    print step
    print value

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
    elif sys.argv[1] == 'test':
        testMode()
    else:
        print 'parameter error'

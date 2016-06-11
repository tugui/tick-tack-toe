"""
@author:000
"""
import numpy as np
import cv2

def drawChessBoard(array):

	cv2.namedWindow("chess board",cv2.WINDOW_AUTOSIZE)

	if len(array) == 3: # the first chess board
		img = np.zeros((600,600,3),np.uint8)

		cv2.rectangle(img,(0,0),(600,600),(255,255,255),-1)

		for x in range(0,3):
			for y in range(0,3):
				cv2.rectangle(img,(y*200,x*200),(y*200+200,x*200+200),(0,0,0),2) # draw border
				if array[x][y] != 0:
					if array[x][y] == 1:
						cv2.circle(img,(y*200+100,x*200+100),50,(0,0,255),-1) # draw blue chess pieces
					else :
						cv2.circle(img,(y*200+100,x*200+100),50,(255,0,0),-1) # draw red chess pieces
				y += 1
			x += 1
	else : # the second chess board
		img = np.zeros((640,640,3),np.uint8)

		cv2.rectangle(img,(0,0),(640,640),(255,255,255),-1)

		# draw line
		cv2.rectangle(img,(80,80),(560,560),(0,0,0),3)
		cv2.rectangle(img,(160,160),(480,480),(0,0,0),3)
		cv2.rectangle(img,(240,240),(400,400),(0,0,0),3)
		cv2.line(img,(80,80),(560,560),(0,0,0),4)
		cv2.line(img,(80,560),(560,80),(0,0,0),4)
		cv2.line(img,(80,320),(560,320),(0,0,0),3)
		cv2.line(img,(320,80),(320,560),(0,0,0),3)
		cv2.rectangle(img,(242,242),(398,398),(255,255,255),-1)

		for x in range(1,8):
			for y in range(1,8):
				if array[x][y] != 0:
					if array[x][y] == 1:
						cv2.circle(img,((y-1)*80+80,(x-1)*80+80),35,(0,0,255),-1) # draw blue chess pieces
					else :
						cv2.circle(img,((y-1)*80+80,(x-1)*80+80),35,(255,0,0),-1) # draw red chess pieces
				y += 1
			x += 1

	cv2.imshow('chess board',img)
	cv2.waitKey(100)

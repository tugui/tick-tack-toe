import numpy as np
import cv2
arr = [[0,1,0],[0,-1,0],[0,0,0]]

def drawChessBoard(array):

	img = np.zeros((600,600,3),np.uint8)

	cv2.rectangle(img,(0,0),(600,600),(255,255,255),-1)

	for x in range(0,3):
		for y in range(0,3):
			cv2.rectangle(img,(x*200,y*200),(x*200+200,y*200+200),(0,0,0),2)   #draw border
			if array[x][y] != 0:
				if array[x][y] == 1:
					cv2.circle(img,(x*200+100,y*200+100),50,(0,0,255),-1)   #draw blue chess pieces
				else :
					cv2.circle(img,(x*200+100,y*200+100),50,(255,0,0),-1)	#draw red chess pieces
			y += 1
		x += 1

	cv2.imshow('chess board',img)
	cv2.waitKey(100)

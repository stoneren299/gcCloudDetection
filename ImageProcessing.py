# Author - Quazi Rabbi
# Date Created - 5/29/2018
# Version - 1.0
# Description - 
# Returns a percentage value from the supplied image for cloud 


import cv2
import numpy as np
from matplotlib import pyplot as plt



def Image_Processing(TimeUTC):
	data = np.zeros((5,5,3),dtype=np.uint8)
	dowloadPic = "Images/Image"+str(TimeUTC)+".jpg"
	img = cv2.imread(dowloadPic)
	
	# plt.subplot(121),plt.imshow(img)
	# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
	# plt.show()
	for i in range(len(data)):
		for j in range(len(data)):
			data[i,j]=img[240+j,450+i]
	
	# cv2.rectangle(img,(250,455),(245,450),(0,255,0),1)
	# cv2.imshow('original',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	
	value = np.mean(data,axis=0)
	value = np.mean(value,axis=0)
	#print percentage(value)
	return percentage(value)
	

def percentage(value):
	#RGB BLUE 1 62 125
	#RGB WHITE 255 255 255
	percentage1 = (value[0]-1)/255
	percentage2 = (value[1]-62)/255
	percentage3 = (value[2]-125)/255
	
	avgPercentage = (percentage1+percentage2+percentage3)*100/3
	
	return avgPercentage

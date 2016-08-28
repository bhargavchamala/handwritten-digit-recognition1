#randomly select few images from the data set and weave them into a bigger image
import numpy as np
import scipy.io as si
import matplotlib.pyplot as plt
import random

mat1=si.loadmat('data')
x = mat1['X']#copy pixels 5000X400
y = mat1['y']#copy labels 5000X1

a = np.array([random.randint(0,5000) for i in range(0,64)]).reshape(8,8)#randomly select 64 indexes
img = np.zeros([8,8,20,20])
label = np.ones([8,8])
for i in range(0,8):
	for j in range(0,8):
		img[i][j] = x[a[i][j]].reshape(20,20).T #copy image pixel vales
		label[i][j] = y[a[i][j]]#copy labels

print label
		
big_pic=np.zeros([160,160])#array of 100X100
#print big_pic.shape
for i in range(0,8):
	for j in range(0,8):
		for k in range(0,20):
			for l in range(0,20):
			    big_pic[i*20+k][j*20+l]=img[i][j][k][l]
			
plt.imshow(big_pic,cmap="Greys_r")#stich image
plt.show()#show image

import cv2

 
img = cv2.imread('/home/harshit/Desktop/dimensions/img/13.png', cv2.IMREAD_UNCHANGED)
 

dimensions = img.shape
 

height = img.shape[0]
width = img.shape[1] 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)

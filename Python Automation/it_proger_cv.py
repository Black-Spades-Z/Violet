import cv2
import numpy as np

#
# img = cv2.imread('images/girls.png')
#
# cv2.imshow('Result', img)
#
# cv2.waitKey(1000)
#
# new_image = cv2.resize(img, 300, 500)
# new_image = c
#
# print(img.shape)

photo = np.zeros((450,450, 3), dtype='uint8')

#photo[:] = (226,43,138)
#photo[100:150, 100:150] = 226,43,138

cv2.rectangle()


cv2.imshow('Photo', photo)
cv2.waitKey(1500)

# cap = cv2.VideoCapture('videos/jisoo.mp4')
#
# # while True:
# #     success, image = cap.read()
# #     cv2.imshow('Result', image)
# #
# #     if cv2.waitKey(10) and  0xFF == ord('q') :
# #         break
#
# camera = cv2.VideoCapture(0)
#
# camera.set(3, 500)
# camera.set(4, 300)
#
# while True:
#     success, image = camera.read()
#     if success:
#         print('Yes')
#     cv2.imshow('Result', image)
#
#     if cv2.waitKey(10) and 0xFF == ord('q') :
#         break


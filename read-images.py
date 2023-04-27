import cv2
image = cv2.imread("F:\Python project\cv2\Snipaste_2022-10-10_18-10-41.png")
resize = cv2.resize(image, (100,100))
cv2.imwrite('FIFA22', resize)



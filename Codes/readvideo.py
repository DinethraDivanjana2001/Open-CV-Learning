import cv2 as cv 

# img = cv.imread('images/largeduck.jpg')
# cv.imshow('Cat',img)



capture = cv.VideoCapture('videos/dog.mp4')  #integres- webcams , Location video 
while True :
    isTrue, frame = capture.read()  #bool that successfully read or not 
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):# if d press break the loop
      break

capture.release()
cv.destroyAllWindows()





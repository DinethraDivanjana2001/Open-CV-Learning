import cv2 as cv 
#cv.imread---methods 
img = cv.imread('images/largeduck.jpg')
cv.imshow('Cat',img)

#resizing frames - work for video images , live videos 
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dimentions = (width,height)
    return cv.resize(frame,dimentions, interpolation=cv.INTER_AREA)#resize the frame to particular dimention             

resized_image = rescaleFrame(img,scale=0.1)
cv.imshow('Image', resized_image)
cv.waitKey(0)

#reszing images  - only wotk for live videos 
def changeRes(width,height):
   capture.set(3,width)
   capture.set(4,height)

capture = cv.VideoCapture('videos/dog.mp4')  #integres- webcams , Location video 
while True :
    isTrue, frame = capture.read()  #bool that successfully read or not 
    frame_resized = rescaleFrame(frame, scale= 0.2)
    cv.imshow('video',frame)
    cv.imshow('resized frame',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):# if d press break the loop
      break

capture.release()
cv.destroyAllWindows()


import cv2
# creating object
video = cv2.VideoCapture(0)

a = 0

img_counter = 0

while (True):
    a = a + 1
    # creating window frame
    check, frame = video.read()
    # converting the image into grey scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # naming the window and color
    cv2.imshow('capturing', gray)
    # check and frame prints the array of the video object
    print(check)
    print(frame)
    # refresh rate
    key = cv2.waitKey(1)
    # press Q for quitting the frame
    if key == ord('q'):
        break

    # Press s for saving the image
    if key == ord('s'):
        # if you have a better webcam then change the image name to test.png and change it in img_processing.py file too
        #for better check
        img_name = "{}.png".format(img_counter)
        # capturing the video array at the same time
        cv2.imwrite(img_name, frame)
        img_counter += 1
        break

# for closing camera
video.release()
cv2.destroyAllWindows()

# img=cv2.imread("test2.png",0)
# cv2.imshow('test2.png',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

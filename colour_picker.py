import cv2
import numpy


def show_colour(event, x, y, flags, param):
    #if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        bgr_colour = tuple(frame[y][x].tolist())
        rgb_colour = bgr_colour[::-1]
        colour_image[:] = bgr_colour
        #write the rgb of the colour in text on the image
        cv2.putText(colour_image,
                    str(rgb_colour),
                    (50, 50),
                    font, 1,
                    (255 - bgr_colour[0], 255 - bgr_colour[1], 255 - bgr_colour[2]),
                    2,
                    cv2.LINE_4)
        #display colour screen
        cv2.imshow('colour', colour_image)


font = cv2.FONT_HERSHEY_SIMPLEX

vid = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.namedWindow('colour')
colour_image = numpy.zeros((380, 540, 3), numpy.uint8)
cv2.setMouseCallback('frame', show_colour)

while(True):
    ret, frame = vid.read()
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, 
                       interpolation = cv2.INTER_CUBIC)
    
    #display video
    cv2.imshow('frame', frame)
    

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
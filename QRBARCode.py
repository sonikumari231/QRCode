import cv2
import numpy as np
from pyzbar.pyzbar import decode

# define a video capture object
vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    for barcode in decode(frame):
        #print(barcode.data)
        myData =barcode.data.decode('utf-8')
        print(myData)
        pts =np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
#!/home/ml/anaconda3/bin/python3
import sys
import signal
import os
import subprocess
import cv2

def extractFrames(filename,pathIn, pathOut):

 
    cap = cv2.VideoCapture(pathIn)
    count = 0
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, filename + "{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 700
            cap.set(1,count)
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



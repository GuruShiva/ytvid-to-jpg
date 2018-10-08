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
            count += 1000
            cap.set(1,count)
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def get_vid_file(filename, vid_dir_file_list, pathOut):
            dir_name = os.path.basename(vid_dir_file_list)
            files = os.listdir(vid_dir_file_list)
            for file in files:
                if file.endswith(".mp4"):
                    pathIn = vid_dir_file_list + file
                    extractFrames(filename,pathIn,pathOut)
def main():
    filename = "foo"
    pathIn = "/home/username/foobarin/" + filename + "/"
    pathOut = "/home/username/foobarout/" + filename + "/"
    get_vid_file(filename,pathIn, pathOut)


if __name__ == '__main__':
    main()
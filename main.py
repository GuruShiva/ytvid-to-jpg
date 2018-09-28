#!/usr/bin/env python3
import sys
import signal
import os
import json
import youtube_dl
import cv2


def signal_handler(sig, frame):
    print("\nCaught SIGINT")
    print("Program terminated")
    sys.exit(1)


def checkdir():
    dir_exists = os.path.isdir('./main_dl')
    if dir_exists == True:
        pass
    else:
        print("Download directory doesn't exist, creating it now.")
        os.makedirs('./main_dl')


def downloader():
    global file_title
    max_downloads = str(10)
    search_title = str(input("Enter search query :\n"))
    amount = str(input("How many videos to download?: "))
    ydl_opts = {'default_search': "ytsearch", 'forcejson': False, 'forceurl': False, 'skip_download': False, 'max_downloads': max_downloads}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        
        result = ydl.extract_info("ytsearch{}:{}".format(amount, search_title))
# def splitter():
#     cap = cv2.VideoCapture(file_title)
#     try:
#         if not os.path.exists('data'):
#             os.makedirs('data')
#     except OSError:
#         print ('There was an error creating the data directory')
#     currentFrame = 0
#     while(True):
#     # Capture frame-by-frame
#         ret, frame = cap.read(
#     # Saves the current frame in jpg file
#     name = './data/frame' + str(currentFrame) + '.jpg'
#     print ('Creating...' + name)
#     cv2.imwrite(name, frame)
#     # To stop duplicate images
#     currentFrame += 1
# # When everything is done, release the capture
#     cap.release()
#     cv2.destroyAllWindows()



def main():
    signal.signal(signal.SIGINT, signal_handler)
    downloader()
    # splitter()

if __name__ == "__main__":
    main()

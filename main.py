#!/usr/bin/env python3
import argparse
import sys
import signal
import os
import json
import subprocess
import shutil
import youtube_dl


def signal_handler(sig, frame):
    print("\nCaught SIGINT")
    print("Program terminated")
    sys.exit(1)


def walk():
    # Set the script directory path to a variable to later come back to because
    # YDL sucks in setting a proper download destination
    global absolutePath, categoryName
    absolutePath = sys.path[0]
    categoryName = input("What is the category name?:\n")
    print("{} doesn't exist, creating it now.".format(categoryName))
    counter = 0
    for files in os.walk('{}/data'.format(absolutePath)):
        counter += 1
        os.makedirs('{}_{}'.format(categoryName, counter))
    for file_name in absolutePath:
        full_file_name = os.path.join(absolutePath, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy2(full_file_name, categoryName)



def downloader():
    absolutePath = sys.path[0]
    os.makedirs('data')
    os.chdir('{}/data'.format(absolutePath))
    max_downloads = 10
    ydl_opts = {'forcefilename': True, 'forcetitle': True, 'format':'mp4', 'outtmpl': '%(title)s',}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        search_title = str(input("Enter title:\n"))
        amount = str(input(
        "How many videos would you like to be downloaded?\n"))
        result = ydl.extract_info("ytsearch{}:{}".format(amount, search_title))
    walk()


def fileList(src):
    counter = 0
    matches = []
    for root, dirnames, filenames in os.walk(src):
        for filename in filenames:
            if filename.endswith(('mp4','mkv', '.mov', '.MOV', '.avi', '.mpg')):
                matches.append(os.path.join(root, filename))
                counter += 1
    return matches



# Trying to simulate the same os walk loop to redirect and render the frames
# Does't work yet
def splitter():
    global categoryName
    absolutePath = sys.path[0]
    dataPath = "{}/data".format(absolutePath)
    counter = 1
    for file_name in absolutePath:
        os.chdir('{}_{}'.format(categoryName, counter))
        counter += 1
        cwd = os.getcwd()
        print("Changed the working directory to {}".format(cwd))
        global currentFrame, currentSeek
        currentFrame = str(input("Which frame should we start from?:\n"))
        currentSeek = "00:00:00.000"
        frameName = "frame%04d.jpg"
        fileName = fileList('{}/data/{}_{}'.format(absolutePath, categoryName, counter))
        i = 0
        while i < len (fileName):
            subprocess.run(
            ["ffmpeg","-i",fileName, currentSeek, "-vframes", currentFrame, frameName, \
            "-hide_banner"]
                          )
            i += 1

def main():
    signal.signal(signal.SIGINT, signal_handler)
    downloader()
    splitter()


if __name__ == "__main__":
    main()

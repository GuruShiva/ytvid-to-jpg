#!/home/ml/anaconda3/bin/python3
import sys
import signal
import os
import json
import subprocess
import shutil
import youtube_dl
import extract_frame
import yt_downloader
from datetime import datetime

def signal_handler(sig, frame):
    print("\nCaught SIGINT")
    print("Program terminated")
    sys.exit(1)

def get_config(absolutePath):
    with open('{}/data/config/data.json'.format(absolutePath), 'r') as json_data_file:
        data = json.loads(json_data_file.read())
        return (data)



def get_vid_class(vid_dir, data):
    for item in data['data']:
        class_name =  [item['category']]
        for c in class_name:
            mk_vid_cat_dir(vid_dir,c)


def get_img_class(img_dir, data):
    for item in data['data']:
        class_name =  [item['category']]
        for c in class_name:
            mk_img_cat_dir(img_dir,c)

def mk_data_dir(absolutePath):
    vid_data_dir = absolutePath + "/data/videos"
    img_data_dir = absolutePath + "/data/images"
    if not os.path.exists(vid_data_dir):
        print ("Path does not exist. Creating directory")
        os.makedirs(vid_data_dir)
    if not os.path.exists(img_data_dir):
        print ("Path does not exist. Creating directory")
        os.makedirs(img_data_dir)
    
    return vid_data_dir, img_data_dir
    

def mk_vid_cat_dir(vid_dir, dir):
    mkdir_path = vid_dir + '/' + dir
    if not os.path.exists(mkdir_path):
        print ("Path does not exist. Creating directory")
        os.makedirs(mkdir_path)


def mk_img_cat_dir(img_dir, dir):
    mkdir_path = img_dir + '/' + dir
    if not os.path.exists(mkdir_path):
        print ("Path does not exist. Creating directory")
        os.makedirs(mkdir_path)


def get_search_query(vid_dir,data):
    for item in data['data']:
        cats =  [item['category']]
        search = [item['search']]
        for c in cats:
            class_dir = vid_dir + '/' + c
            
        for s in search:
            for k,v in s.items():
                yt_downloader.downloader(class_dir, v)
                


def get_vid_filepath(vid_dir):
    subdir= next(os.walk(vid_dir))[1]
    return ([vid_dir +'/'+ s for s in subdir])


def get_vid_file(vid_dir_file_list,img_dir):
    for i in vid_dir_file_list:
            dir_name = os.path.basename(i)
            files = os.listdir(i)
            img_dir_class = img_dir + '/' + dir_name + '/'
            for file in files:
                if file.endswith(".mp4"):
                    splitter(dir_name, i + '/' + file, img_dir_class)

def splitter(dir_name, file, img_dir_class):
        file_name = dir_name
        file = file
        output_path = img_dir_class
        extract_frame.extractFrames(file_name,file,output_path)
        

def main():
    start=datetime.now()
    signal.signal(signal.SIGINT, signal_handler)
    absolutePath = sys.path[0]
    data=(get_config(absolutePath))
    dirs= mk_data_dir(absolutePath)
    vid_dir = (dirs[0])
    img_dir = (dirs[1])
    get_vid_class(vid_dir, data)
    get_img_class(img_dir,data)
    search_query = get_search_query(vid_dir,data)
    vid_dir_file_list = get_vid_filepath(vid_dir)
    get_vid_file(vid_dir_file_list, img_dir)
    print (datetime.now()-start)
    print ("FINISHED!")
  


if __name__ == "__main__":
    main()

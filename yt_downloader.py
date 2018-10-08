#!/home/ml/anaconda3/bin/python3
import sys
import signal
import os
import json
import subprocess
import youtube_dl


def downloader(class_dir, search_query):
    
    os.chdir(class_dir)
    max_downloads = str(1)
    amt_downloads = str(1)
    ydl_opts = {'default_search': "ytsearch", 'forcejson': False, 'forceurl': False, 'skip_download': False, 'format':'bestvideo[ext=mp4]', 'max_downloads': max_downloads}
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        
        result = ydl.extract_info("ytsearch{}:{}".format(amt_downloads, search_query))


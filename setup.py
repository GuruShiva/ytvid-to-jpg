#!/usr/bin/env python3
import subprocess

try:
    import cv2, youtube_dl

except ImportError:
    subprocess.run(['pip3', 'install', '--user', '-r', 'requirements.txt'])

finally:
    import cv2, youtube_dl
    print("Setup is done.")

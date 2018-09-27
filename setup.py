#!/usr/bin/env python3
import pip

try:
    import cv2, youtube_dl

except ImportError:
    pip.main(['install', '-r', '--user', 'requirements.txt'])

finally:
    import cv2, youtube_dl
    print("Setup is done.")

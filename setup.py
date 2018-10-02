#!/usr/bin/env python3
import subprocess

try:
    import youtube_dl

except ImportError:
    subprocess.run(['pip3', 'install', '--user', '-r', 'requirements.txt'])

finally:
    import youtube_dl
    print("Setup is done.")

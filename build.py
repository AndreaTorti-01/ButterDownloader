import PyInstaller.__main__
import os
import shutil
from pathlib import Path

PyInstaller.__main__.run([
    'ButterDownloader.py',
    '--onefile',
    '--noconsole'
])

shutil.move(Path("dist/ButterDownloader.exe"), "ButterDownloader.exe")


os.remove("ButterDownloader.spec")

try:
    shutil.rmtree("build")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

try:
    shutil.rmtree("dist")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
#!/usr/bin/env python


import subprocess
import os

subprocess.Popen("pyinstaller --onefile --windowed main.py AI.py Board.py Game.py")
os.rename("./dist/main.exe", "./gomoku.exe")


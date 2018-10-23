#!/usr/bin/env python3


import subprocess
import os

if __name__ == "__main__":
    subprocess.call(["pyinstaller", "--onefile", "main.py", "AI.py", "Board.py", "Game.py"])
    try:
        os.rename("./dist/main.exe", "./gomoku.exe")
    except:
        os.rename("./dist/main", "./gomoku")

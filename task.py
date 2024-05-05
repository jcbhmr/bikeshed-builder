#!/usr/bin/env python3
import sys
import os
import time
import subprocess
import pathlib
import shutil
import platform

def build():
    subprocess.run(["pyinstaller", "-y", "--collect-all", "bikeshed", "bin/bikeshed.py"])

task_name = sys.argv[1] or 0/0
task = { "build": build }[task_name] or 0/0
task()

#!/usr/bin/env python3
import sys
import subprocess
import shutil

def build():
    subprocess.run([shutil.which("pyinstaller"), "-y", "--collect-all", "bikeshed", "bikeshed.py"])

task_name = sys.argv[1] or 0/0
task = { "build": build }[task_name] or 0/0
task()

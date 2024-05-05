#!/usr/bin/env python3.12

import sys
import os
import time
import subprocess

def build():
    subprocess.run(["python3.12", "-m", "venv", "env"])
    if os.name == "nt":
        subprocess.run(["env\\Scripts\\activate.bat"], shell=True)
    else:
        subprocess.run(["source", "env/bin/activate"], shell=True)
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

task_name = sys.argv[1] or raise Exception("no task")
task = { "build": build }[task_name] or raise Exception("no such task")
task()

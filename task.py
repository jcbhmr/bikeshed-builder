#!/usr/bin/env python3.12
import sys
import os
import time
import subprocess
import pathlib
import shutil
import platform

PYTHON_VERSION = "3.12"
PYTHON = "python"+PYTHON_VERSION

def setup():
    if os.name == "nt":
        if not shutil.which(PYTHON):
            subprocess.run(["winget", "install", "-e", "--id", "Python.Python."+PYTHON_VERSION])
    elif 'ubuntu' in platform.version().lower():
        if not shutil.which(PYTHON):
            subprocess.run(["sudo", "apt-get", "install", "-y", PYTHON, PYTHON+"-venv", PYTHON+"-dev"])
    elif 'darwin' in platform.version().lower():
        if not shutil.which(PYTHON):
            subprocess.run(["brew", "install", PYTHON])
    else:
        print(f"WARNING: Unsupported platform. Please install {PYTHON} manually.")

def build():
    os.chdir("bikeshed")

    # if not os.path.exists("bikeshed/pyinstaller_main.py"):
    if True:
        with open("bikeshed/pyinstaller_main.py", "w") as f:
            f.write("""
from bikeshed.cli import main
main()
""")

    if not os.path.exists("env"):
        if os.name == "nt":
            subprocess.run(["py", "-"+PYTHON_VERSION, "-m", "venv", "env"])
        else:
            subprocess.run([PYTHON, "-m", "venv", "env"])

    cmd = """
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install pyinstaller
pyinstaller -y --name bikeshed bikeshed/pyinstaller_main.py
pyinstaller -y --onefile --name bikeshed-onefile bikeshed/pyinstaller_main.py
"""

    if os.name == "nt":
        p = subprocess.Popen([os.path.abspath("env/Scripts/activate")], stdin=subprocess.PIPE, text=True)
        p.communicate(cmd)
        p.wait()
    else:
        p = subprocess.Popen(["/usr/bin/env", "sh"], stdin=subprocess.PIPE, text=True)
        p.communicate(f". env/bin/activate\n{cmd}")
        p.wait()

    os.chdir("..")

    pathlib.Path("dist").mkdir(parents=True, exist_ok=True)
    shutil.move("bikeshed/dist/bikeshed", "dist/bikeshed")
    if os.name == "nt":
        shutil.move("bikeshed/dist/bikeshed-onefile.exe", "dist/bikeshed-onefile.exe")
    else:
        shutil.move("bikeshed/dist/bikeshed-onefile", "dist/bikeshed-onefile")

task_name = sys.argv[1] or 0/0
task = { "setup": setup, "build": build }[task_name] or 0/0
task()

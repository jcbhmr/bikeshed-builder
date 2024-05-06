#!/usr/bin/env python3
import sys
import subprocess
import shutil


def build():
    subprocess.run(
        [
            shutil.which("pyinstaller"),
            "-y",
            "--collect-all=bikeshed",
            "--name=bikeshed",
            "bikeshed/__main__.py",
        ]
    )


def format_():
    subprocess.run(
        [
            shutil.which("black"),
            ".",
        ]
    )
    subprocess.run(
        [
            shutil.which("shfmt"),
            "--write"
            ".",
        ]
    )

task_name = sys.argv[1] or 0 / 0
task = {"build": build, "format": format_}[task_name] or 0 / 0
task()

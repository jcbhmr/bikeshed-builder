import subprocess
import os
import sys
import platform
import shutil


def test():
    if not os.path.exists("dist"):
        args = [shutil.which("poe"), "build"]
        print(f"$ {' '.join(args)}")
        subprocess.run(args)

    exe_ext = ".exe" if os.name == "nt" else ""
    args = [os.path.abspath("dist/bikeshed/bikeshed" + exe_ext), "--version"]
    print(f"$ {' '.join(args)}")
    subprocess.run(args)

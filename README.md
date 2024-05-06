# Bikeshed builder

🚲 Bundles Bikeshed for use without Python & pip

## Installation

ℹ These installation steps will install **the Bikeshed project** itself (the `bikeshed` binary), not the builder infrastructure metapackage.

You can install Bikeshed straight from [the GitHub releases tab](https://github.com/jcbhmr/bikeshed-builder/releases/latest) or by using the `install.sh` script which will automagically✨ choose the right binary for your platform.

<dl>
<dt>Linux, macOS, and Git Bash
<dd>

```sh
curl -fsSL https://jcbhmr.me/bikeshed-builder/install.sh | sh
```

<dt>Windows
<dd>

```ps1
powershell -c "irm https://jcbhmr.me/bikeshed-builder/install.ps1 | iex"
```

</dl>

## Usage

This project is intended to be used & integrated with software that works better without the Python & pip requirements that the official Bikeshed distribution method uses. You can also use it as a standalone way to install Bikeshed without a Python environment.

## Development

<details><summary>First install the complete Python 3.12 environment</summary>

<dl>
<dt>Ubuntu
<dd>

```sh
sudo apt install python3.12 python3.12-dev python3.12-venv
```

<details><summary>You might need deadsnakes</summary>

Your Ubuntu distribution might not have Python 3.12 in its repositories. You can add [the deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) to get more Python versions for more Ubuntu versions.

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

</details>

<dt>macOS
<dd>

```sh
brew install python@3.12
```

<dt>Windows
<dd>

Install Python 3.12 from the [official Python website](https://www.python.org/downloads/) for Windows.

</dl>
</details>

Make sure you have a Python 3.12 installation setup that includes the magic stuff that PyInstaller needs.

<details><summary>Next, setup your virtual environment (recommended for dev machines)</summary>

Create the virtual environment first:

<dl>
<dt>Linux & macOS
<dd>

```sh
python3.12 -m venv .venv
```

<dt>Windows
<dd>

```cmd
py -3.12 -m venv .venv
```

</dl>

Then activate your virtual environment for the current terminal:

<dl>
<dt>Linux & macOS Bash
<dd>

```sh
. .venv/bin/activate
```

<dt>Windows cmd
<dd>

```cmd
call .venv\Scripts\activate
```

<dt>Windows PowerShell
<dd>

```pwsh
. .venv/Scripts/Activate.ps1
```

</dl>
</details>

And install the dependencies using pip:

```sh
pip install -e .[dev]
```

And now you're ready to start developing! 🚀

`task.py` has the `build` task which will build the Bikeshed binary for your current platform. You can run it like this:

```sh
python task.py build
```

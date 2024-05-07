# Bikeshed builder

🚲 Bundles Bikeshed for use without Python & pip

<p align=center>
  <img width=400 src="https://github.com/jcbhmr/bikeshed-builder/assets/61068799/2afa0995-1048-424f-b31e-112119cca064">
</p>

🐍 Uses [PyInstaller](https://pyinstaller.org/en/stable/) \
🏭 Compiles [the `bikeshed` PyPI package](https://pypi.org/project/bikeshed/) to a standalone program \
[🚚 Distributed via GitHub releases](https://github.com/jcbhmr/bikeshed-builder/releases) \
💻 Builds for Windows x64, macOS M1 and Intel, and Linux x64

## Installation

![GitHub](https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=)
![Shell](https://img.shields.io/static/v1?style=for-the-badge&message=Shell&color=4EAA25&logo=GNU+Bash&logoColor=FFFFFF&label=)
![PowerShell](https://img.shields.io/static/v1?style=for-the-badge&message=PowerShell&color=5391FE&logo=PowerShell&logoColor=FFFFFF&label=)

🛑 If possible you should install Bikeshed directly from [the `bikeshed` PyPI package](https://pypi.org/project/bikeshed/) as is [officially recommended on the Bikeshed Documentation website](https://speced.github.io/bikeshed/#install-final).

```sh
pipx install bikeshed
```

You can install Bikeshed builds from [the GitHub releases tab](https://github.com/jcbhmr/bikeshed-builder/releases).

## Usage

![Windows](https://img.shields.io/static/v1?style=for-the-badge&message=Windows&color=0078D4&logo=Windows&logoColor=FFFFFF&label=)
![Linux](https://img.shields.io/static/v1?style=for-the-badge&message=Linux&color=222222&logo=Linux&logoColor=FCC624&label=)
![macOS](https://img.shields.io/static/v1?style=for-the-badge&message=macOS&color=000000&logo=macOS&logoColor=FFFFFF&label=)

This project is intended to be used & integrated with software that works better without the Python & pip requirements that the official Bikeshed distribution method uses. You can also use it as a standalone way to install Bikeshed without a Python environment.

## Development

![Python](https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label=)
![Poetry](https://img.shields.io/static/v1?style=for-the-badge&message=Poetry&color=60A5FA&logo=Poetry&logoColor=FFFFFF&label=)

```sh
pipx install poetry poethepoet
```

```sh
poetry install
```

```sh
poe test
```

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

```sh
pipx install poetry poethepoet
```

```sh
poetry install
```

```sh
poe test
```

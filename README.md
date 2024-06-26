# Bikeshed builder

🚲 Bundles [Bikeshed](https://speced.github.io/bikeshed/) for use without Python & pip

<p align=center>
  <a href="https://github.com/jcbhmr/bikeshed-builder/releases/latest"><img src="https://github.com/jcbhmr/bikeshed-builder/assets/61068799/85929f40-991a-4de8-b212-86f85a7fed5c"></a>
</p>

<p align=center>
  <a href="https://github.com/jcbhmr/bikeshed-builder/releases">GitHub releases (this project)</a>
  | <a href="https://speced.github.io/bikeshed/">Official Bikeshed website</a>
  | <a href="https://pypi.org/project/bikeshed/">Official <code>bikeshed</code> PyPI package</a>
  | <a href="https://github.com/speced/bikeshed">Official Bikeshed GitHub</a>
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

You can get Bikeshed builds built by this bikeshed-builder project from [the GitHub releases tab](https://github.com/jcbhmr/bikeshed-builder/releases); these are unofficial. You can use ~~[go-bikeshed](https://github.com/jcbhmr/go-bikeshed)~~ 🚧 under construction, ~~[bikeshed-rs](https://github.com/jcbhmr/bikeshed-rs)~~ 🚧 under construction, or ~~[bikeshed.js](https://github.com/jcbhmr/bikeshed.js)~~ 🚧 under construction to integrate bikeshed-builder binaries with your favorite language's package management toolchain. 😉

## Usage

![Windows](https://img.shields.io/static/v1?style=for-the-badge&message=Windows&color=0078D4&logo=Windows&logoColor=FFFFFF&label=)
![Linux](https://img.shields.io/static/v1?style=for-the-badge&message=Linux&color=222222&logo=Linux&logoColor=FCC624&label=)
![macOS](https://img.shields.io/static/v1?style=for-the-badge&message=macOS&color=000000&logo=macOS&logoColor=FFFFFF&label=)

This project is intended to be used & integrated with software that works better without the Python & pip requirements that the official Bikeshed distribution method uses. You can also use it as a standalone way to install Bikeshed without a Python environment. For example an npm redistribution of the Bikeshed project to be `npm install <bikeshed_package_name>` would not want to require a particular Python environment. Instead, they would opt for a premade AiO binary/package like bikeshed-builder! 😉

Here are the relevant URLs that you would use in your code to fetch releases from this bikeshed-builder project:

```
https://github.com/jcbhmr/bikeshed-builder/releases/download/$TAG/bikeshed-arm64-apple-darwin.tar.gz
https://github.com/jcbhmr/bikeshed-builder/releases/download/$TAG/bikeshed-x86_64-apple-darwin.tar.gz
https://github.com/jcbhmr/bikeshed-builder/releases/download/$TAG/bikeshed-x86_64-pc-windows-msvc.zip
https://github.com/jcbhmr/bikeshed-builder/releases/download/$TAG/bikeshed-x86_64-unknown-linux-gnu.tar.gz
```

ℹ bikeshed-builder matches the Bikeshed versions as they are released. `bikeshed==4.1.6` would be built & tagged as `v4.1.6`. Don't forget the `v` prefix! 😁

Programs are encouraged to pin each of their versions to an exact version of Bikeshed and then update Bikeshed as a dependency as opposed to always fetching the latest bikeshed-builder release.

The `.zip` and `.tar.gz` archives all have the same layout:

```
.
├── bikeshed
└── _internal/
    └── ...
```

Note that everything is in the root folder! That means if you want to extract the contents to `~/.bikeshed` here's what you might do:

```sh
mkdir ~/.bikeshed
tar -xzvf bikeshed-x86_64-unknown-linux-gnu.tar.gz -C ~/.bikeshed
```

## Development

![Python](https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label=)
![Poetry](https://img.shields.io/static/v1?style=for-the-badge&message=Poetry&color=60A5FA&logo=Poetry&logoColor=FFFFFF&label=)

This entire project hinges on 1) getting the `bikeshed` PyPI package to properly install, 2) creating a wrapper script that invokes the bikeshed CLI, and then 3) properly wrapping all that up with PyInstaller. There's also 4) get it to build on GitHub Actions and 5) uploading the public release artifacts.

[Python's packaging and dependency landscape is a mess.](https://chriswarrick.com/blog/2024/01/15/python-packaging-one-year-later/) This project uses [Poetry](https://python-poetry.org/), the most popular Python package manager (excluding plain `pip`). [Poe the Poet](https://poethepoet.natn.io/) is used as a task runner since [Poetry doesn't have a built-in task runner](https://github.com/python-poetry/poetry/issues/2496). You can install these tools using [pipx](https://pipx.pypa.io/stable/).

```sh
pipx install poetry poethepoet
```

After cloning this project getting started is easy!

```sh
poetry install
```

And then you can run the `build` or `test` tasks to make sure everything works.

```sh
poe test
```

To create a new release:

1. Change the `bikeshed` version dependency in `pyproject.toml`.
2. Update the `version` field in `pyproject.toml` to reflect the new Bikeshed version with the appropriate suffix. This version field is read by [the gh release create workflow](https://github.com/jcbhmr/bikeshed-builder/blob/main/.github/workflows/gh-release-create.yml).
3. Go to [the gh release create workflow page](https://github.com/jcbhmr/bikeshed-builder/actions/workflows/gh-release-create.yml)
4. Manually run the workflow. You can choose to create a draft instead of immediately publishing it.

You can use `rc1` or similar prereleases to try things out if needed but `draft: true` should suffice in most cases to make sure things look good.

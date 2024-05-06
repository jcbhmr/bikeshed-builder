#!/bin/sh
# Keep this script simple and easily auditable!
set -e
if [ -n "$DEBUG" ]; then
	set -x
fi

if [ "$OS" = "Windows_NT" ]; then
	target="x86_64-pc-windows-msvc"
else
	case $(uname -sm) in
	"Darwin x86_64") target="x86_64-apple-darwin" ;;
	"Darwin arm64") target="aarch64-apple-darwin" ;;
	*) target="x86_64-unknown-linux-gnu" ;;
	esac
fi

if [ "$OS" = "Windows_NT" ]; then
	archive_ext=".zip"
else
	archive_ext=".tar.gz"
fi

if [ "$OS" = "Windows_NT" ]; then
	exe_ext=".exe"
else
	exe_ext=""
fi

file="bikeshed-$target$archive_ext"

safe_bikeshed_install="${BIKESHED_INSTALL:-$HOME/.bikeshed}"
mkdir -p "$safe_bikeshed_install"

if [ -n "$1" ]; then
	url="https://github.com/jcbhmr/bikeshed-builder/releases/download/v$1/$file"
else
	url="https://github.com/jcbhmr/bikeshed-builder/releases/latest/download/$file"
fi

echo "Downloading Bikeshed from $url"
curl -fsSL "$url" -o "$safe_bikeshed_install/$file"
if [ "$archive_ext" = ".zip" ]; then
	unzip -d "$safe_bikeshed_install" -o "$safe_bikeshed_install/$file"
else
	tar -xzf "$safe_bikeshed_install/$file" -C "$safe_bikeshed_install"
fi
rm -f "$safe_bikeshed_install/$file"

chmod +x "$safe_bikeshed_install/bikeshed$exe_ext"

echo "Bikeshed installed to $safe_bikeshed_install/*"

if command -v bikeshed >/dev/null; then
	echo "Run 'bikeshed --help' to get started"
else
	case $SHELL in
	/bin/zsh) shell_profile=".zshrc" ;;
	*) shell_profile=".bashrc" ;;
	esac
	cat <<EOF
Manually add the directory to your \$HOME/$shell_profile (or similar)
  export safe_bikeshed_install="$safe_bikeshed_install"
  export PATH="\$safe_bikeshed_install/bin:\$PATH"

Example:
  echo 'export BIKESHED_INSTALL="$safe_bikeshed_install"' >> ~/$shell_profile
  echo 'export PATH="\$BIKESHED_INSTALL/bin:\$PATH"' >> ~/$shell_profile

Run '$safe_bikeshed_install/bikeshed --help' to get started
EOF
fi

echo "Stuck? Open an Issue https://github.com/jcbhmr/bikeshed-builder/issues"

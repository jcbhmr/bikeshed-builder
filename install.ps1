#!/usr/bin/env pwsh
# Keep this script simple and easily auditable!
$ErrorActionPreference = 'Stop'

if ($v) {
  $Version = "${v}"
}
if ($Args.Length -eq 1) {
  $Version = $Args.Get(0)
}

$SafeBikeshedInstall = $env:BIKESHED_INSTALL
if (!$SafeBikeshedInstall) {
  $SafeBikeshedInstall = "${Home}\.bikeshed"
}

$Target = 'x86_64-pc-windows-msvc'
$File = "bikeshed-${Target}.zip"

$URL = if ($Version) {
  "https://github.com/jcbhmr/bikeshed-builder/releases/download/v${Version}/$File"
} else {
  "https://github.com/jcbhmr/bikeshed-builder/releases/latest/download/$File"
}

if (!(Test-Path "$SafeBikeshedInstall")) {
  New-Item "$SafeBikeshedInstall" -ItemType Directory | Out-Null
}

curl.exe -fsSL "$URL" -o "$SafeBikeshedInstall\$File"
Expand-Archive -Path "$SafeBikeshedInstall\$File" -DestinationPath "$SafeBikeshedInstall" -Force
Remove-Item "$SafeBikeshedInstall\$File"

$User = [System.EnvironmentVariableTarget]::User
$Path = [System.Environment]::GetEnvironmentVariable('Path', $User)
if (!(";${Path};".ToLower() -like "*;$SafeBikeshedInstall;*".ToLower())) {
  [System.Environment]::SetEnvironmentVariable('Path', "${Path};$SafeBikeshedInstall", $User)
  $Env:Path += ";$SafeBikeshedInstall"
}

Write-Output "Bikeshed was installed successfully to $SafeBikeshedInstall\bikeshed.exe"
Write-Output "Run 'bikeshed --help' to get started"
Write-Output "Stuck? Open an Issue https://github.com/jcbhmr/bikeshed-builder/issues"
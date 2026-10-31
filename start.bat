@echo off
REM Launch both portable tools side-by-side from external/
start "" "%~dp0external\Wireshark\Wireshark.exe"
start "" "%~dp0external\AngryIPScanner\ipscan.exe"

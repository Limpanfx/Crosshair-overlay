@echo off
chcp 65001 >nul
color A
title crosshair

echo.
echo Download requirements? (y/n)
set /p choice="Enter your choice: "

if /i "%choice%"=="y" (
    echo Installing requirements...
    pip install PyQt5
    echo Requirements installed.
) else (
    echo Skipping requirements installation.
)

python crosshair.py
pause

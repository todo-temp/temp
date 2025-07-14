@echo off
mkdir %APPDATA%\Todo-app
cd %APPDATA%\Todo-app
cls
python --version >nul
IF %errorlevel% equ 0 (
	goto installed
)
cls
echo "Python is not installed, please reffer to: https://www.python.org/downloads/"
set /p temp=
exit
:installed
curl https://raw.githubusercontent.com/todo-temp/temp/main/installer.py -o installer.py
python installer.py

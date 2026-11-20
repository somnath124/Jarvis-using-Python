@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ========================================
echo   Voice AI Assistant - Setup
 echo ========================================
echo.

where py >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python launcher ^(py^) was not found.
    echo Install Python 3.13 x64 from python.org and enable the launcher.
    pause
    exit /b 1
)

py -3.13 --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3.13 is not installed.
    echo.
    echo Your project uses PyAudio and Kivy. PyAudio 0.2.14 has a Windows
    echo wheel for CPython 3.13, while your Python 3.14 environment is not
    echo supported by this dependency set.
    echo.
    echo Install Python 3.13 x64, then run setup.bat again.
    pause
    exit /b 1
)

echo Creating Python 3.13 virtual environment...
if exist venv rmdir /s /q venv
py -3.13 -m venv venv
if errorlevel 1 (
    echo ERROR: Could not create the virtual environment.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 goto :fail

echo.
echo Installing project dependencies...
pip install -r requirements.txt
if errorlevel 1 goto :fail

echo.
echo Running dependency check...
python check_setup.py
if errorlevel 1 goto :fail

echo.
echo ========================================
echo Setup completed successfully.
echo ========================================
echo.
echo IMPORTANT: Put your Cohere API key in .env:
echo COHERE_API_KEY=your_actual_key_here
echo.
echo Then double-click voiceai.bat
pause
exit /b 0

:fail
echo.
echo ========================================
echo Setup failed. Read the error above.
echo ========================================
pause
exit /b 1

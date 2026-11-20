@echo off
setlocal
cd /d "%~dp0"

if not exist venv\Scripts\python.exe (
    echo Virtual environment not found.
    echo.
    call setup.bat
    if errorlevel 1 (
        pause
        exit /b 1
    )
)

call venv\Scripts\activate.bat
python frontend.py
set EXITCODE=%ERRORLEVEL%
if not "%EXITCODE%"=="0" echo.
if not "%EXITCODE%"=="0" echo The assistant stopped with error code %EXITCODE%.
pause
exit /b %EXITCODE%

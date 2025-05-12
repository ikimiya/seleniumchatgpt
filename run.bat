@echo off
REM Create a virtual environment in the .venv folder if it doesn't exist
IF NOT EXIST ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate the virtual environment
CALL .venv\Scripts\activate

REM Check if requirements are already satisfied
echo Checking installed packages...
pip freeze > current_packages.txt
fc current_packages.txt requirements.txt > nul

IF %ERRORLEVEL% NEQ 0 (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo All dependencies are already installed.
)

DEL current_packages.txt

echo.
echo Setup complete. Virtual environment is activated.

:MENU
echo.
echo Please choose an option:
echo 1. Run in headless mode (no browser)
echo 2. Run in non-headless mode (with browser)
echo 3. Quit
set /P choice=Choice:

IF "%choice%"=="1" (
    echo.
    echo Running in headless mode...
    python chatseleniumpi.py --headless
    goto END
) 
IF "%choice%"=="2" (
    echo.
    echo Running in non-headless mode...
    python chatseleniumpi.py
    goto END
) 
IF "%choice%"=="3" (
    echo.
    echo Quitting...
    goto END
)

echo Invalid Choice, please choose only 1, 2, or 3.
goto MENU

:END
pause

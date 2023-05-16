@echo off
echo Installing dependencies...
pip install -r requirements.txt

REM Check the exit code of the previous command
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies.
) ELSE (
    echo Dependencies installed successfully.
)
pause


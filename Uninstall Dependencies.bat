@echo off
echo Uninstalling dependencies...
pip uninstall -r requirements.txt -y

REM Check the exit code of the previous command
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to uninstall dependencies.
) ELSE (
    echo Dependencies uninstalled successfully.
)
pause

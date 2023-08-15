@echo off

REM Run the provided batch script in the background
start "Run Batch Script" /b RUN.bat

REM Wait for the specified timeout
timeout /t 10 /nobreak

REM Find and terminate the "cmd" process running the "run.bat" script
for /f "tokens=2 delims=," %%a in ('tasklist /nh /fi "WindowTitle eq Run Batch Script" /fo csv') do (
    taskkill /f /pid %%a
    set "taskkill_result=!errorlevel!"
)

REM Check the result of taskkill and exit accordingly
if "%taskkill_result%"=="0" (
    echo Batch script execution stopped after 10 seconds.
    exit 0
) else (
    echo Failed to terminate batch script process.
    exit 1
)

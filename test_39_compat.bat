@echo off

start "test39compat" RUN.bat
timeout /T 60
taskkill /FI "WindowTitle eq test39compat*"
set taskkill_exitcode=%errorlevel%

if %taskkill_exitcode% == 0 (
  exit 0
) else (
  exit 1
)
@echo off
call venv\Scripts\activate
cls
pip install -r requirements.txt
cls
py src/main.py
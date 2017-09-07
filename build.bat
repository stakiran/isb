@echo off
setlocal
python %~dp0builder.py -i %~dp0linklist.md -o %~dp0index.html -t %~dp0template.html
pause

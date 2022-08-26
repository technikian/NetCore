@echo off

:: constants
set PYTHON=D:\users\das\Mega\Project\Auto\Farm\Remote\python\versions\python-3.9.13-embed-amd64\python.exe
set APP=./server

:: get the dir of this bat file
set DIR=%~dp0

:: run python app passing script params to python
%PYTHON% %DIR%%APP% %*

:: uncomment for testing
PAUSE

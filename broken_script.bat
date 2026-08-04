@echo off
REM This script contains an obvious error for testing

echo Starting test
if "%1"=="test" goto test

echo Argument was not test
pause

test:
echo Test branch reached
pause

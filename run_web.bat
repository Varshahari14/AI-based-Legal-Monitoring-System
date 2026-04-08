@echo off
echo ========================================
echo AI Legal Monitoring System - Web Dashboard
echo ========================================
echo.
echo Starting web server...
echo Dashboard will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
python web_app.py

pause
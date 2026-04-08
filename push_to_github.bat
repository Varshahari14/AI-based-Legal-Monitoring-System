@echo off
echo Pushing to GitHub repository...
cd /d "c:\Users\SELVARUBIN\OneDrive\Documents\OneDrive\Documents\Vr\AI-Legal-Monitoring"

REM Try to push using Git
echo Running: git push -u origin master
git push -u origin master

if %errorlevel% neq 0 (
    echo Git push failed. Trying alternative method...
    echo.
    echo Please manually run these commands:
    echo cd "c:\Users\SELVARUBIN\OneDrive\Documents\OneDrive\Documents\Vr\AI-Legal-Monitoring"
    echo git push -u origin master
    echo.
    echo If you get authentication errors, you may need to:
    echo 1. Set up SSH keys or personal access token
    echo 2. Configure Git credentials
    echo 3. Use GitHub Desktop or another Git client
) else (
    echo Successfully pushed to GitHub!
)

pause
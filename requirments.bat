@echo off
setlocal enabledelayedexpansion
:: Get current date and time in YYYY-MM-DD_HH-MM-SS format
for /f "tokens=1-4 delims=/ " %%a in ("%date% %time%") do set dt=%%d-%%b-%%c_%%e
set dt=%dt::=-%
set dt=%dt: =0%
set dt=%dt:,=_%
set logfile=logs\pytest_!dt!.log

echo Running pytest with log file: !logfile!
pytest --log-cli-level=INFO --log-file=!logfile! --log-file-level=INFO
pause

echo Installing required Python packages...
pip install pytest
pip install selenium
pip install pytest-html
pip install openpyxl
pip install pytest-xdist
pip install allure-pytest
echo All packages have been installed successfully.
pause
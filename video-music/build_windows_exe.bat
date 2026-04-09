@echo off
setlocal

REM Build a Windows .exe from convert_xls_to_xlsx.py
cd /d "%~dp0"

echo [1/4] Upgrading pip...
py -m pip install --upgrade pip
if errorlevel 1 goto :fail

echo [2/4] Installing build dependencies...
py -m pip install pandas xlrd openpyxl pyinstaller
if errorlevel 1 goto :fail

echo [3/4] Building EXE with PyInstaller...
py -m PyInstaller --onefile --name xls_to_xlsx_converter convert_xls_to_xlsx.py
if errorlevel 1 goto :fail

echo [4/4] Done.
echo EXE location: dist\xls_to_xlsx_converter.exe
goto :end

:fail
echo Build failed. Please review the error messages above.
exit /b 1

:end
pause

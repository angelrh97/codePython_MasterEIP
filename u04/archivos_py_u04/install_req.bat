python -m pip install --trusted-host pypi.org -U pip
python -m pip install --trusted-host pypi.org -U virtualenv
python -m virtualenv "%~dp0\..\venv_master"
call "%~dp0\..\.venv_master\Scripts\activate.bat"
python -m pip install --trusted-host pypi.org -r req_orig.txt
@echo off
echo.
echo.
echo Installation finished
pause
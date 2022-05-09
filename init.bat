@echo off
:s
set /p DEPT1="[Warning]: The database will be completely cleaned up! Continue [y/n]: "
if /i not defined DEPT1 (cls& goto s)
if /i "%DEPT1%"=="y" (echo yes& goto e)
if /i "%DEPT1%"=="n" (echo no& goto q)
:e
venv\scripts\activate.bat & (
    python manage.py flush
    python manage.py makemigrations
    python manage.py migrate
    python manage.py import_data
    :q
    pause
)


%~d1
cd "%~p1"
call venv\Scripts\activate.bat
call cmd /k python mysite\manage.py collectstatic --noinput
PAUSE;

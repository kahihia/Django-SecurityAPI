%~d1
cd "%~p1"
call venv\Scripts\activate.bat
call python mysite\manage.py makemigrations hello_world
call python mysite\manage.py migrate
PAUSE;

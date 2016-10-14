%~d1
cd "%~p1"
call venv\Scripts\activate.bat
call coverage run mysite\manage.py test
call coverage report -m
call coverage html
PAUSE;

%~d1
cd "%~p1"
call venv\Scripts\activate.bat
call python manage.py makemigrations api_v1_0
call python manage.py migrate
PAUSE;

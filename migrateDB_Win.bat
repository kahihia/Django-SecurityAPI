%~d1
cd "%~p1"
call venv\Scripts\activate.bat
call python manage.py makemigrations landing_page api_v1_0
call python manage.py migrate
PAUSE;

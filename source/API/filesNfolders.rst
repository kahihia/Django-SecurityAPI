Files and Folders' Organisation
================

After going to the new `Django-SecurityAPI` folder you'll will have different types of files and folders.

Here is the organisation of the project you're going to find :

+--------------------------------------------+-------------------------------------------------------------------+
|**Files & Folders**                         |                                                   **Description** |
+============================================+===================================================================+
|/application                                |     The folder that contains `settings.py` and `local settings.py`|
+--------------------------------------------+-------------------------------------------------------------------+
|/api                                        |      The main folder : defines the code base of this app.         |
+--------------------------------------------+-------------------------------------------------------------------+
|/functions                                  |      A folder that contains some functions that can be used later |
+--------------------------------------------+-------------------------------------------------------------------+
|/registration                              |A folder that contains some templates for the login page (optionnal)|
+--------------------------------------------+-------------------------------------------------------------------+
|manage.py                                   |   The main file Django uses to run the server, to manage database.|
+--------------------------------------------+-------------------------------------------------------------------+
|requirements.txt                            |                     The packages our App needs to work            |
+--------------------------------------------+-------------------------------------------------------------------+
|runtime.txt                                 |                     The version of Python to use on for Heroku    |
+--------------------------------------------+-------------------------------------------------------------------+
|app.json       |    "[a manifest format for describing web apps](https://devcenter.heroku.com/articles/app-json-schema)"   |
+--------------------------------------------+-------------------------------------------------------------------+
|*.bat                                       |       Some Windows scripts used as alias for some django commands |
+--------------------------------------------+-------------------------------------------------------------------+
|.env.dist                                   |  A template of the file that describe some environnement variables|
+--------------------------------------------+-------------------------------------------------------------------+
|Procfile & Procfile.windows     |    If you user Heroku only : describe actions the dynos have to do (optionnal)|
+--------------------------------------------+-------------------------------------------------------------------+

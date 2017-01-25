Setting up your minimal API
================

Clonning Django-Security API
~~~~~~~~~~~~~~~~~~~~~

Simply clone the repo via SSH :

.. code-block:: shell

    $ git clone git@github.com:DataIsTheNewBlack/Django-SecurityAPI.git

or via HTTPS :

.. code-block:: shell

    $ git clone https://github.com/DataIsTheNewBlack/Django-SecurityAPI.git

After going to the new `Django-SecurityAPI` folder you'll will have different types of files and folders.
As the name of `Django-SecurityAPI` reveals, this project is based on the web-app Python package *Django*.
If you aren't familiar with Django, we suggest you to check some Django Tutorials : https://code.djangoproject.com/wiki/Tutorials

You have to know the basis, that is to say :

  - how variables and parametters are set (`settings.py`)
  - how does the routage system works (`settings.py` and the `urls.py` files)
  - how to set up and access the administration pannel


Here are the files you're going to find :

+--------------------------------------------+-------------------------------------------------------------------+
|**Files & Folders**                         |                                                   **Description** |
+============================================+===================================================================+
|/application                                |       The main folder for the app to work; contains `settings.py` |
+--------------------------------------------+-------------------------------------------------------------------+
|/functions      (*optionnal*)               |      A folder that contains some functions that can be used later |
+--------------------------------------------+-------------------------------------------------------------------+
|/registration                               |      A folder that contains some templates for the login page     |
+--------------------------------------------+-------------------------------------------------------------------+
|manage.py                                   |   The main file Django uses to run the server, to manage database.|
+--------------------------------------------+-------------------------------------------------------------------+
|requirements.txt                            |                     Some different packages our App needs to work |
+--------------------------------------------+-------------------------------------------------------------------+
|*.bat                                       |       Some Windows scripts used as alias for some django commands |
+--------------------------------------------+-------------------------------------------------------------------+
|.env.dist                                   |  A template of the file that describe some environnement variables|
+--------------------------------------------+-------------------------------------------------------------------+
|Procfile & Procfile.windows  (*optionnal*)  |    If you user Heroku only : describe actions the dynos have to do|
+--------------------------------------------+-------------------------------------------------------------------+

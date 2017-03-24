Setting up your minimal API
================

Clonning Django-Security API
~~~~~~~~~~~~~~~~~~~~~

Simply clone the repo via SSH :

.. code:: shell
   $ git clone git@github.com:DataIsTheNewBlack/Django-SecurityAPI.git

or via HTTPS :

.. code:: shell
   $ git clone https://github.com/DataIsTheNewBlack/Django-SecurityAPI.git

Virtual environment
~~~~~~~~~~~~~~~~~~~~~

Go to the folder and create a *virtual environment* :

.. code-block:: shell
   # For Python 3.6 or Python 3.x
   $ virtualenv -p /usr/bin/python3 venv3
   $ source venv3/bin/activate

   # For Python 2.7
   $ virtualenv venv
   $ source venv/bin/activate


**In the following, all the `export` lines can be put at the end of the file `/venv3/bin/activate`. It is easier to define the env variables that way since those lines are executed when lauching the venv.**

You have to set some variables in your virtual env.
First the "secret key" for the app (needed by Django). You can use `site
<http://www.miniwebtool.com/django-secret-key-generator/>`_ to generate one.

.. code-block:: shell
   $ export SECRET_KEY='someLongStringToImagine'


Requirements
~~~~~~~~~~~~~~~~~~~~~
Then install the requirements :

.. code-block:: shell
   $ pip install -r requirements.txt


If you have the error `pg_config not found` just install the `libpq_dev` package.
If you have the error `could not run curl-config` install the `libcurl4-openssl-dev` package.
Then re-install the requirements


You have to create a `local_settings.py` in the same folder as `setting.py` in order to extend this file (see the end of `setting.py`) ; this is useful for managing different
data base between local development and deployement :
.. code-block:: shell
   $ touch local_settings.py

In this file are the settings set to use the local database (`DEBUG` is set to True for dev', false for production.) :

.. code-block:: python
   # Local settings : used for local development.
   from __future__ import absolute_import
   from .settings import PROJECT_ROOT, BASE_DIR
   import os

   DEBUG = True

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }

Then you have to run this in order to set up the models and the database :
.. code-block:: shell
   $ python manage.py makemigrations
   $ python manage.py makemigrations viewer
   $ python manage.py migrate

Finally, `$ python manage.py runserver` runs the server locally.

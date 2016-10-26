# Python Security API,

[![Build Status](https://travis-ci.org/DataIsTheNewBlack/Django-SecurityAPI.svg?branch=master)](https://travis-ci.org/DataIsTheNewBlack/Django-SecurityAPI)
[![Dependency Status](https://gemnasium.com/badges/github.com/DataIsTheNewBlack/Django-SecurityAPI.svg)](https://gemnasium.com/github.com/DataIsTheNewBlack/Django-SecurityAPI)
[![Code Climate](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI/badges/gpa.svg)](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI)
[![Test Coverage](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI/badges/coverage.svg)](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI/coverage)
[![Issue Count](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI/badges/issue_count.svg)](https://codeclimate.com/github/DataIsTheNewBlack/Django-SecurityAPI)
[![Documentation Status](https://readthedocs.org/projects/django-securityapi/badge/?version=doc-user)](http://django-securityapi.readthedocs.io/en/latest/?badge=doc-user)
[![Documentation Status](https://readthedocs.org/projects/django-securityapi/badge/?version=doc-dev)](http://django-securityapi.readthedocs.io/en/latest/?badge=doc-dev)

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

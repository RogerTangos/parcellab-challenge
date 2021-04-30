# ParcelLab Test App

This is a test app for parcellab's challenge. It is written in Django to take advantage of the framework's many integrations and migrations, and uses a SQLite database. Because of Djanso's broad ORM support, the database easily be changed via `settings.py`.

# Setup

## Requirements

### Install Python
This is tested using python 3.8, but should also work in Python verisions 3.6 - 3.9 To see your python version, type the following in bash. 

`python3 --version`

If your version of python3 is below 3.6, [please update](https://www.python.org/).

### Install Pip

If you do not already have the pip package manager installed, installation instructions can be [found here](https://pip.pypa.io/en/stable/installing/).

### Install Project Requirements
Requirements will ideally be installed on a virtual environment, but this can also be done on your system python installation. There's nothing exotic in here.

```
python3 -m pip install -r requirements.txt
```

## Create a Superuser
A user must be created to access the api:

```
python3 manage.py createsuperuser
```

## Create and Migrate the database
This only needs to be run once, but will not cause any issues if run multiple times.

```
python3 manage.py makemigrations challenge
python3 manage.py migrate
```

# Run

Start the server on port 8080
```
python3 manage.py runserver 8080
```

**Website:**

- Navigate to [http://localhost:8080/challenge/](http://localhost:8080/challenge/) for the UI.

## API

- Navigate to [http://localhost:8080/admin](http://localhost:8080/admin) to log in.

- Navigate to [http://localhost:8080/challenge/api](http://localhost:8080/challenge/api) for the API. _(Requires login)_

You can use either the `/admin` panel, the `/challenge/api` or bash to add and get new tracking and checkpoint objects.

```
curl -H 'Accept: application/json; indent=4' -u admin:YOURPASSWORD http://localhost:8080/challenge/api/tracking/
```

## Test
To test the code, run
```
python manage.py test
```


# Author Notes
I worked extensively on a large Django 1.8 project between 2014 and 2016, designing the API, implementing unit, integration, and functional tests, adding new features, and securing the site. Because I've spent most of my time since then doing data science/data engineering, I decided to use this challenge to refresh my web skills using Django.

Much in the Django world has changed, mostly for the better, and Django remains full of abstract and magical methods. Unfortunately, I've forgotten many of them. As a result, the code took a bit longer to write than I would have liked.

Other notes:

* I added a few tests just to prove that I know how to write them. Also, you can see that I can write tests and am a proponent of testing [here.](https://github.com/datahuborg/datahub/tree/master/src/integration_tests).
* The API can use some work, I know. Django-REST is very different from when I last used it, and I didn't have time to re-read the docs. [Here is a serializer that is mainly my work](https://github.com/datahuborg/datahub/blob/master/src/api/serializer.py) for another project.
* My github username is [RogerTangos](https://github.com/RogerTangos)

_You can see an old Django project of mine at [http://datahub.csail.mit.edu/](http://datahub.csail.mit.edu/) and find my commits at [https://github.com/datahuborg/datahub](https://github.com/datahuborg/datahub). Please ignore the security warning. The project is no longer maintained and there's no one to renew the certificates._

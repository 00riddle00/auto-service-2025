![Car Heaven logo](docs/static/car_heaven_logo_for_readme.png)

# Car Heaven – grant your car a two-way ticket to heaven!

## Installation

#### Create virtual environment in the project root directory:

```Shell
$ python3.13 -m venv venv
```

#### Activate the virtual environment:

- ##### For Linux / Mac:

  ```Shell
  $ source venv/bin/activate
  ```

- ##### For Windows:
  ```PowerShell
  $ .\venv\Scripts\activate
  ```

#### Install the required packages:

```Shell
(venv) $ pip install -r requirements.txt
```

## Running

##### [1] Prepare the database:

Since the SQLite database file is stored in this Git repo, if you would like to
use a fresh new database, remove the file [db.sqlite3](db.sqlite3), and then
run:

```Shell
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
```

If you would like to use the existing database, you can optionally create your
own superuser:

```Shell
(venv) $ python manage.py createsuperuser
```

Credentials for the existing superuser in the database:

- Username: `admin`
- E-mail: tomasgiedraitis@gmail.com
- Password: `test`

Finally, run the development server:

```Shell
(venv) $ python manage.py runserver
```

## Software dependencies

[Django](https://www.djangoproject.com/) – the web framework for perfectionists
with deadlines. Django aims to follow Python’s
["batteries included" philosophy](https://docs.python.org/3/tutorial/stdlib.html#tut-batteries-included).
It ships with a variety of extra, optional tools that solve common web
development problems.

For the full list of software dependencies see
[requirements.txt](requirements.txt).

## Latest releases

**v0.1.0** (2025-01-01)

## API references

None

## [License](LICENSE)

The MIT License (MIT)

Copyright (c) 2025 Code Academy
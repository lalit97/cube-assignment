# Cube Assignment

## Local Setup

- Git clone: `https://github.com/lalit97/cube-assignment.git`
- Go to the project directory: `cd cube-assignment`
- Setup virtual environment: `virtualenv -p python3 .` (do not forget to add the dot(.) in the end)
- Activate virtual environment: `source bin/activate`
- Generate environment variables for `SECRET_KEY`, `DB_USER` and `DB_PASSWORD` which are used in settings.py.
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py makemigrations`, `python manage.py migrate`
- Get data of Rules, Events and Users by running `python manage.py loaddata data.json`
- Run server using local settings: `python manage.py runserver`
- See it running on [localhost](http://127.0.0.1:8000/)

## Running tasks

- Inside terminal go to project root and run `redis-server`
- Inside another terminal window go to project root and run `celery -A mysite worker -l info -B`

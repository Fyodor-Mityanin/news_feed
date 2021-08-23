# News_feed

This is a test project to get a job

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Docker v20.10.2 or newer
```

### Installing

Clone repository to your pc and run Docker-Compose

```
docker-compose up
```
You need to create .env file and fill it with your data. Watch .env.example file in root directory, it's example.

Then you need to be sure that container is running

```
docker container ls
```

Take web CONTAINER and run

```
docker-compose exec web bash
```

Now you need to make migrations of news app and migrate

```
python manage.py makemigrations news
python manage.py migrate
```

and create superuser

```
python manage.py createsuperuser
```

and collect static

```
python manage.py collectstatic
```

You can also fill DB from fixtures.json file

```
python manage.py loaddata dump.json

```
That's all, project avalible at http://localhost:8000/

## Project avalible at

[News_Feed](http://localhost:8000/) 


## Built With

* [Django 3.2](https://docs.djangoproject.com/en/3.2/) - The web framework used
* [PostgreSQL 12.4](https://www.postgresql.org/docs/12/plperl-builtins.html) - Object-relational database system used
* [Docker 20.10.2](https://www.docker.com/) - Package software used

## Authors

* **Fedor Mityanin** - [Fyodor-Mityanin](https://github.com/Fyodor-Mityanin)

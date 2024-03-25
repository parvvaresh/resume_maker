# Resume Builder


Place this code at `.env` file:

```python
# General
# ------------------------------------------------------------------------------
USE_DOCKER=yes
IPYTHONDIR=/app/.ipython

# PostgreSQL
# ------------------------------------------------------------------------------
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=resume_builder
POSTGRES_USER=debug
POSTGRES_PASSWORD=debug
```

make sure that change POSTGRES_DB and POSTGRES_PASSWORD base on your config, after that,
simply run 

```python
pip install -r requirements/local.txt
```
python manage.py migrate
and then:
python manage.py runserver

make sure about doing all parts, after that you will find swagger of the project at
http://127.0.0.1/swagger/ and api root at the
http://127.0.0.1/api/.

to run docker run docker-compose up
to build docker image run docker buid -t onlinetaskbar:latest

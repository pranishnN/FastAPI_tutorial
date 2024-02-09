

"""Project Structure"""
- ecommerce (project)
    - sql (app)
        - models.py => Exactly like django models. where we create db table in class and columns as class instance. 
        - schemas.py => Kind a serializer.py in django, here we declare structure of return data when requested, also for creating data in           db.
        - main.py => Kind a django views.py, here we declare both views functionalities and url path assigning.
        - views.py => Kind a django Queryset, we write directly in django, but here we use individual file and by using function.
        - database.py => Used to connect our project to database and create session for database connection.
- alembic (database migration supporter)
    - env.py



"""Migrations"""

Because we are using SQLAlchemy directly and we don't require any kind of plug-in for it to work with FastAPI, we could integrate database migrations with Alembic directly.

And as the code related to SQLAlchemy and the SQLAlchemy models lives in separate independent files, you would even be able to perform the migrations with Alembic without having to install FastAPI, Pydantic, or anything else.

The same way, you would be able to use the same SQLAlchemy models and utilities in other parts of your code that are not related to FastAPI.

For example, in a background task worker with Celery, RQ, or ARQ.


https://alembic.sqlalchemy.org/en/latest/autogenerate.html

/> alembic init alembic

config db in alembic/env.py

/> alembic revision --autogenerate -m "0001 migration"
/> alembic upgrade head

/> uvicorn sql_app.main:app --reload --> py manage.py runserver


"""Alternative DB session with middleware"""


"""VS Debugger"""

--------launch.json configurations------

    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: FastAPI",
                "type": "python",
                "request": "launch",
                "module": "uvicorn",
                "args": [
                    "ecommerce.sql_app.main:app",
                    "--reload"
                ],
                "jinja": true,
                "justMyCode": false
            }
        ]
    }

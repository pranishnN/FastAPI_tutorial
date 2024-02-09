from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:adhoc@192.168.0.2:5432/test_sql_app"
# 198.168.0.1
# SQLALCHEMY_DATABASE_URL = "postgresql://dbmasteruser:e9m*WfF.OVW9P2&I}r*ulYV)CAC33s8n@ls-2a12f581d3159eae2ac2c910f5fa6103005800b4.cutqkshimxrh.ap-south-1.rds.amazonaws.com:5432/test_sql_app"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# the SessionLocal was made to communicate properly with database, everytime we connect with database new session was generated
# because multiple session, not each session work independently and does not arise in session interpting erros.
# it maintains database health
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
    its kind of django models.Model in FastAPI, when you create the class using the declarative syntax provided by 
    SQLAlchemy, it act as ORM between the class intanse to database tables. It also used in migration of different 
    classes in different app folders. This mapping is used to interact with database with python queries without using 
    raw SQL queries.  
"""
Base = declarative_base()
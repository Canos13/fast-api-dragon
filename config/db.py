from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

# Obtén el valor de una variable de entorno
db_host = os.environ.get('MYSQL_HOST')
db_user = os.environ.get('MYSQL_USER')
db_port = os.environ.get('MYSQL_PORT')
db_password = os.environ.get('MYSQL_PASSWORD')
db_database = os.environ.get('MYSQL_DATABASE')

ConnectionString = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"

engine = create_engine(ConnectionString)

meta = MetaData()
conn = engine.connect()
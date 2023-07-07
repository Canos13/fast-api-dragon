

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

news = Table("news", meta, 
    Column("id",Integer, primary_key=True),
    Column("title", String(75)),
    Column("description", Text),
    Column("date", String(75)),
    Column("content", Text),
    Column("author", String(125)),
    Column("image", String(140)),
    Column("source", String(255))
)

meta.create_all(engine)
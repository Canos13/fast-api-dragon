
from fastapi import APIRouter
from config.db import conn
from models.news import news
from schemas.news import News
from fastapi.responses import JSONResponse
from sqlalchemy import select

router = APIRouter()

def get_news():
    
    query = select(
        news.c.id, 
        news.c.title, 
        news.c.description, 
        news.c.date,
        news.c.author
    )

    try:
        result = conn.execute(query).fetchall()
        news_list = []
        for row in result:
            news_dict = row._asdict()
            news_list.append(news_dict)

        return JSONResponse(content=news_list)
    except Exception as e:
        conn.rollback()
        return JSONResponse(content={"error": str(e)})
    

def get_new(id: int):

    try:

        data = conn.execute(news.select().where(news.c.id == id)).first()

        inserted_dict = data._asdict()

        return JSONResponse(content=inserted_dict, status_code=200)
    
    except Exception as e:
        conn.rollback()
        return JSONResponse(content={"error": str(e)})

def create_news(newss: News):
    new_news = {
        "title": newss.title,
        "description": newss.description,
        "date": newss.date,
        "content": newss.content,
        "author": newss.author,
        "image": newss.image,
        "source": newss.source
    } 

    try:

        result = conn.execute(news.insert().values(new_news))
        conn.commit()
        id_inserted = result.lastrowid
        inserted = conn.execute(news.select().where(news.c.id == id_inserted)).first()
        inserted_dict = inserted._asdict()

        return JSONResponse(content=inserted_dict, status_code=201)
    
    except Exception as e:
        conn.rollback()
        return JSONResponse(content={"error": str(e)})
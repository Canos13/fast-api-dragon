from fastapi import APIRouter
from controllers import news
from schemas.news import News

router = APIRouter()

router.get(
    "/news", 
    response_model=list[News]
)(news.get_news)

router.post("/news")(news.create_news)
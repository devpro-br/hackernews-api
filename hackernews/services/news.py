from hackernews.models.news import News
from hackernews.ext.database import db


def list_news():
    """Retorna lista de notícias"""
    news_list = News.query.order_by(News.id.desc()).all()
    return [t.to_dict() for t in news_list]


def create_news(data):
    """Cria uma notícia"""
    news_add = News(**data)
    db.session.add(news_add)
    db.session.commit()
    return news_add.to_dict()

from hackernews.models.news import News


def list_news():
    """Retorna lista de notícias"""
    news_list = News.query.order_by(News.id.desc()).all()
    return [t.to_dict() for t in news_list]

from flask import jsonify
from hackernews.services import news as news_services


def list_news():
    """Faz chamada ao serviço que retorna lista de notícias"""
    news = news_services.list_news()
    return jsonify(news)

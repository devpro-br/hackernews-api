from flask import jsonify
from hackernews.services import news as news_services


def list_news():
    """Faz chamada ao serviço que retorna lista de notícias"""
    return jsonify({"result": news_services.list_news()})

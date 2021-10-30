from flask import jsonify, request
from hackernews.services import news as news_services


def list_news():
    """Faz chamada ao serviço que retorna lista de notícias"""
    return jsonify({"result": news_services.list_news()})


def create_news():
    """Faz chamada ao serviço que cria e retorna uma notícia"""
    data = request.get_json()
    return jsonify(news_services.create_news(data)), 201

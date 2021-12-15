from flask import jsonify

from hackernews.services import news as news_services


def list_news():
    """Faz chamada ao serviço que retorna lista de notícias"""
    return jsonify({"result": news_services.list_news()})


def create_news(body):
    """Faz chamada ao serviço que cria e retorna uma notícia"""
    new_data = news_services.create_news(body["title"], body.get("description"))
    return jsonify(new_data), 201

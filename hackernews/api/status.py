import os

from hackernews.ext.database import db


def get_status():
    """Retorna status do sistema"""
    return {"sha": os.getenv("GIT_HASH"), "database": _get_db_status()}


def _get_db_status():
    """verifica conexao com o banco"""
    try:
        db_ok = db.session.execute("SELECT 40 + 2")
        if list(db_ok)[0] == (42,):
            return "OK"
        return "NOT OK"
    except Exception:  # pylint: disable=W0703
        return "Error connecting to Database"

import pytest

import sqlalchemy as sa
from sqlalchemy.orm import Session

from hackernews.app import create_app
from hackernews.ext.database import db


@pytest.fixture(autouse=False)
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope="function", autouse=False)
def db_session(app):
    conn = db.engine.connect()
    trans = conn.begin()

    session = Session(bind=conn)
    session.begin_nested()

    # then each time that SAVEPOINT ends, reopen it
    @sa.event.listens_for(db.session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    yield db.session

    # rollback everything
    trans.rollback()
    conn.close()
    db.session.remove()

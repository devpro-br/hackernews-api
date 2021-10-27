# hackernews-api

API (backend python) para o frontend do hackernews-clone

## Setup

- criar virtualenv
- `pip install -r requirements-dev.txt`

## Rodar testes

```
make run_tests
```

OU

```

make db_test_up
pytest
make db_test_down

```

## Rodar API

```
docker-compose up -d
flask db upgrade     # 1a vez apenas
flask run
```

👉 http://localhost:5000/api/
👉 http://localhost:5000/api/news

## Próximos passos

- https://github.com/confraria-devpro/hackernews-api/issues

## Adicionando uma notícia

```
flask shell

Python 3.8.10 (default, Sep 28 2021, 16:10:42)

from hackernews.ext.database import db
from hackernews.models.news import News
from hackernews.models.users import User

News.query.all()
[]


u = User(name="roger", username="rac", email="r@a.c")
db.session.add(u)
db.session.commit()

n = News(title="Teste", description="1o. teste", author_id=u.id)
db.session.add(n)
db.session.commit()

News.query.all()
[Teste]
```

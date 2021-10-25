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

In [1]: from hackernews.ext.database import db
In [2]: from hackernews.models.news import News
In [3]: from hackernews.models.users import User

In [4]: News.query.all()
Out[4]: []


In [5]: u = User(name="roger", username="rac", email="r@a.c")
In [6]: db.session.add(u)
In [7]: db.session.commit()

In [8]: n = News(title="Teste", description="1o. teste", author_id=u.id)
In [9]: db.session.add(n)
In [10]: db.session.commit()

In [11]: News.query.all()
Out[11]: [Teste]
```
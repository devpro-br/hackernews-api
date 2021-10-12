def test_execute_a_simple_query(db_session):
    resultset = db_session.execute("SELECT 40 + 2")

    assert list(resultset)[0] == (42,)

#!/usr/bin/env python
# postgresql: postgresql: // scott: tiger @ localhost:5432 / mydatabase
# jdbc:postgresql://localhost:5432/mydatabase?currentSchema=myschema
# pip install psycopg2-binary
from typing import Optional

import pytest

from qpyone.clients.database.db_client import DbClient
from qpyone.clients.database.models import DbConfig
from sqlalchemy import MetaData
from sqlmodel import Field
from sqlmodel import Session
from sqlmodel import SQLModel


class Hero(SQLModel, table=True):
    __table_args__ = {"schema": "test_hub_demo"}
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


@pytest.mark.skip
def test_create_engine():
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    ## create table in default pulic schema
    SQLModel.metadata.create_all(pg.engine)
    # metadata = MetaData(schema="test_hub_demo")
    # metadata.create_all(pg.engine)
    assert pg is not None
    h1 = Hero(name="test2", secret_name="scret_name", age=10)

    # session = Session(pg.engine)
    # session.add(h1)
    # session.commit()
    # session.close()
    pg.save(h1)


@pytest.mark.skip
def test_query():
    sql = """
    SELECT t.*
                 FROM unit.unit t
                 LIMIT 10
    """
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    result = pg.query_by_sqlmodel(sql)
    print(result)
    all_list = []
    for row in result:
        result_dict = {}
        for key in result.keys():
            result_dict[key] = str(row[key])

        all_list.append(result_dict)

    print(all_list)

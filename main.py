import os
from sqlmodel import create_engine, select, Session, SQLModel
from internal.adapters.domain.arithmetic import ArithCore

from internal.adapters.framework.right.db.db import Adapter as DbAdapter
from internal.adapters.app.app import Adapter as AppAdapter
from internal.adapters.framework.left.http.http_api import Adapter as HttpAPIAdapter, FastAPI


def main():
    engine = create_engine(os.getenv("DATABASE_URL"))
    SQLModel.metadata.create_all(engine)

    db_adapter = DbAdapter(db=engine)
    arith_adapter = AppAdapter(ArithCore())
    http_api_adapter = HttpAPIAdapter(FastAPI(), db_adapter, arith_adapter)
    http_api_adapter.run()


if __name__ == "__main__":
    main()

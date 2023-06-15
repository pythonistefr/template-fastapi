import contextlib
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session, sessionmaker

from project_api.core.config import settings


def engine_controller():
    def inner() -> Engine:
        if not inner.engine:
            inner.engine = create_engine(
                settings.secrets.PGSQL_DSN,
                echo=False,
            )
        return inner.engine

    inner.engine = None
    return inner


get_engine = engine_controller()


def create_pg_session() -> Generator[Session, None, None]:
    pg_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=get_engine(),
        expire_on_commit=False,
        future=True,
    )()

    try:
        yield pg_session
    except OperationalError:
        pg_session.rollback()
    finally:
        pg_session.close()


@contextlib.contextmanager
def create_pg_session_context() -> Generator[Session, None, None]:
    """Contextmanager allowing us to create and teardown a PG session.

    Returns:
        SQLA Session object.
    """
    return create_pg_session()

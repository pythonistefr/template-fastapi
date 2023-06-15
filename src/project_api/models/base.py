from sqlalchemy import Column, MetaData, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import INTEGER, TIMESTAMP

metadata = MetaData()
DeclarativeBase = declarative_base(metadata=metadata)


class Base(DeclarativeBase):
    """A Base SQLAlchemy model containing fields shared amongst all other models."""

    __abstract__ = True

    id = Column(
        INTEGER(),
        primary_key=True,
        nullable=False,
        doc="Unique auto incrementing integer used as the primary key for this table.",
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        doc="Date and time at which this database row was created.",
    )

    last_modified_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        doc="Date and time at which this database row was last modified.",
    )

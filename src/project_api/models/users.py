from sqlalchemy import Column
from sqlalchemy.types import BOOLEAN, TEXT

from project_api.models.base import Base


class User(Base):
    full_name = Column(TEXT(), nullable=False, index=True, doc="User full name.")
    email = Column(TEXT(), nullable=False, index=True, unique=True, doc="User email (should be unique).")
    hashed_password = Column(TEXT(), nullable=False, doc="User hashed password.")
    is_active = Column(BOOLEAN(), nullable=False, default=True, doc="User is active ?")

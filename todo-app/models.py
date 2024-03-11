from database import Base
from sqlalchemy import Column, SmallInteger, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'

    id: Column(SmallInteger, primary_key=True, index=True) # type: ignore
    title = Column(String)
    description = Column(String)
    priority = Column(SmallInteger)
    complete = Column(Boolean, default=False)
from ..database import Base
from sqlalchemy import Column,String,Integer,Boolean, text, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    isComplete = Column(Boolean,server_default='False')
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    user_id = Column(Integer,ForeignKey("users.id",ondelete='CASCADE'))
    user = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))
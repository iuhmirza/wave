from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time, Table
from sqlalchemy.orm import relationship

from .database import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("conversation_id", ForeignKey("conversations.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    username = Column(String, unique = True, index = True)
    hashed_password = Column(String)
    public_key = Column(String)

    children = relationship("Child", secondary = association_table)

    

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key = True, index = True)

    children = relationship("Child")
    

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key = True, index = True)
    sender_id = Column(Integer)
    recipient_id = Column(Integer)
    encrypted_content = Column(String)
    timestamp = Column(Time)

    parent_id = Column(Integer, ForeignKey("conversations.id"))


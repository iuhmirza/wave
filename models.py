from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    username = Column(String, unique = True, index = True)
    hashed_password = Column(String)

    public_key = Column(String)
    conversation = Column(Integer)

    conversations = relationship("Messages", back_populates="owner")

    

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key = True, index = True)
    


    messages = relationship("Messsage", back_populates="Owner")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key = True, index = True)
    sender_id = Column(Integer)
    recipient_id = Column(Integer)
    encrypted_content = Column(String)
    timestamp = Column(Time)

    owner_id = Column(Integer, ForeignKey("conversations.id"))
    owner = relationship("Conversation", back_populates="Messages")


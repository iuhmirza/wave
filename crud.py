from sqlalchemy import Session

from . import models, schemas

from argon2 import PasswordHasher

ph = PasswordHasher()

#ph.verify(hash, "string")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    hashed_password = ph.hash(user.password)
    db_user = models.User(**user.dict(), hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

"""
def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()
"""

def get_conversations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Conversation).offset(skip).limit(limit).all()

def create_conversation(db: Session, conversation: schemas.ConversationBase):
    db_conversation = models.Conversation(**conversation.dict())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def create_user_message(db: Session, message: schemas.MessageBase, user_id: int):
    db_message = models.Message(**message.dict(), sender_id = user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
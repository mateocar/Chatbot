from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    user_message = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)

class Correction(Base):
    __tablename__ = "corrections"
    id = Column(Integer, primary_key=True, index=True)
    original_question = Column(Text, nullable=False)
    correc_anwser = Column(Text, nullable=False)
    added_at = Column(DateTime(timezone=True), server_default=func.now())

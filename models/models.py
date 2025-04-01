from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from db.session import Base
from datetime import datetime


class ConversationTurns(Base):
    __tablename__ = "conversation_turns"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(10))
    message = Column(Text, nullable=False)
    consent_to_contact = Column(Boolean, default=False)
    guest_name = Column(String(100), nullable=True)
    company = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    step = Column(String(100), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
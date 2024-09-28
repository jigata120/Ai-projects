from sqlalchemy import create_engine

# example_URL
DATABASE_URL = 'postgresql://postgres:NOTOoOnYfbESCCFfyPZEeSpFbcUhiro@junction.proxy.rlwy.net:57672/railway'

from sqlalchemy import create_engine, Column, String

engine = create_engine(DATABASE_URL)

import uuid
from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatbotSession(Base):
    __tablename__ = 'chatbot_session'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    session_data = Column(JSONB, nullable=False)  
    all_messages =  Column(JSONB, nullable=True)
    def __repr__(self):
        return f"<ChatbotSession(id={self.id})>"


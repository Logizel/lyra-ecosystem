from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    project_id = Column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=True
    )
    filename = Column(String(255), nullable=False)
    s3_path = Column(String(500))
    file_size = Column(Integer)
    mime_type = Column(String(100))
    status = Column(String(50), default="pending")
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True))
    metadata = Column(JSONB)
    total_chunks = Column(Integer, default=0)

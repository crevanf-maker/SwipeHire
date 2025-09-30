from sqlalchemy import Column, DateTime, func, String
import uuid
from app.core.database import Base


class BaseModel(Base):
    """
    Abstract base model with common fields for all models.
    """
    __abstract__ = True
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class SoftDeleteMixin:
    """
    Mixin for soft delete functionality.
    """
    deleted_at = Column(DateTime(timezone=True), nullable=True, index=True)

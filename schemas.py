"""
Database Schemas for Illustration Portfolio

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercased class name.

- Artwork -> "artwork"
- Inquiry -> "inquiry"
"""
from typing import List, Optional
from pydantic import BaseModel, Field


class Artwork(BaseModel):
    title: str = Field(..., description="Artwork title")
    image_url: str = Field(..., description="Public image URL")
    thumbnail_url: Optional[str] = Field(None, description="Smaller preview URL")
    description: Optional[str] = Field(None, description="Short description")
    year: Optional[int] = Field(None, description="Year created")
    tags: List[str] = Field(default_factory=list, description="Tags like 'portrait', 'fantasy'")
    palette: Optional[str] = Field(None, description="Primary palette or hex e.g. #f5f5f5")


class Inquiry(BaseModel):
    name: str = Field(..., min_length=2)
    email: str = Field(...)
    subject: str = Field(..., min_length=2)
    message: str = Field(..., min_length=10)
    budget: Optional[str] = None

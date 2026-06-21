# app/models/response_model.py

from pydantic import BaseModel
from typing import List

class DocumentResponse(BaseModel):
    summary: str
    key_points: List[str]
    raw_text_length: int
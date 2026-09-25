from pydantic import BaseModel
from typing import List, Dict

class DocumentText(BaseModel):
    document_id: str
    text_content: str

class ClassificationResult(BaseModel):
    document_id: str
    predicted_category: str # LEGAL, FINANCIAL, HR, TECHNICAL, MARKETING
    confidence_score: float
    routing_destination: str
    keyword_signals: List[str]

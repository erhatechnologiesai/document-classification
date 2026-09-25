from fastapi import FastAPI
from app.config import settings
from app.models import DocumentText, ClassificationResult
from app.services.classifier import classify_doc

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/classify", response_model=ClassificationResult)
def classify(doc: DocumentText):
    cat, conf, dest, signals = classify_doc(doc.document_id, doc.text_content)
    return ClassificationResult(
        document_id=doc.document_id,
        predicted_category=cat,
        confidence_score=round(conf, 2),
        routing_destination=dest,
        keyword_signals=signals
    )

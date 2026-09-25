CATEGORIES = {
    "LEGAL": ["agreement", "contract", "parties", "hereby", "jurisdiction", "liability", "clause"],
    "FINANCIAL": ["invoice", "balance", "fiscal", "ebitda", "revenue", "audit", "expenditure"],
    "HR": ["candidate", "benefits", "leave", "payroll", "interview", "performance", "onboarding"],
    "TECHNICAL": ["api", "architecture", "microservice", "latency", "docker", "endpoint", "database"]
}

def classify_doc(doc_id: str, text: str):
    t_low = text.lower()
    scores = {}
    signals = []
    
    for cat, kws in CATEGORIES.items():
        matched = [k for k in kws if k in t_low]
        scores[cat] = len(matched)
        if matched:
            signals.extend(matched)

    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        best_cat = "GENERAL"
        conf = 0.50
    else:
        conf = min(0.98, 0.60 + (scores[best_cat] * 0.10))

    destinations = {
        "LEGAL": "LegalOps_DocuSign_Queue",
        "FINANCIAL": "Finance_QuickBooks_Queue",
        "HR": "Workday_HRIS_Ingestion",
        "TECHNICAL": "Engineering_Wiki_Confluence",
        "GENERAL": "Manual_Review_Bucket"
    }

    return best_cat, conf, destinations.get(best_cat, "Manual_Review_Bucket"), signals[:5]

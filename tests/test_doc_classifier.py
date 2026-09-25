import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestDocClassifier(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_legal_classification(self):
        doc = {"document_id": "D-1", "text_content": "This Non-Disclosure Agreement and contract binds all parties under the jurisdiction."}
        res = self.client.post("/classify", json=doc)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["predicted_category"], "LEGAL")
        self.assertIn("LegalOps", data["routing_destination"])

if __name__ == "__main__":
    unittest.main()

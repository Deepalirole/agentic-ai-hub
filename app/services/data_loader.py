from typing import List, Dict


def load_sample_faqs() -> List[Dict]:
    return [
        {
            "id": "faq1",
            "question": "What is your return policy?",
            "answer": "You can return any item within 30 days of delivery for a full refund."
        },
        {
            "id": "faq2",
            "question": "How long does shipping take?",
            "answer": "Standard shipping takes 3–5 business days, express shipping 1–2 days."
        },
        {
            "id": "faq3",
            "question": "Do you offer international shipping?",
            "answer": "Yes, we ship to most countries with additional delivery time and fees."
        },
    ]


def load_sample_products() -> List[Dict]:
    return [
        {
            "id": "P001",
            "name": "Ergonomic Office Chair",
            "category": "Furniture",
            "price": 8999,
            "rating": 4.5,
            "tags": ["office", "back support", "premium"],
        },
        {
            "id": "P002",
            "name": "Wireless Noise-Cancelling Headphones",
            "category": "Electronics",
            "price": 6999,
            "rating": 4.7,
            "tags": ["music", "focus", "remote work"],
        },
        {
            "id": "P003",
            "name": "Standing Desk Converter",
            "category": "Furniture",
            "price": 4999,
            "rating": 4.3,
            "tags": ["health", "productivity", "desk"],
        },
    ]


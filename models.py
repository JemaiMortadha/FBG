from typing import List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Feedback:
    id: int
    userId: str
    productId: str
    rating: int
    comment: str
    date: str = datetime.now().isoformat()
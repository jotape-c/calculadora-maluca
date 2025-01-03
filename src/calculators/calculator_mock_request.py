"""Class for mock request"""
from typing import Dict

class MockRequest:
    """Classe de mokada pra teste"""
    def __init__(self, body: Dict) -> None:
        self.json = body

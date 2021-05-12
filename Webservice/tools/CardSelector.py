from pydantic import BaseModel
from typing import Optional

class CardSelector(BaseModel):
	nbCards : Optional[int] = 1
	deckID : Optional[str] = ""
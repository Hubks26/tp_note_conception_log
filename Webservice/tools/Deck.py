from pydantic import BaseModel
from typing import Optional

class Deck(BaseModel):
	deck_id : Optional[str] = None
from uuid import uuid4
from pydantic import Field
from decimal import Decimal
from pydantic import BaseModel
from pydantic.types import UUID4
from typing import List, Optional

from app.repository.claims import ClaimsRepository


class ClaimsModel(BaseModel):
    uid: Optional[str] = None
    claim_type: str = Field(..., example='CTR')
 


class ClaimsDomain():
    def __init__(self, repository: ClaimsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_claim(self, uid: str):
        return self.__repository.get_claim(uid)

    def create_claim(self, claim: ClaimsModel):
        claim.uid = str(uuid4())
        return self.__repository.create_claim(claim.dict())

    def update_claim(self, claim: ClaimsModel):
        return self.__repository.update_claim(claim.dict())

    def delete_claim(self, uid: str):
        return self.__repository.delete_claim(uid)
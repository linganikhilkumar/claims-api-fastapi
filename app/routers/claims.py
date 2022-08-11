from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.claims import ClaimsDomain, ClaimsModel


class ClaimsRouter:
    def __init__(self, claims_domain: ClaimsDomain) -> None:
        self.__claims_domain = claims_domain

    @property
    def router(self):
        api_router = APIRouter()
        
        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to claims index route'

        @api_router.post('/claims')
        def create_claim(claims_model: ClaimsModel):
            return self.__claims_domain.create_claim(claims_model)

        @api_router.get('/claims/{claim_uid}')
        def get_claim(claim_uid: str):
            try:
                return self.__claims_domain.get_claim(claim_uid)
            except KeyError:
                raise HTTPException(status_code=400, detail='No claim found')

        @api_router.put('/claims')
        def update_claim(claims_model: ClaimsModel):
            return self.__claims_domain.update_claim(claims_model)

        @api_router.delete('/claims/{claim_uid}')
        def delete_claim(claim_uid: str):
            return self.__claims_domain.delete_claim(claim_uid)

        @api_router.get('/claims')
        def get_all():
            return self.__claims_domain.get_all()

        return api_router
import uvicorn
from fastapi import FastAPI

from app.internal.db import initialize_db

from app.domain.claims import ClaimsDomain
from app.repository.claims import ClaimsRepository
from app.routers.claims import ClaimsRouter

app = FastAPI()


db = initialize_db()


claims_repository = ClaimsRepository(db)
claims_domain = ClaimsDomain(claims_repository)
claims_router = ClaimsRouter(claims_domain)

app.include_router(claims_router.router)


@app.get('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)

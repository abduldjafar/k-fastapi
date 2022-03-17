from fastapi import APIRouter
router = APIRouter()

from services.services import Services

router = APIRouter()
svc = Services()

@router.get("/v1/users")
async def root():
    return {"datas":svc.get_users()}
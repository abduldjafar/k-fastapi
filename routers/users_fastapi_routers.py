from fastapi import APIRouter
from schemas.idx import Model as idx_model
from services.services import Services

router = APIRouter()
svc = Services()

@router.get("/v1/users")
async def root():
    return {"datas":svc.get_users()}

@router.post("/v1/idx")
async def create_item(item: idx_model):
   return item
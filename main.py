from fastapi import Depends, FastAPI
from routers import users_fastapi_routers

app = FastAPI()

app.include_router(users_fastapi_routers.router)




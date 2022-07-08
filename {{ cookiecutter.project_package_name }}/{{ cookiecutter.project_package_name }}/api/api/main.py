from typing import List

from cors import configure_cors
from fastapi import APIRouter, FastAPI
from routers import ALL_ROUTERS
from settings import settings


def include_routers(app: FastAPI, routers: List[APIRouter]) -> None:
    for router in routers:
        app.include_router(router)


app = FastAPI()
configure_cors(app)
include_routers(app, ALL_ROUTERS)


@app.get("/")
def root():
    return {"discovery": f"{settings.project_name} API root"}

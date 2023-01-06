from fastapi import FastAPI

from .routers import layaway

app = FastAPI()

app.include_router(layaway.router)

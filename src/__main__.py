"""Entrypoint for the API."""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.controllers import kamas_controller

app = FastAPI(title="API for kamas dashboard")
app.include_router(kamas_controller.router)

register_tortoise(
    app,
    db_url="sqlite://src/db/db.sqlite3",
    modules={"models": ["src.models.kamas_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

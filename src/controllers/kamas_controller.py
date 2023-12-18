import datetime

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from src.models.kamas_model import Kamas, Kamas_Pydantic

router = APIRouter()


@router.post("/kamas", responses={404: {"model": HTTPNotFoundError}})
async def create_kamas_value(message: Kamas_Pydantic):
    await Kamas.create(**message.dict(exclude_unset=True))


@router.get("/today", responses={404: {"model": HTTPNotFoundError}})
async def get_today_kamas():
    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + datetime.timedelta(days=1)

    return await Kamas.filter(timestamp__gte=today_start, timestamp__lt=today_end).all()


@router.get("/yesterday", responses={404: {"model": HTTPNotFoundError}})
async def get_yesterday_kamas():
    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday_start = today_start - datetime.timedelta(days=1)

    return await Kamas.filter(timestamp__gte=yesterday_start, timestamp__lt=today_start).all()


@router.get("/kamas", responses={404: {"model": HTTPNotFoundError}})
async def get_kamas():
    return await Kamas.all()
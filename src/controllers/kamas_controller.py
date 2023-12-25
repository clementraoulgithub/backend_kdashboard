"""Module for the kamas controller."""

import datetime

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from src.models.kamas_model import Kamas, Kamas_Pydantic

router = APIRouter()


@router.post("/kamas", responses={404: {"model": HTTPNotFoundError}})
async def create_kamas_value(message: Kamas_Pydantic):
    """
    Summary: Create a new kamas value.

    Args:
        message (Kamas_Pydantic): Pydantic model for kamas.
    """
    await Kamas.create(**message.dict(exclude_unset=True))


@router.get("/today", responses={404: {"model": HTTPNotFoundError}})
async def get_today_kamas(server: str):
    """
    Summary: Get today's kamas value.

    Args:
        server (str): Server name.

    Returns:
        Kamas_Pydantic: Kamas_Pydantic
    """
    today_start = datetime.datetime.now(datetime.timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    today_end = today_start + datetime.timedelta(days=1)
    return (
        await Kamas.filter(
            timestamp__gte=today_start, timestamp__lt=today_end, server=server
        )
        .order_by("-timestamp")
        .first()
    )


@router.get("/yesterday", responses={404: {"model": HTTPNotFoundError}})
async def get_yesterday_kamas(server: str):
    """
    Summary: Get yesterday's kamas value.

    Args:
        server (str): Server name.

    Returns:
        Kamas_Pydantic: Kamas_Pydantic
    """
    today_start = datetime.datetime.now(datetime.timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    yesterday_start = today_start - datetime.timedelta(days=1)
    return (
        await Kamas.filter(
            timestamp__gte=yesterday_start, timestamp__lt=today_start, server=server
        )
        .order_by("-timestamp")
        .first()
    )


@router.get("/kamas", responses={404: {"model": HTTPNotFoundError}})
async def get_kamas(server: str, scope: str):
    """
    Summary: Get kamas value.

    Args:
        server (str): Server name.
        scope (str): Scope of the request.

    Returns:
        Kamas_Pydantic: Kamas_Pydantic
    """
    today_start = datetime.datetime.now(datetime.timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    if scope == "day":
        today_end = today_start + datetime.timedelta(days=1)
        return await Kamas.filter(
            timestamp__gte=today_start, timestamp__lt=today_end, server=server
        ).order_by("timestamp")

    if scope == "week":
        week_start = today_start - datetime.timedelta(days=today_start.weekday())
        week_end = week_start + datetime.timedelta(days=7)
        return await Kamas.filter(
            timestamp__gte=week_start, timestamp__lt=week_end, server=server
        ).order_by("timestamp")

    if scope == "month":
        month_start = today_start.replace(day=1)
        month_end = month_start + datetime.timedelta(days=31)
        return await Kamas.filter(
            timestamp__gte=month_start, timestamp__lt=month_end, server=server
        ).order_by("timestamp")

    if scope == "3month":
        month_start = today_start.replace(day=1) - datetime.timedelta(days=62)
        month_end = month_start + datetime.timedelta(days=31)
        return await Kamas.filter(
            timestamp__gte=month_start, timestamp__lt=month_end, server=server
        ).order_by("timestamp")

    if scope == "6month":
        month_start = today_start.replace(day=1) - datetime.timedelta(days=155)
        month_end = month_start + datetime.timedelta(days=31)
        return await Kamas.filter(
            timestamp__gte=month_start, timestamp__lt=month_end, server=server
        ).order_by("timestamp")

    year_start = today_start.replace(month=1, day=1)
    year_end = year_start + datetime.timedelta(days=365)
    return await Kamas.filter(
        timestamp__gte=year_start, timestamp__lt=year_end, server=server
    ).order_by("timestamp")

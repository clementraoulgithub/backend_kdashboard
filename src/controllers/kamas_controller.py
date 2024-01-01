# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


"""Module for the kamas controller."""

import datetime

import numpy as np
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

    lst_yesterday = await Kamas.filter(
        timestamp__gte=yesterday_start, timestamp__lt=today_start, server=server
    ).order_by("-timestamp")

    if len(lst_yesterday) == 0:
        return None

    average = np.mean([Kamas.average for Kamas in lst_yesterday])
    lst_yesterday[0].average = round(average, 3)
    lst_yesterday[0].min = min(Kamas.min for Kamas in lst_yesterday)

    return lst_yesterday[0]


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

    if scope == "three_months":
        month_start = today_start.replace(day=1) - datetime.timedelta(days=62)
        month_end = month_start + datetime.timedelta(days=93)
        return await Kamas.filter(
            timestamp__gte=month_start, timestamp__lt=month_end, server=server
        ).order_by("timestamp")

    if scope == "six_months":
        month_start = today_start.replace(day=1) - datetime.timedelta(days=93)
        month_end = month_start + datetime.timedelta(days=186)
        return await Kamas.filter(
            timestamp__gte=month_start, timestamp__lt=month_end, server=server
        ).order_by("timestamp")

    year_start = today_start.replace(month=1, day=1)
    year_end = year_start + datetime.timedelta(days=365)
    return await Kamas.filter(
        timestamp__gte=year_start, timestamp__lt=year_end, server=server
    ).order_by("timestamp")

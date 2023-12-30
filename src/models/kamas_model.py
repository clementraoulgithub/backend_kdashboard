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


"""Module for the kamas model."""

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Kamas(models.Model):
    """
    Summary: Kamas model.

    Args:
        models (models.Model): Base model from tortoise ORM.
    """

    id = fields.IntField(pk=True)
    timestamp = fields.DatetimeField(auto_now_add=True)
    kamas_dict = fields.JSONField()
    average = fields.FloatField()
    max = fields.FloatField()
    min = fields.FloatField()
    server = fields.CharField(max_length=200)


Kamas_Pydantic = pydantic_model_creator(
    Kamas, name="KamasIn", exclude=["id", "timestamp"]
)

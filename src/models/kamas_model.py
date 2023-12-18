from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Kamas(models.Model):
    id = fields.IntField(pk=True)
    timestamp = fields.DatetimeField(auto_now_add=True)
    kamas_dict = fields.JSONField()
    average = fields.FloatField()
    max = fields.FloatField()
    min = fields.FloatField()


Kamas_Pydantic = pydantic_model_creator(Kamas, name="KamasIn", exclude=["id", "timestamp"])

# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

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

#!/usr/bin/python3
"""
City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent city.

    Attributes:
        state_id (str): The state id.
        name (str): City name.
    """

    state_id = ""
    name = ""

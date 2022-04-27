#
# This is a Payer class using pydantic. Used to store incoming input.
#
# Author: Felix Estrella
# Date: April 27, 2022
#

from pydantic import BaseModel
from datetime import datetime

class Payer(BaseModel):
    payer: str
    points: int
    timestamp: datetime
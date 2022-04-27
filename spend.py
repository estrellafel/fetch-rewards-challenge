#
# This is a Spend class using pydantic. Used to store incoming input.
#
# Author: Felix Estrella
# Date: April 27, 2022
#

from pydantic import BaseModel

class Spend(BaseModel):
    points: int
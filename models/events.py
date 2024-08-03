from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra ={
            "example" : {
                "title":"Title",
                "image":"Link to image",
                "description":"Description",
                "tags":["tag1", "tag2"],
                "location":"Location",
            }
        }


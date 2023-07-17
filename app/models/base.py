from pydantic import BaseModel
from typing import List


class Login(BaseModel):
    name: str
    password: str


class Tables(BaseModel):
    data: List[dict]


class TablesIn(BaseModel):
    file_path: str


class WebSocket(BaseModel):
    createTime: int
    data: dict
    id: str
    returnMessage: str
    status: str
    type: int
    username: str


class Load(BaseModel):
    gridKey: str


cell_data = [{"r": 0, "c": 0, "v": {"v": 1, "m": "1", "ct": {"fa": "General", "t": "n"}}}]

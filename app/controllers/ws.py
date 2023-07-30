from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = list()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        pass

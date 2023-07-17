import os
import json
import time
import pandas as pd
from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import UploadFile, File
from starlette.responses import FileResponse
from app.models.base import Tables, cell_data
from app.controllers.excel_control import ExcelControl
from app.controllers.services.import_excel import DataControl


def table_router() -> APIRouter:
    router = APIRouter()
    control = ExcelControl()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    in_file_dir = os.path.join(base_dir, 'in_file')
    out_file_dir = os.path.join(base_dir, 'out_file')
    if not os.path.exists(in_file_dir):
        os.mkdir(in_file_dir)
    if not os.path.exists(out_file_dir):
        os.mkdir(out_file_dir)

    @router.post('/input', tags=['tables'])
    async def table_input(file: UploadFile = File(...)):
        file_path = os.path.join(in_file_dir, file.filename)
        contents = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contents)
        headers, frame = control.data_analysis(file_path)
        cell_data.clear()
        for item, header_data in enumerate(headers):
            lucky_data = {'r': 0, 'c': item, 'v': header_data}
            cell_data.append(lucky_data)
        for item, frame_data in enumerate(frame):
            r = item + 1
            for c, data in enumerate(frame_data):
                lucky_data = {'r': r, 'c': c, 'v': data}
                cell_data.append(lucky_data)
        return {
            'code': 0,
            'msg': 'success'
        }

    @router.post('/output', tags=['tables'])
    async def table_output(item: Tables):
        sheet_names, data_frame = control.frontend_data_to_excel(item.data)
        file_path = os.path.join(out_file_dir, 'demo.xlsx')
        file = pd.ExcelWriter(file_path)
        data = pd.DataFrame(data_frame)
        for sheet_name in sheet_names:
            data.to_excel(file, sheet_name=sheet_name)
        file.close()
        return {
            'file': file_path
        }

    @router.get('/download', tags=['tables'])
    async def file_download(file_path: str):
        return FileResponse(
            file_path,
            filename='demo.xlsx'
        )

    @router.post('/load', tags=['tables'])
    async def table_load():
        print(cell_data)
        load = [
            {
                "name": "sheet",
                "index": "01",
                "order": 0,
                "status": 1,
                "celldata": cell_data
            },
        ]
        return json.dumps(load)

    @router.websocket('/ws')
    async def update(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive()
            if data['text'] == 'rub':
                continue
            else:
                data = json.loads(data['text'])
                print(data)
                t = data['t']
                con = DataControl(t, data)
                up_data = con.control()
                if up_data is not None:
                    cell_data.append(up_data)
            await websocket.send_json({
                'createTime': time.time(),
                'returnMessage': "继续保持",
                'status': "1",
                'type': 0
            })

    return router

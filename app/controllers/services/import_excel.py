import time
import pandas as pd


def analysis_excel(file_path):
    frame = pd.read_excel(file_path)
    data_frame = frame.values
    table_headers = frame.columns.values
    return table_headers, data_frame


class DataControl:
    def __init__(self, t: str, msg):
        self.t = t
        self.msg = msg

    def __update(self):
        msg = self.msg.get('v')
        res = {'r': self.msg.get('r'), 'c': self.msg.get('c'), 'v': self.msg.get('v')}
        return res

    def __default(self):
        msg = self.msg.get('v')
        res = {'createTime': time.time(),
               'celldata': msg,
               'returnMessage': 'succes', 'status': '0', 'type': 0}
        return res

    def control(self):
        if self.t == 'v':
            return self.__update()


class DataConvert:
    def __init__(self, file_path: str = None, data_frame: list = None):
        self.file_path = file_path
        self.data_frame = data_frame

    def frame_to_pandas(self):
        frame = list()
        sheet_names = list()
        frame_data = dict()
        for sheet_data in self.data_frame:
            sheet_names.append(sheet_data.get('name'))
            sheet_frame = sheet_data.get('data')
            for _data in sheet_frame:
                row_list = list()
                for _data_child in _data:
                    if _data_child is not None:
                        row_list.append(_data_child.get('v'))
                if len(row_list) >= 1:
                    frame.append(row_list)
        table_header = frame[0]
        frame.pop(0)
        for item, key in enumerate(table_header):
            values = [x[item] for x in frame]
            frame_data[key] = values
        return sheet_names, frame_data

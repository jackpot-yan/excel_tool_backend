import pandas as pd
from .services.import_excel import analysis_excel, DataConvert


class ExcelControl:
    def __init__(self):
        pass

    @classmethod
    def data_analysis(cls, file_path):
        table_headers, data_frame = analysis_excel(file_path)
        return table_headers, data_frame

    @classmethod
    def frontend_data_to_excel(cls, data: list):
        convert = DataConvert(data_frame=data)
        sheet_names, frame_data = convert.frame_to_pandas()
        return sheet_names, frame_data

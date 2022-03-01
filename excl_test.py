#-*- coding:utf-8 -*-

import os
from openpyxl import Workbook,load_workbook

def excel_creat():
    if not(os.path.exists("./original_data")):
        os.mkdir("original_data")
    if not(os.path.exists("./weather_data.xlsx")):
        wb = Workbook()
        ws =wb.active
        # cell = ws["A"]
        # cell[0].data_type='d'
        ws.append(["时间","温度","空气质量","相对湿度","风力"])
        wb.save("weather_data.xlsx")
        
def excel_process(shijian,tem,kongqi,shidu,fengli):
    wb = load_workbook("weather_data.xlsx")
    ws = wb.active
    ws.append([shijian,tem,kongqi,shidu,fengli])
    wb.save("weather_data.xlsx")
    pass

# wb = Workbook()
# ws =wb.active
# cell = ws["A"]
# cell[0].data_type='d'
# print(cell[0].data_type)

from ti_config.bootstrap import init_ti_srv_cfg
from ti_daf.sql_context import SqlContext, session_scope, iselect_rows_by_sql
import json
import pandas as pd
from datetime import datetime
import datetime as dt
import os
import numpy as np
import decimal


M2_df=pd.DataFrame({'a':[1,2,3,4,5],'b':[8,9,0,2,3]})


class excel_format():

    def __init__(self,excel_writer):
        self.excel_writer=excel_writer
        self.work_book=excel_writer.book
        self.title_format=self.work_book.add_format({'align':'center','font_name':'微软雅黑'})
        self.text_format=self.work_book.add_format({'align':'center','font_name':'微软雅黑'})
        self.num_format=self.work_book.add_format({'align':'center','num_format':'0.0%','font_name':'微软雅黑'})


    def data_to_sheet(self,dataframe,sheet_name,start_row=0,start_col=0):
        dataframe.to_excel(self.excel_writer, sheet_name,index=False,startrow=start_row,startcol=start_col)
        self.sheet = self.excel_writer.sheets[sheet_name]
        return self.sheet


    def get_format(self):
        format_1=self.work_book.add_format()
        format_2=self.work_book.add_format()
        pass


    def sheet_format(self,sheet,area,size=18,format_type='text'):
        if format_type=='title':
            format_defaut=self.title_format
        elif format_type=='text':
            format_defaut=self.text_format
        elif format_type=='number':
            format_defaut=self.num_format

        sheet.set_column(area,size,format_defaut)

        return sheet


excel_writer=pd.ExcelWriter('/Users/andpay/Desktop/excelformat.xlsx',engine='xlsxwriter')
format=excel_format(excel_writer)
sheet=format.data_to_sheet(M2_df,'new')
format_sheet=format.sheet_format(sheet,'A:F')

print(sheet)


# work_book=excel_writer.book
# format_1=work_book.add_format({'align':'center','font_name':'微软雅黑'})
# format_2=work_book.add_format({'align':'center','num_format':'0.00%','font_name':'微软雅黑'})
# format_3=work_book.add_format({'align':'center','font_name':'微软雅黑','bold': True, 'font_color': 'bule'})
#
# M2_df.to_excel(excel_writer,'新增M2客户明细',index=False,startrow=1)
# M2_df.to_excel(excel_writer,'新增M2客户明细',index=False,startrow=10)
# M2_sheet=excel_writer.sheets['新增M2客户明细']
#
# M2_sheet.merge_range(0,0,0,1,'here is a title,we must be give many word',format_3)
# #M2_sheet.write('A1:B1','here is a title,we must be give many word',format_3)
# M2_sheet.set_column('A:Z',18,format_1,)
# format_3.set_font_name('new sheet')
#
# excel_writer.save()



# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:35:07 2018

@author: H.T
"""

#
# 万得数据接口数据处理
# get_wind_data.py
#
import pandas as pd

from WindPy import *
from datetime import datetime as dt

def get_wind_optiondata(startdate, enddate):
    ''' 利用Wind数据接口获取期权交易市场数据。
    
    Parameters
    ==========
    startdate : str
        行情数据开始日期
    enddate : str
        行情数据结束日期
    
    Results
    =======
    option_data_set : DataFrame
        包含收盘价及到期日等信息的期权数据集
    '''
    w.start()
    getstr1 = "startdate=" + startdate + ";enddate=" + enddate + ";exchange=sse;windcode=510050.SH;field=date,option_code,option_name,close"
    getstr2 = "exchange=sse;windcode=510050.SH;status=all;field=wind_code,sec_name,exercise_price,listed_date,expire_date"
    oetf1 = w.wsd("512510.SH", "close", startdate, startdate, "")
    oetf2 = w.wsd("512510.SH", "close", enddate, enddate, "")
    odo1 = w.wset("optiondailyquotationstastics", getstr1)
    odo2 = w.wset("optioncontractbasicinfo", getstr2)
    option_data = pd.DataFrame()
    contract_data = pd.DataFrame()
    for i in range(len(odo1.Fields)):
        option_data[odo1.Fields[i]] = odo1.Data[i]
    option_data.index = odo1.Data[0]
    
    for i in range(len(odo2.Fields)):
        contract_data[odo2.Fields[i]] = odo2.Data[i]
    
    temp1 = option_data[option_data.index == dt.strptime(startdate, '%Y-%m-%d')]
    temp1['underlying'] = oetf1.Data[0]
    temp2 = option_data[option_data.index == dt.strptime(enddate, '%Y-%m-%d')]
    temp2['underlying'] = oetf2.Data[0]
    ops = temp1.append(temp2, ignore_index=True)
    contract_data.rename(columns={contract_data.columns[0] : 'option_code'}, 
                                  inplace=True)
    option_data_set = ops.merge(contract_data, on='option_code')
    return option_data_set
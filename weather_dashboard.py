# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 16:47:29 2025

@author: sasha
"""
import certifi
import requests
import streamlit as st
import pandas as pd

st.title("台灣氣象資料 Dashboard")

API_KEY = st.secrets["CWA_API_KEY"]   # 改成讀 secrets 的方式

# 使用者選城市（要用中文才能查 CWA API）
LOCATION = st.selectbox("選擇城市", ["臺北市", "臺中市", "高雄市"])

# API URL（F-C0032-001 是今明 36 小時天氣預報）
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

params = {
    "Authorization": API_KEY,
    "format": "JSON",
    "locationName": LOCATION
}

# 取得資料
res = requests.get(url, params=params,verify=False)
data = res.json()

# 解析資料
location = data["records"]["location"][0]

st.subheader(f"{location['locationName']} 36 小時預報")

# 顯示每一項 weatherElement
for element in location["weatherElement"]:
    name = element["elementName"]
    
    # 取第一個時段的預報資料
    value = element["time"][0]["parameter"]["parameterName"]

    st.write(f"{name}：{value}")




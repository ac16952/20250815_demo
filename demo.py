import numpy as np
import pandas as pd
import streamlit as st

st.title("Demo Page")

st.write("This is a demo page")
st.write("## This is a demo page")

arr1 = np.array([1, 2, 3, 4, 5])
st.write(arr1)

df1 = pd.DataFrame([[11,22,33,44],[50,60,70,80]])
st.write(df1)

st.table(df1)

st.sidebar.write("## 核取方塊")
r1 = st.sidebar.checkbox("外帶")
if r1:
    st.sidebar.info("外帶")
else:
    st.sidebar.info("內用")

checks = st.sidebar.columns(2)
txt = ''
with checks[0]:
    r11 = st.sidebar.checkbox("Ａ")
    if r11:
        txt+=" A "

with checks[1]:
    r12 = st.sidebar.checkbox("B")
    if r12:
        txt+=" B "

st.info(txt)

st.sidebar.write("## 單選按鈕")
b1 = st.sidebar.radio("請選擇飲料",["咖啡","果汁","奶茶"])
st.sidebar.info(b1)

st.sidebar.write("## 單選按鈕")
b2 = st.sidebar.radio("請選擇飲料",["咖啡","果汁","奶茶"],key='b2')
st.sidebar.info(b2)

st.sidebar.write("## 滑桿")
num = st.slider("請選擇數量",1.0,5.0,0.5)
st.sidebar.info(num)

st.sidebar.write("## 下拉選單")
city = st.selectbox("請選擇城市",["台北","台中","高雄"])
if city == "台北":
    st.sidebar.info("A")
elif city == "台中":
    st.sidebar.info("B")
else:
    st.sidebar.info("others")



a = st.number_input("請輸入數字....")
b = st.number_input("請輸入數字....",key="b")
if st.button("相加"):
    st.write("### ",a+b)
    
    
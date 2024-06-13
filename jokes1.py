import streamlit as st
st.text("A man visits the doctor. The doctor says I have bad news for you.You have cancer and Alzheimer's disease.  The man replies Well,thank God I don't have cancer!")
level=st.slider("Select your level",1,5)
st.write("you select:",level)
st.text("Q. What's 200 feet long and has 4 teeth?   A. The front row at a Willie Nelson Concert.")
level=st.slider("Select your level ",1,5)
st.write("you select:",level)
st.text("How many feminists does it take to screw in a light bulb? That's not funny.")
level=st.slider("Select your level  ",1,5)
st.write("you select:",level)

import streamlit as st
import os
#from fastai import *
import pathlib
import sys
import pickle

# 根据不同的操作系统设置正确的pathlib.Path
if sys.platform == "win32":
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
else:
    temp = pathlib.WindowsPath
    pathlib.WindowsPath = pathlib.PosixPath
path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(path,"joke5.pkl")
with open(model_path,'rb') as file:
    data=pickle.load(file)
if st.button("submit ratings"):
    st.write(data)
level1=st.slider("Select your level to the first joke",1,5)
st.write("you select:",level1)
level2=st.slider("Select your level to the second joke",1,5)
st.write("you select:",level2)
level3=st.slider("Select your level to the third joke",1,5)
st.write("you select:",level3)
level4=st.slider("Select your level to the fourth joke",1,5)
st.write("you select:",level4)
level5=st.slider("Select your level to the fifth joke",1,5)
st.write("you select:",level5)
if st.button("submit recommended ratings"):
    satisfaction=(level1+level2+level3+level4+level5)/5*20
    st.write(f"{satisfaction}%")







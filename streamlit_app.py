
import streamlit as st
import pandas as pd
from deta import Deta
import os
# from dotenv import load_dotenv
# load_dotenv(".env")
# key = os.getenv("key")
key = "d04zgljxeva_WbFhwMJowwp3B7vNgdQViDoDqxfMRFVc"

deta = Deta(key)

def push_data(db,name,heigth):
    return db.put({"key":name,"उंची":heigth})


st.title("|| श्री राम समर्थ || ")
st.header("वृक्ष सर्वेक्षण")

st.sidebar.header("प्लॉट निवडा")
plot = st.sidebar.selectbox("निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरशिंग" ])

if plot == "सरिता पॉलिमर्स":
    st.title("सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        push_data(db=db1,name=name,heigth=height)
        st.write(pd.DataFrame(db1.fetch().items).tail(5))
elif plot == "नारायण":
    st.title("नारायण")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि"])
    st.write(name)
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    st.write(height)
elif plot == "लक्ष्मी ऍग्रो":
    st.title("लक्ष्मी ऍग्रो")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि"])
    st.write(name)
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    st.write(height)
elif plot == "राकेश ब्रिक्स":
    st.title("राकेश ब्रिक्स")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि"])
    st.write(name)
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    st.write(height)
elif plot == "सुमरशिंग":
    st.title("सुमरशिंग")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि"])
    st.write(name)
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    st.write(height)
else:
    st.write("select plot from left side menu")





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
    # st.write(db.fetch().count)
    return db.put({"key":str(db.fetch().count+1),"झाडाचे_नाव":name,"उंची":str(heigth)})

st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">""", unsafe_allow_html=True)

# Center-aligned title with tree icons

st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री राम समर्थ ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'> <i class='fa fa-tree'></i> वृक्ष सर्वेक्षण  <i class='fa fa-tree'></i> </h1>", unsafe_allow_html=True)


# st.markdown("<h2 style='text-align: center; font-size: 24px;'>वृक्ष सर्वेक्षण</h2>", unsafe_allow_html=True)

# st.sidebar.markdown("<h2 style='text-align: center;'>प्लॉट निवडा</h2>", unsafe_allow_html=True)


# st.title("|| श्री ||")
# st.title( "|| श्री राम समर्थ || ")
# st.header("वृक्ष सर्वेक्षण")
# st.sidebar.header("प्लॉट निवडा")
plot = st.selectbox("प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरशिंग" ])

if plot == "सरिता पॉलिमर्स":
    st.title("सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        push_data(db=db1, name=name,heigth=height)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db1.fetch().items).tail(5))



elif plot == "नारायण":
    st.title("नारायण")
    db2 = deta.Base("narayan")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        push_data(db=db2, name=name,heigth=height)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db2.fetch().items).tail(5))

elif plot == "लक्ष्मी ऍग्रो":
    st.title("लक्ष्मी ऍग्रो")
    db3 = deta.Base("laxmi")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        push_data(db=db3, name=name,heigth=height)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        st.write(pd.DataFrame(db3.fetch().items).tail(5))

    
elif plot == "राकेश ब्रिक्स":
    st.title("राकेश ब्रिक्स")
    db4 = deta.Base("rakesh")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        push_data(db=db4, name=name,heigth=height)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db4.fetch().items).tail(5))

    
elif plot == "सुमरशिंग":
    st.title("सुमरशिंग")
    db5 = deta.Base("sumershing")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        push_data(db=db5, name=name,heigth=height)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db5.fetch().items).tail(5))

    

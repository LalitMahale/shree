
import streamlit as st
import pandas as pd
from deta import Deta
import os
# from dotenv import load_dotenv
# load_dotenv(".env")
# key = os.getenv("key")
key = "d04zgljxeva_WbFhwMJowwp3B7vNgdQViDoDqxfMRFVc"

deta = Deta(key)

def push_data(db,name,heigth,sr):
    # st.write(db.fetch().count)
    return db.put({"key":sr,"झाडाचे_नाव":name,"उंची":str(heigth)})

# def update(db,key,name,heigth):
#     # st.write(db.fetch().count)
#     return db1.update(updates={"झाडाचे_नाव":name,"उंची":str(height)},key=str(key))

def update(db):
    st.write("Please fill out the form below:")
    key = st.number_input("Key",step=1,min_value=1)
    height = st.number_input(" झाडांची उंची ",step=1,min_value=1)
    name = st.selectbox(" झाडाचे नाव निवडा ",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])

    # message = st.text_area("Message")
    submit_button = st.button("बदल जतन करा")
    if submit_button:
        db.update(updates={"झाडाचे_नाव":name,"उंची":str(height)},key=str(key))
        st.success("बदल यशस्वीरित्या जतन केले!")

def photo(name):
    data = {"कडू लिंब":"neem.jpg","पिंपळ":"pimpal.jpeg","वड":"vad.jpeg","आंब्या":"mango.jpeg","निलगि":"nilgari.jpg",
            "कविट":"kavit.jpg"}
    st.image(data[name])
    st.write(name)

st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">""", unsafe_allow_html=True)

# Center-aligned title with tree icons

st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री राम समर्थ ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'> <i class='fa fa-tree'></i> वृक्ष सर्वेक्षण  <i class='fa fa-tree'></i> </h1>", unsafe_allow_html=True)


plot = st.selectbox("प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरशिंग" ])


if plot == "सरिता पॉलिमर्स":
    st.title("सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    if name == "" or name == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)

    container = st.container()

    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि"])
        if selected_option != "":
            photo(selected_option)

        # if show_form:
        #     open_form()

        # if contact_us:
        #     open_contact()


  
    # button_save = st.button("जतन करा")
    
    # button_update = st.button("बदल करा")

    if show_form :
        sr = str(db1.fetch().count+1)
        push_data(db=db1, name=name,heigth=height)
        st.write("key :",sr)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db1.fetch().items).tail(5))

    # if button_update :
    #     update(db = db1)
        # key = st.number_input("Key",step=1,min_value=1)
        # u = st.button("बदल करा ")

        # if u == True:
        #     update(db1,key,name,height)
        #     st.success("बदल केला")
        #     st.write(pd.DataFrame(db1.get(str(key)),index=[0]))

  



elif plot == "नारायण":
    st.title("नारायण")
    db2 = deta.Base("narayan")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    if name == "":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        sr = str(db2.fetch().count+1)
        push_data(db=db2, name=name,heigth=height,sr=sr)

        st.write("key :",sr)


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
    if name == "" or name == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        sr = str(db3.fetch().count+1)
        push_data(db=db3, name=name,heigth=height,sr=sr)
        st.write("key :",sr)

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
    if name == "" or name == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        # sr = db1.fetch().count + 1
        sr = str(db4.fetch().count+1)
        push_data(db=db4, name=name,heigth=height)
        st.write("key :",sr)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db4.fetch().items).set_index("key").tail(5))

    
elif plot == "सुमरशिंग":
    st.title("सुमरशिंग")
    db5 = deta.Base("sumershing")
    name = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंब्या","पिंपळ","निलगि","उपलब्ध नाही"])
    if name == "उपलब्ध नाही":
        name = st.text_input("झाडाचे नाव टाका")
    if name == "" or name == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)
    button = st.button("जतन करा")
    if button:
        sr = str(db5.fetch().count+1)
        push_data(db=db5, name=name,heigth=height)
        st.write("key :",sr)
        st.write(f"झाडाचे नाव :{name }")
        st.write(f"झाडांची उंची : {height }")
        st.success("यशस्वीरित्या जतन केले ")
        # st.write(db1.fetch().items)
        st.write(pd.DataFrame(db5.fetch().items).tail(5))



bar = st.sidebar.selectbox("संपूर्ण डेटा पाहण्यासाठी प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरशिंग" ])

if bar == "सरिता पॉलिमर्स":
    st.sidebar.write("निवडले :- सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    b = st.sidebar.button("पहा")
    if b:
        st.sidebar.write(pd.DataFrame(db1.fetch().items))

elif bar == "नारायण":
    st.sidebar.write("निवडले :- नारायण")
    db1 = deta.Base("narayan")
    b = st.sidebar.button("पहा")
    if b:
        st.sidebar.write(pd.DataFrame(db1.fetch().items))

    
elif bar == "लक्ष्मी ऍग्रो":
    st.sidebar.write("निवडले :- लक्ष्मी ऍग्रो")
    db1 = deta.Base("laxmi")
    b = st.sidebar.button("पहा")
    if b:
        st.sidebar.write(pd.DataFrame(db1.fetch().items))

elif bar == "राकेश ब्रिक्स":
    st.sidebar.write("निवडले :- राकेश ब्रिक्स")
    db1 = deta.Base("rakesh")
    b = st.sidebar.button("पहा")
    if b:
        st.sidebar.write(pd.DataFrame(db1.fetch().items))

elif bar == "सुमरशिंग":
    st.sidebar.write("निवडले :- सुमरशिंग")
    db1 = deta.Base("sumershing")
    b = st.sidebar.button("पहा")
    if b:
        st.sidebar.write(pd.DataFrame(db1.fetch().items))




st.markdown("<div style='height: 15vh'></div>", unsafe_allow_html=True)

# Create a container to hold the "Contact Us" button
contact_container = st.container()
with contact_container:
        # Right-align the button at the bottom
        st.markdown("<div style='position: fixed; bottom: 10px; right: 100px; text-align: right;'>"
                    "<a href='tel:+918087830153' target='_blank'>"
                    "<button style='padding: 8px 15px;'>संपर्क साधा</button>"
                    "</a></div>", unsafe_allow_html=True)

    # Create a Spacer to push the content up and create space for the footer
# st.markdown("<div style='height: 20vh'></div>", unsafe_allow_html=True)

# # Create a container to hold the buttons
# buttons_container = st.container()
# with buttons_container:
#     # Right-align the buttons at the bottom
#     st.markdown("<div style='position: fixed; bottom: 10px; right: 10px; text-align: right;'>"
#                 "<a href='https://example.com/contact' target='_blank'>"
#                 "<button style='padding: 10px 20px; margin-right: 10px;'>Contact Us</button>"
#                 "</a>"
#                 "<a href='https://example.com/another-link' target='_blank'>"
#                 "<button style='padding: 10px 20px;'>Contact Us 2</button>"
#                 "</a>"
#                 "</div>", unsafe_allow_html=True)

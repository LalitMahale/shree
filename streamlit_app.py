from googletrans import Translator
import streamlit as st
import pandas as pd
from deta import Deta
import os
# from dotenv import load_dotenv
# load_dotenv(".env")
# key = os.getenv("key")
key = "d04zgljxeva_WbFhwMJowwp3B7vNgdQViDoDqxfMRFVc"

deta = Deta(key)
translator = Translator()

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
    name = st.selectbox(" झाडाचे नाव निवडा ",["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम","उपलब्ध नाही"])

    # message = st.text_area("Message")
    submit_button = st.button("बदल जतन करा")
    if submit_button:
        db.update(updates={"झाडाचे_नाव":name,"उंची":str(height)},key=str(key))
        st.success("बदल यशस्वीरित्या जतन केले!")

def photo(name):
    data = {"कडू लिंब":"neem.jpg","पिंपळ":"pimpal.jpeg","वड":"vad.jpeg","आंबा":"mango.jpeg","निलगि":"nilgari.jpg","सिसम":"nilgari.jpg",
            "कविट":"kavit.jpg"}
    st.image(data[name])
    st.write(name)


def translate_to_marathi(english_text):
    if english_text:
        translation = translator.translate(english_text, src='en', dest='mr')
        return translation.text
    return ""

background_image = "neem.jpg"
background_color = "rgba(255, 255, 255, 0.9)"  # Background color with opacity

# Apply the background image and color
page_bg_img = f"""
<style>
body {{
    background: url({background_image});
    background-size: cover;
    background-color: {background_color};
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">""", unsafe_allow_html=True)

# Center-aligned title with tree icons

st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'>|| श्री राम समर्थ ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'>||  जय जय रघुवीर समर्थ ||</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'> <i class='fa fa-tree'></i> वृक्ष सर्वेक्षण  <i class='fa fa-tree'></i> </h1>", unsafe_allow_html=True)


plot = st.selectbox("प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरसिंग" ])


if plot == "सरिता पॉलिमर्स":
    st.title("सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    name1 = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम","उपलब्ध नाही"])
    if name1 == "उपलब्ध नाही":
        english_text = st.text_input("झाडाचे नाव टाका")
        name1 = translate_to_marathi(english_text)
        st.success(f"Translated to Marathi: {name1}")
    if name1 == "" or name1 == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)

    container = st.container()
    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम"])
        if selected_option != "":
            photo(selected_option)


    if show_form :
        sr = str(db1.fetch().count+1)
        if name1 != "" or name1 != " ":
            push_data(db=db1, name=name1,heigth=height,sr=sr)
            st.write("key :",sr)
            st.write(f"झाडाचे नाव :{name1 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            st.write(pd.DataFrame(db1.fetch().items).tail(5))
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")


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
    name2 = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","वड","उंबर","आभूटा","जांभुळ","आंबा","पिंपळ","निलगि","सिसम","बांबू",
                                             "बदाम","करंज","चच","जास्वंद","बेल","अंजन","पाचपत्री","लिंबू","कविट","उपलब्ध नाही"])
    if name2 == "उपलब्ध नाही":
        english_text = st.text_input("झाडाचे नाव टाका")
        name2 = translate_to_marathi(english_text)
        st.success(f"Translated to Marathi: {name2}")
    if name2 == "":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)

    container = st.container()
    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form2 = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम"])
        if selected_option != "":
            photo(selected_option)

    if show_form2 :
        sr = str(db2.fetch().count+1)
        if name2 != "" or name2 != " ":
            push_data(db=db2, name=name2,heigth=height,sr=sr)
            st.write("key :",sr)
            st.write(f"झाडाचे नाव :{name2}")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            st.write(pd.DataFrame(db2.fetch().items).tail(5))
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")




elif plot == "लक्ष्मी ऍग्रो":
    st.title("लक्ष्मी ऍग्रो")
    db3 = deta.Base("laxmi")
    name3 = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम","उपलब्ध नाही"])
    if name3 == "उपलब्ध नाही":
        english_text = st.text_input("झाडाचे नाव टाका")
        name3 = translate_to_marathi(english_text)
        st.success(f"Translated to Marathi: {name3}")
    if name3 == "" or name3 == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)


    container = st.container()
    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form3 = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम"])
        if selected_option != "":
            photo(selected_option)

    if show_form3 :
        sr = str(db3.fetch().count+1)
        if name3 != "" or name3 != " ":
            push_data(db=db3, name=name3,heigth=height,sr=sr)
            st.write("key :",sr)
            st.write(f"झाडाचे नाव :{name3 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            st.write(pd.DataFrame(db3.fetch().items).tail(5))
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")

    
elif plot == "राकेश ब्रिक्स":
    st.title("राकेश ब्रिक्स")
    db4 = deta.Base("rakesh")
    name4 = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम","उपलब्ध नाही"])
    if name4 == "उपलब्ध नाही":
        english_text = st.text_input("झाडाचे नाव टाका")
        name4= translate_to_marathi(english_text)
        st.success(f"Translated to Marathi: {name4}")
    if name4 == "" or name4 == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)


    container = st.container()
    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form4 = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम"])
        if selected_option != "":
            photo(selected_option)

    if show_form4:
        sr = str(db4.fetch().count+1)
        if name4 != "" or name4 != " ":
            push_data(db=db4, name=name4,heigth=height,sr=sr)
            st.write("key :",sr)
            st.write(f"झाडाचे नाव :{name4 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            st.write(pd.DataFrame(db4.fetch().items).tail(5))
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")
   

    
elif plot == "सुमरसिंग":
    st.title("सुमरसिंग")
    db5 = deta.Base("sumershing")
    name5 = st.selectbox("झाडाचे नाव निवडा",["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम","उपलब्ध नाही"])
    if name5 == "उपलब्ध नाही":
        english_text = st.text_input("झाडाचे नाव टाका")
        name5 = translate_to_marathi(english_text)
        st.success(f"Translated to Marathi: {name5}")
    if name5 == "" or name5 == " ":
        st.error("कृपया वैध नाव प्रविष्ट करा")
    height = st.number_input("झाडांची उंची",step=1,min_value=1)

    
    container = st.container()
    with container:
        # Create buttons to open the form and to contact us
        col1, col2, col3 = st.columns(3)

        show_form5 = col1.button("जतन करा")
        # button_update = col2.button("बदल करा")
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडू लिंब","कविट","वड","आंबा","पिंपळ","निलगि","सिसम"])
        if selected_option != "":
            photo(selected_option)

    if show_form5:
        sr = str(db5.fetch().count+1)
        if name5 != "" or name5 != " ":
            push_data(db=db5, name=name5,heigth=height,sr=sr)
            st.write("key :",sr)
            st.write(f"झाडाचे नाव :{name5 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            st.write(pd.DataFrame(db5.fetch().items).tail(5))
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")




bar = st.sidebar.selectbox("संपूर्ण डेटा पाहण्यासाठी प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरसिंग" ])

if bar == "सरिता पॉलिमर्स":
    st.sidebar.write("निवडले :- सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        st.sidebar.write(df)
        # st.dataframe(df)
        st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="सरिता पॉलिमर्स.csv",
                   mime="text/csv")
        

elif bar == "नारायण":
    st.sidebar.write("निवडले :- नारायण")
    db1 = deta.Base("narayan")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        st.sidebar.write(df)
        # st.dataframe(df)
        st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="नारायण.csv",
                   mime="text/csv")

    
elif bar == "लक्ष्मी ऍग्रो":
    st.sidebar.write("निवडले :- लक्ष्मी ऍग्रो")
    db1 = deta.Base("laxmi")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        st.sidebar.write(df)
        # st.dataframe(df)
        st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="लक्ष्मी ऍग्रो.csv",
                   mime="text/csv")

elif bar == "राकेश ब्रिक्स":
    st.sidebar.write("निवडले :- राकेश ब्रिक्स")
    db1 = deta.Base("rakesh")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        st.sidebar.write(df)
        # st.dataframe(df)
        st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="राकेश ब्रिक्स.csv",
                   mime="text/csv")

elif bar == "सुमरसिंग":
    st.sidebar.write("निवडले :- सुमरसिंग")
    db1 = deta.Base("sumershing")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        st.sidebar.write(df)
        # st.dataframe(df)
        st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="सुमरसिंग.csv",
                   mime="text/csv")




st.markdown("<div style='height: 15vh'></div>", unsafe_allow_html=True)

# Create a container to hold the "Contact Us" button
contact_container = st.container()
with contact_container:
        # Right-align the button at the bottom
        st.markdown("<div style='position: fixed; bottom: 10px; right: 100px; text-align: right;'>"
                    "<a href='tel:+918087830153' target='_blank'>"
                    "<button style='padding: 10px 20px;'>संपर्क साधा</button>"
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

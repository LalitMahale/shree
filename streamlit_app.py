from googletrans import Translator
import streamlit as st
import pandas as pd
from deta import Deta
from streamlit_lottie import st_lottie
import os
import requests
# from dotenv import load_dotenv
# load_dotenv(".env")
# key = os.getenv("key")
key = "d04zgljxeva_WbFhwMJowwp3B7vNgdQViDoDqxfMRFVc"

deta = Deta(key)
translator = Translator()

def push_data(db,name,heigth,sr):
    # st.write(db.fetch().count)
    return db.put({"key":sr,"झाडाचे_नाव":name,"उंची":str(heigth)})

def load_lottieur(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


url = "https://lottie.host/da64ca28-5eb8-4aee-a98a-530a2ef8c070/Jva96FtCyk.json"



def photo(name):
    data = {"कडूलिंब":"./images/neem.jpg","पिंपळ":"./images/pimpal.jpeg","वड":"./images/vad.jpeg",
            "आंबा":"./images/mango.jpeg","नीलगीरी":"./images/nilgari.jpg","शिसम":"./images/nilgari.jpg",
            "कविट":"./images/kahit.jpg","बाभूळ":"./images/babhul.jpg","मोह":"./images/moha.jpg"," चिंच":"./images/chinch.jpg","सप्तपरणी":"./images/7_leaf.jpg","सेतुक":"./images/setuk.jpg",
             "बदाम":"./images/badam.jpg","बेल":"./images/bel.jpg","कहीट":"./images/kahit.jpg","इंग्रजी चिंच":"./images/english chinch.jpg","भोकर":"./images/bhokar.jpg","पेरू":"./images/peru.jpg","चिंचोळ":"./images/chinchola.jpg","उंबर":"./images/umber.jpg","आपटे":"./images/apate.jpg","सीताफल":"./images/sitaphal.jpg",
            "जांभुळ":"./images/jambul.jpg","आभोटा":"./images/aabhuta.jpg","आवळा":"./images/avala.jpg"}
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


plot = st.selectbox("प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरसिंग" ], format_func=str)


if plot == "सरिता पॉलिमर्स":
    st.title("सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    name1 = st.selectbox("झाडाचे नाव निवडा",["","कडूलिंब","कविट","वड","आंबा","पिंपळ","मोह","करंज","बेल","चिंच","पळस","उंबर",
                                             "देवकापूस","जांभूळ","आभूटा","शिसम","इंग्रजी चिंच","महू","आभुळशेंग","शिसम / वड","उपलब्ध नाही"])
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
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक"
                                             ,"बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभोटा","आवळा"])
        if selected_option != "":
            photo(selected_option)


    if show_form :
        sr = str(db1.fetch().count+1)
        if name1 != "" or name1 != " ":
            push_data(db=db1, name=name1,heigth=height,sr=sr)
            st.write("झाडाचा क्रमांक  :",sr)
            st.write(f"झाडाचे नाव :{name1 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            df1 = db1.fetch().items
            df1.key = df1.key.astype("int")
            df1.sort_values("key",inplace=True)
            st.write(pd.DataFrame(df1.tail(5)))
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
    name2 = st.selectbox("झाडाचे नाव निवडा",["","कडूलिंब","वड","उंबर","आभूटा","जांभुळ","पिंपळ","शिसम","बांबू",
                                             "बदाम","करंज","चिंच","जास्वंद","बेल","अंजन","पाचपत्री","लिंबू","उपलब्ध नाही"])
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
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक",
                                             "बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभोटा","आवळा"])
        if selected_option != "":
            photo(selected_option)

    if show_form2 :
        sr = str(db2.fetch().count+1)
        if name2 != "" or name2 != " ":
            push_data(db=db2, name=name2,heigth=height,sr=sr)
            st.write("झाडाचा क्रमांक  :",sr)
            st.write(f"झाडाचे नाव :{name2}")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            df2 = db2.fetch().items
            df2.key = df2.key.astype("int")
            df2.sort_values("key",inplace=True)
            st.write(pd.DataFrame(df2.tail(5)))        
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")




elif plot == "लक्ष्मी ऍग्रो":
    st.title("लक्ष्मी ऍग्रो")
    db3 = deta.Base("laxmi")
    name3 = st.selectbox("झाडाचे नाव निवडा",["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक",
                                             "बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभुळशेंग","आभोटा","आवळा","उपलब्ध नाही"])
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
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक",
                                             "बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभोटा","आवळा"])
        if selected_option != "":
            photo(selected_option)

    if show_form3 :
        sr = str(db3.fetch().count+1)
        if name3 != "" or name3 != " ":
            push_data(db=db3, name=name3,heigth=height,sr=sr)
            st.write("झाडाचा क्रमांक  :",sr)
            st.write(f"झाडाचे नाव :{name3 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            df3 = db3.fetch().items
            df3.key = df3.key.astype("int")
            df3.sort_values("key",inplace=True)
            st.write(pd.DataFrame(df3.tail(5)))        
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")

    
elif plot == "राकेश ब्रिक्स":
    st.title("राकेश ब्रिक्स")
    db4 = deta.Base("rakesh")
    name4 = st.selectbox("झाडाचे नाव निवडा",["","कडूलिंब","कविट","वड","उंबर","बोर","करंज","बेहडा","मोह","आभुळशेंग","चिंच","चिंचोळ","सप्तपरणी","जांभुळ",
                                             "आभुळशेंग","सुबाभूळ","चिकू","देवकापूस","आपटे","आवळा","आभूटा","पिंपळ","नीलगीरी","शिसम","शिसम / सुबाभूळ","उपलब्ध नाही"])
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
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक",
                                             "बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभोटा","आवळा"])
        if selected_option != "":
            photo(selected_option)

    if show_form4:
        sr = str(db4.fetch().count+1)
        if name4 != "" or name4 != " ":
            push_data(db=db4, name=name4,heigth=height,sr=sr)
            st.write("झाडाचा क्रमांक  :",sr)
            st.write(f"झाडाचे नाव :{name4 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            df4 = db4.fetch().items
            df4.key = df4.key.astype("int")
            df4.sort_values("key",inplace=True)
            st.write(pd.DataFrame(df4.tail(5)))  
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")
   

elif plot == "सुमरसिंग":
    st.title("सुमरसिंग")
    db5 = deta.Base("sumershing")
    name5 = st.selectbox("झाडाचे नाव निवडा",["","कडूलिंब","आभूटा","मोह","वड","आंबा","करंज","सप्तपरणी","सीताफल","शिसम","उपलब्ध नाही"])
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
        selected_option = col3.selectbox("झाडाचे फोटो पहा", ["","कडूलिंब","बाभूळ","वड","आंबा","पिंपळ","नीलगीरी","मोह"," चिंच","सप्तपरणी","सेतुक",
                                             "बदाम","बेल","कहीट","इंग्रजी चिंच","भोकर","पेरू","चिंचोळ","उंबर","शिसम","आपटे","सीताफल",
                                             "जांभुळ","आभोटा","आवळा"])
        if selected_option != "":
            photo(selected_option)

    if show_form5:
        sr = str(db5.fetch().count+1)
        if name5 != "" or name5 != " ":
            push_data(db=db5, name=name5,heigth=height,sr=sr)
            st.write("झाडाचा क्रमांक :",sr)
            st.write(f"झाडाचे नाव :{name5 }")
            st.write(f"झाडांची उंची : {height }")
            st.success("यशस्वीरित्या जतन केले ")
            # st.write(db1.fetch().items)
            df5 = db5.fetch().items
            df5.key = df5.key.astype("int")
            df5.sort_values("key",inplace=True)
            st.write(pd.DataFrame(df5.tail(5)))  
        else:
            st.warning("कृपया योग्य माहिती प्रविष्ट करा")




bar = st.sidebar.selectbox("संपूर्ण डेटा पाहण्यासाठी प्लॉट निवडा",["","सरिता पॉलिमर्स","नारायण", "लक्ष्मी ऍग्रो","राकेश ब्रिक्स","सुमरसिंग","संपूर्ण डेटा"])

if bar == "सरिता पॉलिमर्स":
    st.sidebar.write("निवडले :- सरिता पॉलिमर्स")
    db1 = deta.Base("sarita")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        if "key" in df.columns:
            st.sidebar.write(df)
            # st.dataframe(df)
            st.sidebar.download_button("Download csv",
                    df.to_csv(),
                    file_name="सरिता पॉलिमर्स.csv",
                    mime="text/csv")
        else:
            st.sidebar.warning("No data is present")  
        

elif bar == "नारायण":
    st.sidebar.write("निवडले :- नारायण")
    db1 = deta.Base("narayan")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        if "key" in df.columns:
            df.key = df.key.astype("int")
            df.sort_values("key",inplace=True)
            st.sidebar.write(df)
            st.sidebar.download_button("Download csv",
                    df.to_csv(),
                    file_name="नारायण.csv",
                    mime="text/csv")
        else:
            st.sidebar.warning("No data is present")  

    
elif bar == "लक्ष्मी ऍग्रो":
    st.sidebar.write("निवडले :- लक्ष्मी ऍग्रो")
    db1 = deta.Base("laxmi")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        if "key" in df.columns:
            df.key = df.key.astype("int")
            df.sort_values("key",inplace=True)
            st.sidebar.write(df)
            st.sidebar.download_button("Download csv",
                    df.to_csv(),
                    file_name="लक्ष्मी ऍग्रो.csv",
                    mime="text/csv")
        else:
            st.sidebar.warning("No data is present")            

elif bar == "राकेश ब्रिक्स":
    st.sidebar.write("निवडले :- राकेश ब्रिक्स")
    db1 = deta.Base("rakesh")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        if "key" in df.columns:
            df.key = df.key.astype("int")
            df.sort_values("key",inplace=True)
            st.sidebar.write(df)
            st.sidebar.download_button("Download csv",
                    df.to_csv(),
                    file_name="राकेश ब्रिक्स.csv",
                    mime="text/csv")
        else:
            st.sidebar.warning("No data is present")

elif bar == "सुमरसिंग":
    st.sidebar.write("निवडले :- सुमरसिंग")
    db1 = deta.Base("sumershing")
    b = st.sidebar.button("पहा")
    if b:
        df = pd.DataFrame(db1.fetch().items)
        if "key" in df.columns:
            df.key = df.key.astype("int")
            df.sort_values("key",inplace=True)
            st.sidebar.write(df)
            st.sidebar.download_button("Download csv",
                   df.to_csv(),
                   file_name="सुमरसिंग.csv",
                   mime="text/csv")
        else:
            st.sidebar.warning("No data is present")


elif bar == "संपूर्ण डेटा":
    plot = ["sarita","laxmi","rakesh","sumershing"]
    st.sidebar.write("निवडले :- संपूर्ण डेटा")
    b = st.sidebar.button("पहा")
    
    if b:
        try:
            df1 = deta.Base("narayan")
            df =  pd.DataFrame(df1.fetch().items)
            for i in plot:
                data = deta.Base(i)
                df1 = pd.DataFrame(data.fetch().items)
                df = pd.concat([df,df1],ignore_index=True)
            if "key" in df.columns:
                df.key = df.key.astype("int")
                df.sort_values("key",inplace=True)
                st.sidebar.write(df)
            # csv = df.to_csv("संपूर्ण डेटा.csv")
                st.sidebar.download_button("Download csv",
                        df.to_csv(),
                        file_name="संपूर्ण डेटा.csv",
                        mime="text/csv")
            else:
                st.sidebar.warning("No data is present")
        except:
            st.sidebar.warning("No data is present")





st.markdown("<div style='height: 15vh'></div>", unsafe_allow_html=True)

# Create a container to hold the "Contact Us" button
contact_container = st.container()
with contact_container:
        # Right-align the button at the bottom
        st.markdown("<div style='position: fixed; bottom: 10px; right: 100px; text-align: right;'>"
                    "<a href='tel:+918087830153' target='_blank'>"
                    "<button style='padding: 10px 20px;'>संपर्क साधा</button>"
                    "</a></div>", unsafe_allow_html=True)


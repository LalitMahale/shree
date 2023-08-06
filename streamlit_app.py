

import streamlit as st
import pandas as pd

st.title("Excel update app")

df = pd.read_csv("data.csv")
# df.drop("Unnamed: 0",inplace=True,axis=0)

st.sidebar.header("Option")

option_form = st.sidebar.form("Options_form")
user_name = option_form.text_input("user_name")
size_name = option_form.text_input("size_input")
add_form = option_form.form_submit_button()


if add_form:
    st.write(user_name,size_name)
    df2 = pd.DataFrame({"name":[user_name], "size":[size_name]},index=[df.index[-1]+1])
    df = pd.concat([df,df2])
    df.to_csv("data.csv",index=False)
    st.write(df.tail(5))

# import streamlit as st

# def main():
#     st.title("Name Selection App")

#     # Predefined list of names
#     predefined_names = ["lalit", "rahul"]

#     # Dropdown to select a name from the predefined list
#     selected_name = st.selectbox("Select a name:", [""] + predefined_names)

#     # If the selected name is not in the predefined list, allow manual input
#     if selected_name == "":
#         manual_name = st.text_input("Enter a name:")
#         if manual_name:
#             st.success(f"Manually entered name: {manual_name}")
#     else:
#         st.success(f"Selected name: {selected_name}")

# if __name__ == "__main__":
#     main()

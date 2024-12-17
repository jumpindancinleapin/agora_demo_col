import streamlit as st
import os


#Messaging
st.title("View Files")
st.write("The files below correspond to the topic preference you set. You can explore all of the files here using the controls below. **Agora** already has!")

st.divider()

#Inputs
directories = os.listdir("resources/data")

topic_path = st.segmented_control(
    "Choose directory:",
    directories,
    default=st.session_state["topic_choice"]
)

directory_path = f"resources/data/{topic_path}"

file_path = None

if topic_path != None:
    files = os.listdir(directory_path)

    file_path = st.segmented_control(
        "Choose file:",
        files,
        default=files[0]
    )

st.divider()

#File section

if topic_path == None:
    st.write("No directory selected, please make a selection above.")
else:
    if file_path == None:
        st.write("No file selected, please make a selection above.")

    else:
        full_path = f"{directory_path}/{file_path}"
        with open(full_path, "r") as file:
            text = file.read()
            st.write(text)



st.divider()


#Nav
foot_lt, foot_rt = st.columns(2)
with foot_lt:
    if st.button("<- Manage API Keys", use_container_width=True):
        st.switch_page("tools/manage_api_keys.py")

with foot_rt:
    if st.button("Agora ->", use_container_width=True, type="primary"):
                st.switch_page("tools/agora_v2.py")
        





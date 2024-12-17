import streamlit as st

#Messaging
st.title("Upload Files")
st.write("I have handled the file uploading, but this is the place a user would upload and organize their own files.")

st.divider()

#File Uploader
uploaded_file = st.file_uploader("Upload your file(s)", type=["csv", "txt", "xlsx"], accept_multiple_files=True, disabled=True)

# - Actual code removed, lightening payload for Columbia, page is illustrative



#Nav
st.divider()

foot_lt, foot_md, foot_rt = st.columns(3)
with foot_lt:
    if st.button("<- Preferences", use_container_width=True):
        st.switch_page("tools/preferences.py")

with foot_rt:
    if st.button("Manage API Keys ->", use_container_width=True, type="primary"):
        st.switch_page("tools/manage_api_keys.py")


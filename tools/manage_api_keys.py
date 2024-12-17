import streamlit as st


#Messaging
st.title("Manage API Keys")
st.write("I have also included API keys for you, but this is where users would input their keys.")
st.divider()

#Inputs
st.text_input("OpenAI API Key", disabled=True, type="password", value="Nice try!")
st.text_input("Anthropic API Key", disabled=True, type="password", value="When's the library reopen?")
# - actual code is removed, lightening payload for Columbia, page is just illustrative


#Nav
st.divider()
foot_lt, foot_md, foot_rt = st.columns(3)
with foot_lt:
    if st.button("<- Upload Files", use_container_width=True):
        st.switch_page("tools/upload_files.py")
with foot_rt:
    if st.button("View Files ->", use_container_width=True, type="primary"):
        st.switch_page("tools/file_viewer.py")


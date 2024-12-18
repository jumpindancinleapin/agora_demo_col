import streamlit as st

#Messaging
st.title("About")

st.write(
    """
    The user interface and hosting is handled by Streamlit.
    OpenAI's API is used extensively to handle file interpretation and user querying. 
    The chat is set up using modern best practice of threads, assistants, and runs,

    The ***novel*** portion of this application is the general functionality...
    ETC ETC

    For simplicity's sake, I have removed account/credential functionality for this demo.

    To scale the app up, accounts and credentials would be issued, and a database would be
    created to store user interactions so they can be returned to. 
    """
)




#Nav
foot_l, foot_m, foot_r = st.columns(3)

with foot_m:
    if st.button(":material/replay: Start Demo Over", use_container_width=True):
        st.switch_page("home/welcome.py")
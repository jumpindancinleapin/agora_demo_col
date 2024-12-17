import streamlit as st

#Messaging
st.header("Before you meet Agora...")
st.write(
    """
    This app is not collecting personal infomation.
    However, user prompts are sent to third party APIs which may process and log the user prompts.
    Please **avoid inputting any sensitive, personal, or confidential information** while 
    using this app.
    """
)

#Input
st.session_state["disclaimer_acknowledged"] = st.toggle(
    "Click to acknowledge.",
    value=st.session_state["disclaimer_acknowledged"],
)

if st.session_state["disclaimer_acknowledged"]:
    st.write("User acknowledged ✔")


st.divider()


#Nav
foot_lt, foot_rt = st.columns(2)
with foot_lt:
    if st.button("<- Welcome", use_container_width=True):
        st.switch_page("home/welcome.py")

with foot_rt:
    if st.session_state["disclaimer_acknowledged"] == False:
        st.button("Agora ->", use_container_width=True, type="primary", disabled=True)
    else:
        if st.button("Agora ->", use_container_width=True, type="primary"):
            st.switch_page("tools/agora_v2.py")



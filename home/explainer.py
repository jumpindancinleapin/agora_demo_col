import streamlit as st

st.session_state["last_page_visited"] = "home/explainer.py"

#Messaging
st.title("What is this?")

st.write(
    """
    ***This*** is a custom webapp that allows a law student to leverage the best artificial intelligence
    without it encroaching on their critical thinking.  
    """
)
st.write(
    """
    **Agora**, an AI Assistant, refuses to write complete drafts or state opinions.
    Instead, Agora answers simple legal questions, sifts through files, and leads the user in the 
    right direction.
    """
)
st.write(
    """
    Underlying technology includes **HTML**, **Python**, **Streamlit**, and **OpenAI**.
    """
)
st.write(
    """
    For navigation, use the buttons to follow the demonstration flow I've set, 
    or navigate freely using the side menu, accessible by the arrow on the top left.
    """
)
st.write(
    """
    Next, you'll choose some preferences, and go on a tour of the platform. 
    """
)


st.divider()


#Nav
foot_lt, foot_rt = st.columns(2)
with foot_lt:
    if st.button("<- Welcome", use_container_width=True):
        st.switch_page("home/welcome.py")

with foot_rt:
    if st.button("Preferences ->", use_container_width=True, type="primary"):
        st.switch_page("tools/preferences.py")


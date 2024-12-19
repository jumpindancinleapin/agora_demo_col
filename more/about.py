import streamlit as st

last_page_visited = st.session_state["last_page_visited"]


#Messaging
st.title("About")


st.write(
    """
    **Scripting**

    Scripting is done with Python, the popular and versatile programming language.
    Python is well-suited for AI use cases.

    **Artificial Intelligence**

    OpenAI's Assistants API is used extensively for the AI in this app. 
    Best practices are used to fetch assistants, threads, messages, runs, et cetera. 

    **User Interface**

    The elements of the user interface are Streamlit components, from Streamlit's API. 
    Although the functionality belongs to the app, the appearance is Streamlit code. 
    Streamlit allows for rapid development of novel things, such as Agora and Queequeg, by
    handling many of the boilerplate UI and hosting code.

    **Future**

    This tech-stack allows for rapid scalability. The app is built to be modular, and interoperable
    with databases, payment systems, account systems, et cetera. **While this is a very simple demonstration, 
    the potential for this app is as far as our imaginations take us.** 
    """
)


st.divider()

#Nav
foot_l, foot_m, foot_r = st.columns(3)

with foot_m:
    if st.button("<- Previous Page", use_container_width=True):
        st.switch_page(last_page_visited)


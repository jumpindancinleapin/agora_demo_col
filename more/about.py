import streamlit as st

last_page_visited = st.session_state["last_page_visited"]


#Messaging
st.title("About")


st.write(
    """
    **The Team**

    Agora is named for the word **agora**, which can refer to a place for
    civil debate. 

    ***Q***ueeque***g***'s name reflects their purpose: ***Q***uery ***g***eneration. 


    **GitHub**
    """
)
st.link_button("See the code ->", "https://github.com/jumpindancinleapin/agora_demo_col")
st.write(
    
    """


    **Scripting**

    Scripting is done with Python, the popular and versatile programming language.
    Python is well-suited for AI use cases.

    **Artificial Intelligence**

    OpenAI's Assistants API is used extensively for the AI in this app. 
    Best practices are used to fetch assistants, threads, messages, runs, et cetera. 

    **User Interface**

    The elements of the user interface are Streamlit components from Streamlit's API. 
    Although the functionality belongs to the app, the appearance is Streamlit code. 
    Streamlit allows for rapid development of novel things, such as Agora and Queequeg, by
    handling much of the boilerplate UI and hosting code.

    **Future**

    I am currently migrating this platform away from Streamlit to enable more 
    flexibility as the platform grows. Streamlit is excellent at 
    creating smaller apps really fast. I wrote the bulk of this app in several days. 
    At its core, however, it requires 
    code to be run at a high redundancy in certain use cases which slows things down. For this use 
    case, an event based execution model is required. React, a popular JS 
    framework, and Reflex, a React-based Python framework are under consideration.  
    """
)

st.caption("Version v1.2c")


st.divider()

#Nav
foot_l, foot_m, foot_r = st.columns(3)

with foot_m:
    if st.button("<- Previous Page", use_container_width=True):
        st.switch_page(last_page_visited)


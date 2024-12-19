import streamlit as st

st.session_state["last_page_visited"] = "more/thank_you.py"


#Helper functions
def reset_demo():
    
    st.session_state["disclaimer_acknowledged"] = False
    st.session_state["last_page_visited"] = "home/welcome.py"

    # - Pref
    
    st.session_state["avatar_choice"] = "🦁"
    st.session_state["topic_choice"] = "1_PicnicMystery"
    st.session_state["model_choice"] = "gpt-4o"

    # - Agora v2
    st.session_state["agora_v2_instructions_viewed"] = False
    st.session_state["agora_v2_assistant_id"] = None
    st.session_state["agora_v2_thread_id"] = None
    st.session_state["agora_v2_vector"] = None

    # - Agora v3
    st.session_state["agora_v3_instructions_viewed"] = False
    st.session_state["agora_v3_assistant_id"] = None
    st.session_state["agora_v3_thread_id"] = None
    st.session_state["agora_v3_vector"] = None
    st.session_state["agora_v3_qqg_id"] = None
    st.session_state["agora_v3_thread_qqg_id"] = None
    st.session_state["agora_v3_query_choice"] = None



#Messaging
st.title("Thank you!")
st.write("...for trying out ***Agora***!")
st.write(
    """
    Columbia Law School is my dream. By the numbers, my potential is below that of the average CLS applicant. 
    My drive speaks louder. This app exists to showcase my 
    technical skills, my commitment to empowering others, and my ability to innovate and solve problems. 
    **I'm applying with nothing to lose**, determined to bring my unique perspective, resilience, and skills to Columbia Law. 
    I will gladly accept defeat once I have given it my all. Until then, I proceed. This way, upon acceptance, I am deserving of 
    the opportunity that so many other qualified candidates do not receive. 
    """
)
st.write(
    "All the best,"
)
st.write(
    "***Jake Lindsay***"
)
st.write("L43133966")


#Nav
foot_l, foot_r = st.columns(2)

with foot_l:
    if st.button(":material/info: Learn how Agora works", use_container_width=True):
        st.switch_page("more/about.py")
with foot_r:
    if st.button(":material/replay: Start Demo Over", use_container_width=True):
        reset_demo()
        st.switch_page("home/welcome.py")


import streamlit as st

#Helper functions
def topic_change():
    #agora v2
    st.session_state["agora_v2_assistant_id"] = None
    st.session_state["agora_v2_thread_id"] = None
    st.session_state["agora_v2_vector"] = None
    #agora v3
    st.session_state["agora_v3_assistant_id"] = None
    st.session_state["agora_v3_thread_id"] = None
    st.session_state["agora_v3_vector"] = None
    st.session_state["agora_v3_qqg_id"] = None
    st.session_state["agora_v3_thread_qqg_id"] = None
    st.session_state["agora_v3_query_choice"] = None
    

#Messaging
st.title("Preferences")
st.write("A few choices to guide your conversation with **Agora**. You can change these at anytime.")
st.divider()


#Inputs
avatar_options = ["🦁", "⚖️", "🍎", "🦉", "🗽" ]
topic_options = ["1_PicnicMystery", "2_Contracts101", "3_Securities"]
model_options = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o"]

col1, col2 = st.columns(2)

with col1:
    st.session_state["avatar_choice"] = st.radio(
        "Please choose an avatar:",
        avatar_options,
        captions=[
            "Go Columbia Lions!",
            "Checks and balances.",
            "Welcome to NY!",
            "Alma Mater's Secret Owl...", 
            "Lady Liberty."
        ],
        index=avatar_options.index(st.session_state["avatar_choice"]),
    )

with col2:
    st.session_state["topic_choice"] = st.radio(
        "Please choose a topic:",
        topic_options,
        index=topic_options.index(st.session_state["topic_choice"]),
        on_change=topic_change
    )
    st.session_state["model_choice"] = st.radio(
        "Please choose a model:",
        model_options,
        captions=[
            "Older",
            "Fast, cheap",
            "Robust, pricier",
        ],
        index=model_options.index(st.session_state["model_choice"]),
        disabled=True
    )





#Nav
st.divider()
foot_lt, foot_rt = st.columns(2)
with foot_lt:
    if st.button("<- Explainer", use_container_width=True):
        st.switch_page("home/explainer.py")

with foot_rt:
    if st.button("Upload Files ->", use_container_width=True, type="primary"):
        st.switch_page("tools/upload_files.py")



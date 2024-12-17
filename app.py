import streamlit as st


#Pages

welcome = st.Page("home/welcome.py", title="Welcome", icon=":material/mood:", default=True)
explainer = st.Page("home/explainer.py", title="Explainer", icon=":material/trending_up:")

preferences = st.Page("tools/preferences.py", title="Preferences", icon=":material/tune:")
uploadFiles = st.Page("tools/upload_files.py", title="Upload Files", icon=":material/upload_file:")
manageApiKeys = st.Page("tools/manage_api_keys.py", title="Manage API keys", icon=":material/key:")
file_viewer = st.Page("tools/file_viewer.py", title="View Files", icon=":material/search:")
agora_v2 = st.Page("tools/agora_v2.py", title="Agora", icon=":material/robot_2:")

thankYou = st.Page("more/thank_you.py", title="Thank You", icon=":material/star:")
about = st.Page("more/about.py", title="About", icon=":material/info:")
disclaimer = st.Page("more/disclaimer.py", title="Disclaimer", icon=":material/warning:")

#Navigation

pg = st.navigation(
    {
        "Home": [welcome, explainer],
        "Tools": [preferences, uploadFiles, manageApiKeys, file_viewer, agora_v2],
        "More": [thankYou, about, disclaimer]
    }
)

#Run it!
pg.run()



#Default Settings -> Session State

if "disclaimer_acknowledged" not in st.session_state:
    st.session_state["disclaimer_acknowledged"] = False

if "avatar_choice" not in st.session_state:
    st.session_state["avatar_choice"] = "🦁"

if "topic_choice" not in st.session_state:
    st.session_state["topic_choice"] = "1_PicnicMystery"

if "model_choice" not in st.session_state:
    st.session_state["model_choice"] = "gpt-4o"

if "agora_v2_assistant_id" not in st.session_state:
    st.session_state["agora_v2_assistant_id"] = None

if "agora_v2_thread_id" not in st.session_state:
    st.session_state["agora_v2_thread_id"] = None

if "agora_v2_vector" not in st.session_state:
    st.session_state["agora_v2_vector"] = None

#API Keys -> Session State
if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = st.secrets["api_keys"]["openai_api_key"]




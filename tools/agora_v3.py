import streamlit as st

#Disclaimer control
if st.session_state["disclaimer_acknowledged"] == False:
    st.switch_page("more/disclaimer.py")



from openai import OpenAI
import json
import time
import os

#Helper functions
def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        time.sleep(0.2)
    return run


def set_agora_v3_query_choice(guten_tag):
    st.session_state["agora_v3_query_choice"] = guten_tag



#Status init
with st.sidebar:
    st.write("**Restart**")
    if st.button(":material/replay:"):
        st.session_state["agora_v3_instructions_viewed"] = False
        st.session_state["agora_v3_assistant_id"] = None
        st.session_state["agora_v3_thread_id"] = None
        st.session_state["agora_v3_vector"] = None
        st.session_state["agora_v3_qqg_id"] = None
        st.session_state["agora_v3_thread_qqg_id"] = None
        st.session_state["agora_v3_query_choice"] = None
        st.session_state["agora_v3_query_btn"] = None
    st.write("**Status**")


#Nav
head_l, head_r = st.columns(2)
with head_l:
    if st.button("<- View Files", use_container_width=True):
        st.switch_page("tools/file_viewer.py")
with head_r:
    if st.button("Complete Demo ->", use_container_width=True, type="primary"):
        st.switch_page("more/thank_you.py")
    

#Messaging
st.title("Agora Guide :material/explore:")

if st.session_state["agora_v3_instructions_viewed"] == False:
    st.write(
        """
        New instructions needed 1
        """    
    )

    st.write(
        """
        New instructions needed 2
        """
    )

    st.write(
        """
        New instructions needed 3
        """
    )

st.session_state["agora_v3_instructions_viewed"] = True

topic_choice = st.session_state["topic_choice"]
st.write(f"**Agora** has been trained on the `{topic_choice}` directory.")

st.divider()

#Open Client
client = OpenAI(api_key=st.session_state["openai_api_key"])

#Threads - create or plug in
thread = None
if st.session_state["agora_v3_thread_id"] == None:
    with st.sidebar:
        with st.spinner("Creating main thread..."):
            thread = client.beta.threads.create()
            st.session_state["agora_v3_thread_id"] = thread.id

thread_qqg = None
if st.session_state["agora_v3_thread_qqg_id"] == None:
    with st.sidebar:
        with st.spinner("Creating query thread..."):
            thread_qqg = client.beta.threads.create()
            st.session_state["agora_v3_thread_qqg_id"] = thread_qqg.id

#Agora - create new or plug in
agora = None
if st.session_state["agora_v3_assistant_id"] == None:
    
    with st.sidebar:
        with st.spinner("Creating Agora instance..."):
    
            #Create Agora
            agora = client.beta.assistants.create(
            name="Legal Research Assistant",
            instructions="You are a legal research assistant named Agora. You answer with facts, and avoid encroaching upon the users critical thinking. Do not write complete drafts for essays.",
            model=st.session_state["model_choice"],
            tools=[{"type": "file_search"}],
            )
            st.session_state["agora_v3_assistant_id"] = agora.id

            #Prompt Agora
            client.beta.threads.messages.create(
                thread_id=st.session_state["agora_v3_thread_id"],
                role="user",
                content="Hi, please introduce yourself, and offer help with legal research."
            )

            #Initial Run
            init_run = client.beta.threads.runs.create(
                thread_id=st.session_state["agora_v3_thread_id"],
                assistant_id=st.session_state["agora_v3_assistant_id"]
            )
            with st.sidebar:
                with st.spinner("Running initial query..."):
                    init_run = wait_on_run(init_run, st.session_state["agora_v3_thread_id"])

#Queequeg (query generating agent)
qqg = None
if st.session_state["agora_v3_qqg_id"] == None:

    with st.sidebar:
        with st.spinner("Creating Queequeg instance..."):
            #Create Queequeg
            qqg = client.beta.assistants.create(
                name="Query Generator",
                instructions="You are going to generate queries for a user to use based on a message thread and a vector store.",
                model=st.session_state["model_choice"],
                tools=[{"type": "file_search"}],
            )
            st.session_state["agora_v3_qqg_id"] = qqg.id



#Vector - create new or plug in
vector = None
topic_path = st.session_state["topic_choice"]
if st.session_state["agora_v3_vector"] == None:

    with st.sidebar:
        with st.spinner("Creating new vector..."):

            vector = client.beta.vector_stores.create(name="Files")
            file_names = os.listdir(f"resources/data/{topic_path}")
            file_paths = [f"resources/data/{topic_path}/{file_name}" for file_name in file_names]
            file_streams = [open(file_path, "rb") for file_path in file_paths]
            file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector.id,
                files=file_streams
            )
            st.session_state["agora_v3_vector"] = vector
else:
    vector = st.session_state["agora_v3_vector"]


#Give the Vector to the Agora and Queequeg
agora = client.beta.assistants.update(
    assistant_id = st.session_state["agora_v3_assistant_id"],
    tool_resources = {"file_search": {"vector_store_ids": [vector.id]}}
)
qqg = client.beta.assistants.update(
    assistant_id = st.session_state["agora_v3_qqg_id"],
    tool_resources = {"file_search": {"vector_store_ids": [vector.id]}}
)

#Run Previous Query, if there is one
if st.session_state["agora_v3_query_choice"] != None:
    client.beta.threads.messages.create(
        thread_id=st.session_state["agora_v3_thread_id"],
        role="user",
        content=st.session_state["agora_v3_query_choice"],
    )

    prev_query_run = client.beta.threads.runs.create(
        thread_id=st.session_state["agora_v3_thread_id"],
        assistant_id=st.session_state["agora_v3_assistant_id"],
    )

    with st.sidebar:
        with st.spinner("Running query..."):
            prev_query_run = wait_on_run(prev_query_run, st.session_state["agora_v3_thread_id"])



#Chat
#Load Messages 
messages = client.beta.threads.messages.list(thread_id=st.session_state["agora_v3_thread_id"])

for message in reversed(messages.data[:-1]):
    if message.role == "user":
        st.chat_message(message.role, avatar=st.session_state["avatar_choice"]).write(message.content[0].text.value)
    elif message.role == "assistant":
        st.chat_message(message.role).write(message.content[0].text.value)

#Get queries
current_messages = client.beta.threads.messages.list(thread_id=st.session_state["agora_v3_thread_id"])
message_string = (
    """
    Provide 3 queries for a user to learn about the files based on the contents of the files.
    Return the three queries in the following json format.
    Phrase the queries as questions. 
    Capitilize the first word in each queries. 
    Include question marks at the end of the queries.
    Keep the queries shorter.
    Do not include anything else in your response. The json:
    {
        "query1":"the first query",
        "query2":"the second query",
        "query3":"the third query",
    }

    References the following messages that have already taken place about the files:

    """
)
for message in reversed(current_messages.data):
    message_string = message_string + message.content[0].text.value + " \n "
    
client.beta.threads.messages.create(
    thread_id=st.session_state["agora_v3_thread_qqg_id"],
    role="user",
    content=message_string
)

query_fetch = client.beta.threads.runs.create(
    thread_id = st.session_state["agora_v3_thread_qqg_id"],
    assistant_id = st.session_state["agora_v3_qqg_id"]
)
with st.sidebar:
    with st.spinner("Fetching queries..."):
        query_fetch = wait_on_run(query_fetch, st.session_state["agora_v3_thread_qqg_id"])

query_response = client.beta.threads.messages.list(thread_id=st.session_state["agora_v3_thread_qqg_id"]).data[0].content[0].text.value
query_options = json.loads(query_response)

print(query_options["query1"])
print(query_options["query2"])
print(query_options["query3"])
print("Hallo!")

#New Message
st.button(query_options["query1"], key="qo1", on_click=set_agora_v3_query_choice(query_options["query1"]))
st.button(query_options["query2"], key="qo2", on_click=set_agora_v3_query_choice(query_options["query2"]))
st.button(query_options["query3"], key="qo3", on_click=set_agora_v3_query_choice(query_options["query3"]))



#Done, ready to go!
with st.sidebar:
    st.success("Ready", icon=":material/check_circle:")
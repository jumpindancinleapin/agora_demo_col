import streamlit as st


st.session_state["last_page_visited"] = "home/welcome.py"

#Image


st.image(
        "resources/images/garden.jpg",
        caption=None,
)


#Messaging
st.subheader("Welcome, Columbia Law!")

st.write("**Thank you for your time!** Please find a demonstration of the platform I describe in my personal statement. -Jake")

#Nav
col1, col2, col3 = st.columns(3)
with col2:

    if st.button("Get Started ->", use_container_width=True, type="primary"):
        st.switch_page("home/explainer.py")


import streamlit as st

#Image
head_l, head_m, head_r = st.columns(3)
with head_m:
    st.image(
            "resources/images/columbia_law_brand.jpg",
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


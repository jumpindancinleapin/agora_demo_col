import streamlit as st



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
        st.switch_page("home/welcome.py")


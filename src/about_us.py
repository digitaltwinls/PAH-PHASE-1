import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget





def main_about_us():
    st.header('About Us')
    st.markdown('---')
# Create three columns
    col1, col2, col3 = st.columns(3)

    # First column: Photo and information
    with col3:
        st.image("src/akshay_linkedin_photo.jpeg", width=150)
        st.markdown("**Name:** Akshay Bhat")
        st.markdown("**Role:** Data Scientist")


    # Second column: Photo and information
    with col2:
        st.image("src/kranthi_linkedin.jpeg", width=150)
        st.markdown("**Name:** Kranthi Addanki")
        st.markdown("**Role:** Co-founder")


    # Third column: Photo and information
    with col1:
        st.image("src/narayan_linkedin.jpeg", width=150)
        st.markdown("**Name:** Narayan Kumar A")
        st.markdown("**Role:** Founder")




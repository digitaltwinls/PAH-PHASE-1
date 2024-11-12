import streamlit as st
st.set_page_config(layout="wide")

from streamlit_option_menu import option_menu
import time
import json
from streamlit.components.v1 import html
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
import pandas as pd
import plotly.express as px
from src.document_analysis import document_analysis # for document analysis
from src.trend_analysis import trend_analysis #for trend analysis
from src.about_us import main_about_us

# st.set_page_config(layout="wide")

with st.sidebar:
    app = option_menu(
        menu_title='Menu',
        options=['Home', 'Analysis', 'About', 'Contact'],
        icons=['house-fill','ui-checks', 'person-circle','info-circle-fill'],
        menu_icon='chat-text-fill',
        default_index=0)

#Home 
if app == 'Home':
    st.header('Digital Twin Learning Solution')
    st.markdown('---')

#analysis
if app == 'Analysis':
    st.header('AI-Assisted Learning Pathway Recognition')
    st.markdown('---')
    nav_bar = option_menu(
        menu_title=None,
        options=['Document Analysis', 'Trend Analysis'],
        icons=['bar-chart-fill', 'graph-up-arrow'],
        menu_icon="cast", default_index=0, orientation="horizontal")
    
    #single document analysis
    if nav_bar == 'Document Analysis':
        document_analysis()
        
    #trend analysis
    if nav_bar == 'Trend Analysis':
        trend_analysis()

#about
if app == 'About':
    main_about_us()

#contact
if app == 'Contact':
    st.header('Contact')
    st.markdown('---')
    st.markdown('Please contact us at [kranthi@digitaltwinls.com.au](mailto:kranthi@digitaltwinls.com.au)')


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)












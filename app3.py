import streamlit as st
from Home import main as home_app
from page1 import main as page1_app
from Resource import main as Resource_app
PAGES = {
    "Home": home_app,
    "Page 1": page1_app,
    "Resource":Resource_app
}
st.sidebar.title('Select')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()



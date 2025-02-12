import streamlit as st
from PIL import Image
def main():
    st.title(":red[HOTEL RESERVATION PREDICTION]")
    st.write("The objective of my project is to ascertain the cancellation status of each customer's reservation by analyzing their reservation information")
    img = Image.open('Hotel booking.jpg')
    st.image(img, width=600)
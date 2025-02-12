import streamlit as st
import pickle


def main():
    st.title(":red[HOTEL RESERVATION PREDICTION]")
    # img = Image.open('Hotel booking.jpg')
    # st.image(img, width=425)
    adults_no=st.selectbox("No of Adults",(0,1,2,3,4),)
    childrens_no=st.selectbox("No of Childrens",(0,1,2,3,9,10),)
    weekend_nights=st.text_input("No Of Weekend Nights",'')
    week_nights=st.text_input("No of Week Nights",'')
    meal_plan=st.selectbox("Meal Plan",('Meal Plan 1','Not Selected','Meal Plan 2','Meal Plan 3'),)
    if meal_plan=="Mean Plan 1":
        mp=0
    elif meal_plan=="Meal Plan 2":
        mp=1
    elif meal_plan=="Meal Plan 3'":
        mp=2
    else:
        mp=3
    car_space=st.radio("Enter Required Car Parking Space",options=[0,1])
    room_type=st.selectbox("Enter Room Type",('Room_Type 1','Room_Type 4','Room_Type 2','Room_Type 6',
       'Room_Type 5','Room_Type 7','Room_Type 3'),)
    if room_type=='Room_Type 1':
        rt=0
    elif room_type=='Room_Type 2':
        rt=1
    elif room_type=='Room_Type 3':
        rt=2
    elif room_type=='Room_Type 4':
        rt=3
    elif room_type=='Room_Type 5':
        rt=4
    elif room_type=='Room_Type 6':
        rt=5
    else:
        rt=6
    lead_time=st.text_input("Enter Lead Time",'')
    arrival_year=st.radio("Enter Arrival Year",options=[2017,2018])
    if arrival_year==2017:
        ay=0
    else:
        ay=1
    arrival_month=st.text_input("Enter Arrival Month",'')
    arrival_date=st.text_input("Enter Arrival Date",'')
    market_seg=st.selectbox("Enter Market Segment Type",('Offline','Online','Corporate','Aviation','Complementary'),)
    if market_seg=='Aviation':
        ms=0
    elif market_seg=='Complementary':
        ms=1
    elif market_seg=='Corporate':
        ms=2
    elif market_seg=='Offline':
        ms=3
    else:
        ms=4
    repeated_guest=st.radio("Are You Repeated Guest Or Not",options=[0,1])
    previous_cancelation=st.text_input("Enter No Of Previous Cancellation",'')
    previous_not_cancel=st.text_input("Enter No Of Not Previous Cancellation",'')
    # avg_price=st.text_input("Enter Average Price Per Room",'')
    avg_price=st.slider("Enter Average Price Per Room",0,1000)
    special_guest=st.selectbox("Enter No Of Special Geust",(0,1,2,3,4,5),)
    features=[adults_no,childrens_no,weekend_nights,week_nights,mp,car_space,rt,lead_time,ay,arrival_month,arrival_date,ms,repeated_guest,previous_cancelation,previous_not_cancel,avg_price,special_guest]
    scaled=pickle.load(open('scales.sav','rb'))
    model=pickle.load(open('modale.sav','rb'))
    pred=st.button('PREDICT')
    if pred:
        result=model.predict(scaled.transform([features]))
        if result==0:
            st.write("Booking is cancelled")
        else:
            st.write("Booking is not cancelled")

#     url = 'https://colab.research.google.com/drive/1BHollBuAti8iCZXEQcrjms2uauxDM9FY#scrollTo=Ef4wiYhZ5cQ4'
#     st.write("Check Out This link For Code:['https://colab.research.google.com/drive/1BHollBuAti8iCZXEQcrjms2uauxDM9FY#scrollTo=Ef4wiYhZ5cQ4'](%s)" % url)
# main()

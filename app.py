import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import sklearn

crop_model = pickle.load(open('crop_prediction.pkl','rb'))
fertilizer_model = pickle.load(open('fertilizer_prediction.pkl','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('AgriHelper',
                           ['Crop Prediction',
                            'Fertilizer Prediction'],
                           icons=['ear_of_rice', 'medicine'],
                           default_index=0)

# Crop Prediction Page
if (selected == 'Crop Prediction'):

    # page title
    st.title('Crop Prediction using ML')
    st.subheader("Note:")
    st.text('Based on Your Soil Testing, Enter the Percentage of Nutrients in your Soil.')
    st.text('To do the Soil testing, You can go to your nearby soil testing laborateries.')
    link = '[See Here](https://farmer.gov.in/stl.aspx)'
    st.markdown(link, unsafe_allow_html=True)
    st.divider()

    col21, col22 = st.columns(2)
    col1, col2, col3 = st.columns(3)

    with col21:
        temperature = st.number_input("Temperature")

    with col22:
        humidity = st.number_input("Humidity")

    with col21:
        rainfall = st.number_input("Rainfall")

    with col22:
        ph = st.number_input("Ph")

    with col1:
        nitrogen = st.slider("Nitrogen", 0, 100)

    with col2:
        potassium = st.slider("Potassium", 0, 100)

    with col3:
        phosphorous = st.slider("Phosphorous", 0, 100)

    # code for Prediction
    result = ''

    # creating a button for Prediction

    if st.button('Predict'):

        result = crop_model.predict(np.array([[nitrogen, potassium, phosphorous, temperature, humidity, ph, rainfall]]))
        if result[0] == 0:
            result = 'Crop Name: Apple'
        elif result[0] == 1:
            result = 'Crop Name: Banana'
        elif result[0] == 2:
            result = 'Crop Name: Blackgram'
        elif result[0] == 3:
            result = 'Crop Name: Chickpea'
        elif result[0] == 4:
            result = 'Crop Name: Coconut'
        elif result[0] == 5:
            result = 'Crop Name: Coffee'
        elif result[0] == 6:
            result = 'Crop Name: Cotton'
        elif result[0] == 7:
            result = 'Crop Name: Grapes'
        elif result[0] == 8:
            result = 'Crop Name: Jute'
        elif result[0] == 9:
            result = 'Crop Name: Kidneybeans'
        elif result[0] == 10:
            result = 'Crop Name: Lentil'
        elif result[0] == 11:
            result = 'Crop Name: Maize'
        elif result[0] == 12:
            result = 'Crop Name: Mango'
        elif result[0] == 13:
            result = 'Crop Name: Mothbeans'
        elif result[0] == 14:
            result = 'Crop Name: Mungbean'
        elif result[0] == 15:
            result = 'Crop Name: Musk Melon'
        elif result[0] == 16:
            result = 'Crop Name: Orange'
        elif result[0] == 17:
            result = 'Crop Name: Papaya'
        elif result[0] == 18:
            result = 'Crop Name: Pigeonpeas'
        elif result[0] == 19:
            result = 'Crop Name: Pomegranate'
        elif result[0] == 20:
            result = 'Crop Name: rice'
        else:
            result = 'Crop Name: watermelon'

        print(result)

    st.success('The output is {}'.format(result))


# Fertilizer Prediction Page

if (selected == 'Fertilizer Prediction'):

    # page title
    st.title('Fertilizer Prediction using ML')

    st.subheader("Note:")
    st.text('Based on Your Soil Testing, Enter the Percentage of Nutrients in your Soil.')
    st.text('To do the Soil testing, You can go to your nearby soil testing laborateries.')
    link = '[See Here](https://farmer.gov.in/stl.aspx)'
    st.markdown(link, unsafe_allow_html=True)
    st.divider()

    col21, col22 = st.columns(2)

    with col21:
        cropType = st.selectbox("Crop Type", ("Barley","Cotton", "Ground Nuts", "Maize", "Millets", "Oil seeds", "Paddy", "Pulses", "Sugarcane", "Tobacco", "Wheat"))
        croptype = 0
        if cropType == "Barley":
            croptype = 0
        elif cropType == "Cotton":
            croptype = 1
        elif cropType == "Ground Nuts":
            croptype = 2
        elif cropType == "Maize":
            croptype = 3
        elif cropType == "Millets":
            croptype = 4
        elif cropType == "Oil seeds":
            croptype = 5
        elif cropType == "Paddy":
            croptype = 6
        elif cropType == "Pulses":
            croptype = 7
        elif cropType == "Sugarcane":
            croptype = 8
        elif cropType == "Tobacco":
            croptype = 9
        elif cropType == "Wheat":
            croptype = 10


    with col22:
        soilType = st.selectbox("Soil Type", ("Black", "Clayey", "Loamy", "Red", "Sandy"))
        soiltype = 0
        if soilType == "Black":
            soiltype = 0
        elif soilType == "Clayey":
            soiltype = 1
        elif soilType == "Loamy":
            soiltype = 2
        elif soilType == "Red":
            soiltype = 3
        elif soilType == "Sandy":
            soiltype = 4


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.number_input("Temperature")

    with col2:
        humidity = st.number_input("Humidity")

    with col3:
        moisture = st.number_input("Moisture")

    with col1:
        nitrogen = st.slider("Nitrogen", 0,50)

    with col2:
        potassium = st.slider("Potassium", 0,50)

    with col3:
        phosphorous = st.slider("Phosphorous", 0,50)

    # code for Prediction
    result = ''

    # creating a button for Prediction

    if st.button('Predict'):

        result = fertilizer_model.predict(np.array([[temperature,humidity,moisture,soiltype,croptype,nitrogen,potassium,phosphorous]]))
        if result[0] == 0:
            result = 'Fertilizer name: 10-26-26'
        elif result[0] == 1:
            result = 'Fertilizer name: 14-35-14'
        elif result[0] == 2:
            result = 'Fertilizer name: 17-17-17'
        elif result[0] == 3:
            result = 'Fertilizer name: 20-20'
        elif result[0] == 4:
            result = 'Fertilizer name: 28-28'
        elif result[0] == 5:
            result = 'Fertilizer name: DAP'
        else:
            result = 'Fertilizer name: UREA '

        print(result)

    st.success('The output is {}'.format(result))


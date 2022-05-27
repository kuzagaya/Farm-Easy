import streamlit as st 
from crop import function
from fertiliser import fertiliser_app
from PIL import Image


st.set_page_config(
     page_title="FarmEasy",
     page_icon="🌾",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




image = Image.open('farmeasy.png')
st.sidebar.image(image)

st.sidebar.header('Menu Bar:')

user_choice = st.sidebar.radio('Go to',('Home','Crop Recommendation','Fertiliser Recommender','About'))

if user_choice == 'Crop Recommendation':
    function()
if user_choice == 'Fertiliser Recommender':
    fertiliser_app()
if user_choice == 'Home':
    image2 = Image.open('design.png')
    st.image(image2)
    st.write('''This app recommend you crop for your farm based on the soil quality. 
                This app not made for use in real life scenario.The data to train model for the prediction is collected from
                the Kaggle so, there is not much credibility in it. This app just made for fun and 
                showcasing the proof of concept.
             ''')
if user_choice == 'About':
    st.write('Name:')
    st.info('Gurpreet')
    st.write('Contact:')
    st.info('gurpreetmeelu900@gmail.com')
    st.markdown('''### LinkedIn: [Gurpreet](https://www.linkedin.com/in/gurpreet-meelu-68421a201/)''')
    




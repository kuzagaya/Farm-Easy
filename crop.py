import streamlit as st
import pickle



def crop_rec(lst):
    loaded_model = pickle.load(open('models/RF_model.pkl','rb'))
    x = loaded_model.predict([lst])
    return x 

    

def function():
    st.header('Crop Recommendation', )
    with st.form("Crop Recommender"):
        nitrogen = st.number_input('Nitrogen',value = 90 )
        phosphorous = st.number_input('Phosphorous',value = 42 )
        pottasium = st.number_input('pottasium',value = 43)
        temperature = st.number_input('Temperature')
        humidity = st.number_input('Humidity',value = 82)
        ph_level = st.number_input('ph Level',value = 6.5)
        rainfall = st.number_input('Rainfall',value = 202)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        lst = [nitrogen, phosphorous, pottasium, temperature, humidity, ph_level, rainfall]

    if submitted:
    
        ans = crop_rec(lst)
        st.success(f'We recommend you to grow {ans[0].capitalize()} on your land.', )
        st.snow()

        

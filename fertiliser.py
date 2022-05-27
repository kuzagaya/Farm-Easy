import streamlit as st
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
import numpy as np

def recommend_fertiliser(lst):
    loaded_model = pickle.load(open('models XGBModel.pkl','rb'))
    col_transformer = pickle.load(open('models\col_transformer.pkl','rb'))
    value = np.array(lst)
    value = col_transformer.transform([value])
    ans = loaded_model.predict(value)
    return ans

def fertiliser_app():
    st.header('Fertiliser Recommender')
    st.write("This app recommend you about the type of fertiliser to be applied which is best suited for respective conditions")
    with st.form("Fertiliser Recommender"):
        temperature = st.number_input('Temperature',value = 26)
        humidity = st.number_input('Humidity',value = 52)
        moisture = st.number_input('Moisture',value = 32)
        soil__type = st.selectbox('Enter the type of soil', ('Sandy', 'Loamy', 'Black', 'Red', 'Clayey'))
        crop__type = st.selectbox('Enter the type of Crop you want to grow', ('Maize','Sugarcane','Cotton','Tobacco','Paddy','Barley', 'Wheat', 'Millets', 'Oil seeds','Pulses','Ground Nuts'))
        nitrogen = st.number_input('Nitrogen',value = 3)
        pottasium = st.number_input('pottasium',value = 0)
        phosphorous = st.number_input('Phosphorous',value = 0 )
        
        submitted = st.form_submit_button("Submit")
        lst = [temperature, humidity, moisture, soil__type, crop__type, nitrogen, pottasium, phosphorous]
    
    if submitted:
    
        ans = recommend_fertiliser(lst)
        st.success(f'Fertiliser Recommended: {ans[0].capitalize()}' )
        st.snow()









if __name__ == '__main__':
    fertiliser_app()

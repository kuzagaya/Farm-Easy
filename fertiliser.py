import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def recommend_fertiliser(lst):
    df = pd.read_csv('dataset/Fertilizer Prediction.csv')
    features = ['Temparature', 'Humidity ', 'Moisture', 'Soil Type', 'Crop Type','Nitrogen', 'Potassium', 'Phosphorous']
    label = ['Fertilizer Name']
    X = df[features].copy()
    y = df[label].copy()
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3,4])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    value = np.array(lst)

    value = ct.transform([value])
    ans = model.predict(value)
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

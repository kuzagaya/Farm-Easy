import pickle

loaded_model = pickle.load(open('models/RF_model.pkl','rb'))
x = loaded_model.predict([[90,	42,	43,	20.879744,	82.002744,	6.502985,	202.935536]])
print(x)
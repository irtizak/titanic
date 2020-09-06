import streamlit as st
import joblib
import sklearn
import numpy as np

# Load model
filepath_model = ''
model = joblib.load('model.joblib')

# Create sliders for values
pclass = st.selectbox('Passenger Class', range(1, 4))
sex = st.selectbox('Sex', range(0, 2))
age = st.slider('Age', 1, 80)
sblng_sps = st.selectbox('Siblings/Spouses Aboard', range(0, 9))
prnts_chld = st.selectbox('Parents/Children Aboard', range(0, 7))
fare = st.slider('Fare', 1, 513)

#Transformations
if sex == 'Male':
    sex_m = 1
    sex_f = 0
else:
    sex_m = 0
    sex_f = 1

# Make prediction
feature_list = [pclass, age, sex_m, sex_f, fare, sblng_sps, prnts_chld]
# print(np.array(feature_list))

prediction = model.predict(np.array(feature_list).reshape(1, -1))
if prediction == [1]:
    pred_label = 'survived'
else:
    pred_label = 'did not survive'

st.write('The passenger {}.'.format(pred_label))
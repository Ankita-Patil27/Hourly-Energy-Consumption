import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime

st.title("Welcome to Energy Consumption Project")


st.sidebar.header('User Input Parameters')

no_days = st.sidebar.number_input("Insert Number of days", min_value=1, max_value=365, step=1)

with open("Linear_Regression_Final_Model.pkl", mode="rb") as f:
    model = pickle.load(f)

data=pd.read_csv('Daywise Consumption Data.csv',index_col='Datetime',parse_dates=True)
data.rename({'PJMW_MW':'MW'},inplace=True,axis=1)
forecast_check_data = np.array(data['MW'][:'2018-07-04'][-7:])
z=forecast_check_data

for i in range(0,no_days):
    ck=z[-7:]
    ck=np.array([ck])
    lin_f_chk=model.predict(ck)
    z=np.append(z,lin_f_chk)
    i=+1
future_pred_lr=z[-no_days:]

#ct = datetime.datetime.now() + datetime.timedelta(days=1)
#ct_1 = datetime.datetime.now() + datetime.timedelta(days=no_days)
#Predict=pd.date_range(ct,ct_1, freq='D')
Predict = pd.date_range(start='4/8/2018',periods=no_days,tz=None,freq = 'D')
future_df = pd.DataFrame(index=Predict)
future_df['Forecast'] = future_pred_lr.tolist()
st.write(future_df)

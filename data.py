import numpy as np 
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import RFE,SelectFromModel
from sklearn.ensemble import RandomForestClassifier 
import os 
import pickle

path=r'E:\python_practise\python_practise\project\work_home\work_from_home_burnout_dataset.csv'
def load_data()->pd.DataFrame:
    df=pd.read_csv(path)
    return df 

def burnout_risk(data):
    if data=='Low':
        return 1 
    elif data=='Medium':
        return 2 
    else:
        return 3

def day_type(data):
    if data=='Weekday':
        return 1 
    else:
        return 2
    

df=load_data()
df_copy=df.copy()
df_copy['burnout']=df_copy['burnout_risk'].apply(burnout_risk)
df_copy['day_types']=df_copy['day_type'].apply(day_type)

# def feature_data()->pd.DataFrame:
#     df_copy['burnout']=df_copy['burnout_risk'].apply(burnout_risk)
#     df_copy['day_types']=df_copy['day_type'].apply(day_type)
#     return df_copy 

input_col=['user_id','day_types','work_hours','screen_time_hours','meetings_count','breaks_taken','after_hours_work','sleep_hours','task_completion_rate',
'burnout_score']
output_col='burnout'
x=df_copy[input_col]
y=df_copy[output_col]

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

def data_pipeline():
    model = RandomForestClassifier(max_depth=10)
    pipeline=Pipeline(steps=[
        ('selectmodel',SelectFromModel(model)),
        ('model',model)
    ])
    return pipeline.fit(x_train,y_train)

def predict():
    model_fit =data_pipeline()
    y_pred = model_fit.predict(x_test)
    return y_pred 






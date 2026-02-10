from fastapi import FastAPI,HTTPException, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field 
from typing import Annotated,Literal,Optional 
import pandas as pd 
import pickle 
import numpy as np

with open ('model.pkl','rb') as f:
   model =  pickle.load(f)

app=FastAPI()

class UserIn(BaseModel):
    user_id:Annotated[int,Field(...,description='id of the employee',examples=[1])]
    day_types:Annotated[str,Field(...,description='Day types',examples=['Weekday','Weekend'])]
    work_hours:Annotated[float,Field(...,description='Hourly works')]
    screen_time_hours:Annotated[float,Field(...,description='Screen times')] 
    meetings_count:Annotated[float,Field(...,description='Total count of meetings',ge=0)]
    breaks_taken:Annotated[int,Field(...,ge=0)]
    after_hours_work:Annotated[int,Field(...,ge=0)]
    sleep_hours:Annotated[float,Field(...,ge=0)] 
    task_completion_rate:Annotated[float,Field(...,ge=0,le=100)]
    burnout_score:Annotated[float,Field(...,ge=0,le=100)] 


@app.get('/')
def get_home():
    return {'message': 'Hello ! this is Employee performance page..'}

@app.post('/predict')
def predict(data:UserIn):
    input_df=pd.DataFrame([{
        'user_id':data.user_id,
        'day_types':data.day_types,
        'work_hours':data.work_hours,
        'screen_time_hours':data.screen_time_hours,
        'meetings_count':data.meetings_count,
        'breaks_taken':data.breaks_taken,
        'after_hours_work':data.after_hours_work,
        'sleep_hours': data.sleep_hours,
        'task_completion_rate':data.task_completion_rate,
        'burnout_score':data.burnout_score
    }])
    predition=model.predict(input_df)[0]
    
    if isinstance(predition, (np.integer, np.floating)):
        predition = predition.item()  # Converts numpy.int64 or numpy.float64 to int/float
    # print(predition)
    mapping={1:'Low',2:'Medium',3:'Low'}
    
    return JSONResponse(status_code=200,content={'Predicted result': mapping.get(predition,'unknown')})
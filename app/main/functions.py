from .. import db
from ..models import Actor
from flask_sqlalchemy import SQLAlchemy
import pandas as pd 
from datetime import datetime, timedelta 


def return_col(column_name):
    query = Actor.query.all()
    result = []
    
    if column_name == 'first_name':
        for item in query:
            result.append(item.first_name)
        return result
    
    if column_name == 'last_name':
        for item in query:
            result.append(item.last_name)
        return result
    
    if column_name == 'last_update':
        for item in query:
            result.append(item.last_update)
        return result
        

def return_df(selected_cols):
    columns = []

    if not isinstance(selected_cols, (list, tuple)):
        selected_cols = [selected_cols]
        
    df = pd.DataFrame(columns=selected_cols)
    
    for column in selected_cols:
        columns.append(column)

   
    for column in columns:
        df[column] = return_col(column)
    
    return df.head()

def days_ago(num_days):
    
    days_ago = datetime.now() - timedelta(num_days)
    
    return days_ago 
    


    
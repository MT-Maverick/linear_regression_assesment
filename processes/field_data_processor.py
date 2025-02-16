import pandas as pd
import sqlite3

class FieldDataProcessor():  
    def __init__(self,config_params):
        self.config_params = config_params
        self.df = pd.DataFrame()

    def process(self):    
        
        try:
            db_file = self.config_params['db_path']
            query = self.config_params['sql_query']
            conn = sqlite3.connect(db_file)
            df = pd.read_sql_query(query,conn)
            conn.close()
            
            df.rename(columns = self.config_params['columns_to_rename'] , inplace=True)           
            df.rename(columns= {'Crop_type_temp':'Crop_type'} , inplace=True)
            df['Crop_type'] = df['Crop_type'].replace(self.config_params['values_to_rename'])
            df['Crop_type'] = df['Crop_type'].apply(lambda x: x.strip())
            df.drop(columns={'Min_temperature_C','Max_temperature_C','Plot_size','Annual_yield','Latitude','Longitude'},inplace=True)
            self.df = df
            return self.df
            
        except Exception as e:
            return (f"Error loading data: {e}")
        
  



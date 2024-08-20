import pandas as pd
import os
import data_validation as dv

def save_registration_data(registration_data):
    #Path to the existing CSV file
    csv_file = 'data.csv'
    existed_record = dv.check_user_id_existance(csv_file, registration_data['email'])
    print(type(existed_record))
    new_df = pd.DataFrame([registration_data])
    if existed_record == None : pass 
    elif type(existed_record) == list and existed_record[0].empty :
        
        new_df = pd.concat([existed_record[1], new_df], ignore_index=True)
        
    elif type(existed_record) == list and not existed_record[0].empty :
        return False 
        # raise ValueError(f"Registration failed the email {registration_data['email']} is already existed ")
            
    new_df.to_csv(csv_file, index=False)
    return True
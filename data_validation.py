
import re
from datetime import datetime
import pandas as pd
import os

def validate_name(name,pattern):
    try:
        if len(name) > 3 and len(name) < 30 and re.match(pattern, name):
            return True
        else:
           raise ValueError("Entered name is invalid, name length should be >3 and <30 chars and not allowed space, special characters")
    except ValueError as ve:
        raise ve
    except Exception as e:
            raise e

def validate_age(age_input):
    try:
        if not age_input.isdigit():
            raise ValueError("Entered value is incorrect, please provide valid age") 
        age=int(age_input)
        if age < 18 or age > 100:
            raise ValueError("Age should be grater than 18 and less than 100 ")  
        else:
            return True
    except ValueError as ve:
        raise ve
    except Exception as e:
            raise e
    
def validate_email(email,allowed_domains,pattern):
    try:
        if email.count('@') != 1:
            raise ValueError("Invalid email format. The email must contain Domain part.")

        domain_part = email.split('@')
        domain = domain_part[1].split('.')[0]
        
        if domain not in allowed_domains:
            raise ValueError("Sorry for the inconvenience, we only allow domains like gmail and yahoo.")

        if not re.match(pattern, email):
           raise ValueError("Invalid email format or domain.")
        else:
            return True
            
    except ValueError as ve:
       raise ve
    except Exception as e:
        raise e


def validate_dob(dob: str):
    try:
        # Attempt to parse the date with the expected format
        datetime.strptime(dob, '%d/%m/%Y')
        return True
    except ValueError:
        # Raise a ValueError if the date format is invalid
        raise ValueError(f"The provided date '{dob}' is invalid. Please use the format dd/mm/yyyy.")
    
def validate_password(password: str):
    try:
        # Password must be at least 8 characters long
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        # Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError("Password must contain at least one special character.")
        return password
    except ValueError as ve:
       raise ve
    except Exception as e:
        raise e
    
def confirm_password(confirm_password: str,password: str):
    try:
            # Check if the confirmed password matches the original password
        if password != confirm_password:
            raise ValueError("Password and confirm_password do not match.")
    except ValueError as ve:
        raise ve


def validate_phone_number(phone_number: str):
        try: # Phone number must be exactly 10 digits long and contain only numbers
            if not phone_number.isdigit():
                raise ValueError("Entered value is incorrect, please provide a valid phone number.")
            if not re.fullmatch(r'\d{10}', phone_number):
                raise ValueError("Phone number must be exactly 10 digits long and contain only numbers.")
            return True
        except ValueError as ve:
            raise ve
        

def check_user_id_existance(csv_file, email):
    if os.path.exists(csv_file):
            main_df = pd.read_csv(csv_file)
            is_email_existed = main_df[main_df['email'] == email]
            return [is_email_existed,main_df]
    else : return None
           # is_email_existance = main_df['email'].str.contains(email).any()
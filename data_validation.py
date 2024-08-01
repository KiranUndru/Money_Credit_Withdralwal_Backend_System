import re

class ValidationError(Exception):
    pass

def validation_name(name):
    #print(f"Inside validation name function{name}")
    pattern = r'^[a-zA-Z]+$'
    if len(name) > 3 and len(name) < 30 and re.match(pattern, name):
        print(f"{name} is valid ")
        
    else:
        print(f"{name} is invalid, please enter only charactors")
        

def validate_first_name(first_name):
    validation_name(first_name)

def validate_last_name(last_name):
    validation_name(last_name)
    
def validate_age(age):
    if  not age.isdigit():
      raise ValidationError
    age=int(age)    
    if age < 0 or (18 < age <100):
     print(f"Age {age} is valid")
    else :
        raise ValidationError
    